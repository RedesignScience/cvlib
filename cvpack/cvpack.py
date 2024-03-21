"""
.. module:: cvpack
   :platform: Linux, MacOS, Windows
   :synopsis: Useful Collective Variables for OpenMM

.. moduleauthor:: Charlles Abreu <craabreu@gmail.com>

"""

import collections
import inspect
import typing as t

import openmm
import yaml
from openmm import app as mmapp

from cvpack import unit as mmunit

from .serializer import Serializable
from .unit import value_in_md_units
from .utils import compute_effective_mass, get_single_force_state


class SerializableAtom(Serializable):
    r"""
    A serializable version of OpenMM's Atom class.
    """

    def __init__(  # pylint: disable=super-init-not-called
        self, atom: t.Union[mmapp.topology.Atom, "SerializableAtom"]
    ) -> None:
        self.name = atom.name
        self.index = atom.index
        if isinstance(atom, mmapp.topology.Atom):
            self.element = atom.element.symbol
            self.residue = atom.residue.index
        else:
            self.element = atom.element
            self.residue = atom.residue
        self.id = atom.id

    def __getstate__(self) -> t.Dict[str, t.Any]:
        return self.__dict__

    def __setstate__(self, keywords: t.Dict[str, t.Any]) -> None:
        self.__dict__.update(keywords)


SerializableAtom.registerTag("!cvpack.Atom")


class SerializableResidue(Serializable):
    r"""A serializable version of OpenMM's Residue class."""

    def __init__(  # pylint: disable=super-init-not-called
        self, residue: t.Union[mmapp.topology.Residue, "SerializableResidue"]
    ) -> None:
        self.name = residue.name
        self.index = residue.index
        if isinstance(residue, mmapp.topology.Residue):
            self.chain = residue.chain.index
        else:
            self.chain = residue.chain
        self.id = residue.id
        self._atoms = list(map(SerializableAtom, residue.atoms()))

    def __getstate__(self) -> t.Dict[str, t.Any]:
        return self.__dict__

    def __setstate__(self, keywords: t.Dict[str, t.Any]) -> None:
        self.__dict__.update(keywords)

    def __len__(self) -> int:
        return len(self._atoms)

    def atoms(self):
        """Iterate over all Atoms in the Residue."""
        return iter(self._atoms)


SerializableResidue.registerTag("!cvpack.Residue")


class BaseCollectiveVariable(openmm.Force, Serializable):
    r"""
    An abstract class with common attributes and method for all CVs.
    """

    _unit: mmunit.Unit = mmunit.dimensionless
    _mass_unit: mmunit.Unit = mmunit.dalton * mmunit.nanometers**2
    _args: t.Dict[str, t.Any] = {}
    _period: t.Optional[float] = None

    def __getstate__(self) -> t.Dict[str, t.Any]:
        return self._args

    def __setstate__(self, keywords: t.Dict[str, t.Any]) -> None:
        self.__init__(**keywords)

    def __copy__(self):
        return yaml.safe_load(yaml.safe_dump(self))

    def __deepcopy__(self, memo):
        return yaml.safe_load(yaml.safe_dump(self))

    def _registerCV(
        self,
        unit: mmunit.Unit,
        *args: t.Any,
        **kwargs: t.Any,
    ) -> None:
        """
        Register the newly created BaseCollectiveVariable subclass instance.

        This method must always be called from Subclass.__init__.

        Parameters
        ----------
            unit
                The unit of measurement of this collective variable. It must be a unit
                in the MD unit system (mass in Da, distance in nm, time in ps,
                temperature in K, energy in kJ/mol, angle in rad).
            args
                The arguments needed to construct this collective variable
            kwargs
                The keyword arguments needed to construct this collective variable
        """
        cls = self.__class__
        self.setName(cls.__name__)
        self._unit = unit
        self._mass_unit = mmunit.dalton * (mmunit.nanometers / self.getUnit()) ** 2
        arguments, _ = self._getArguments()
        self._args = dict(zip(arguments, args))
        self._args.update(kwargs)

    def _registerPeriod(self, period: float) -> None:
        """
        Register the period of this collective variable.

        This method must called from Subclass.__init__ if the collective variable is
        periodic.

        Parameters
        ----------
            period
                The period of this collective variable
        """
        self._period = period

    @classmethod
    def _getArguments(cls) -> t.Tuple[collections.OrderedDict, collections.OrderedDict]:
        """
        Inspect the arguments needed for constructing an instance of this collective
        variable.

        Returns
        -------
        OrderedDict
            A dictionary with the type annotations of all arguments
        OrderedDict
            A dictionary with the default values of optional arguments

        Example
        -------
            >>> import cvpack
            >>> args, defaults = cvpack.RadiusOfGyration._getArguments()
            >>> for name, annotation in args.items():
            ...     print(f"{name}: {annotation}")
            group: typing.Iterable[int]
            pbc: <class 'bool'>
            weighByMass: <class 'bool'>
            >>> print(*defaults.items())
            ('pbc', False) ('weighByMass', False)
        """
        arguments = collections.OrderedDict()
        defaults = collections.OrderedDict()
        for name, parameter in inspect.signature(cls).parameters.items():
            arguments[name] = parameter.annotation
            if parameter.default is not inspect.Parameter.empty:
                defaults[name] = parameter.default
        return arguments, defaults

    def _setUnusedForceGroup(self, system: openmm.System) -> None:
        """
        Set the force group of this collective variable to the one at a given position
        in the ascending ordered list of unused force groups in an :OpenMM:`System`.

        .. note::

            Evaluating a collective variable (see :meth:`getValue`) or computing its
            effective mass (see :meth:`getEffectiveMass`) is more efficient when the
            collective variable is the only force in its own force group.

        Parameters
        ----------
            system
                The system to search for unused force groups

        Raises
        ------
            RuntimeError
                If all force groups are already in use
        """
        used_groups = {force.getForceGroup() for force in system.getForces()}
        new_group = next(filter(lambda i: i not in used_groups, range(32)), None)
        if new_group is None:
            raise RuntimeError("All force groups are already in use.")
        self.setForceGroup(new_group)

    def getUnit(self) -> mmunit.Unit:
        """
        Get the unit of measurement of this collective variable.
        """
        return self._unit

    def getPeriod(self) -> t.Optional[mmunit.SerializableQuantity]:
        """
        Get the period of this collective variable.

        Returns
        -------
            The period of this collective variable or None if it is not periodic
        """
        if self._period is None:
            return None
        return mmunit.SerializableQuantity(self._period, self.getUnit())

    def addToSystem(
        self, system: openmm.System, set_unused_force_group: bool = True
    ) -> None:
        """
        Add this collective variable to an :OpenMM:`System`.

        Parameters
        ----------
        system
            The system to which this collective variable should be added
        set_unused_force_group
            If True, the force group of this collective variable will be set to the
            first available force group in the system
        """
        if set_unused_force_group:
            self._setUnusedForceGroup(system)
        system.addForce(self)

    def getValue(self, context: openmm.Context) -> mmunit.Quantity:
        """
        Evaluate this collective variable at a given :OpenMM:`Context`.

        .. note::

            This method will be more efficient if the collective variable is the only
            force in its force group (see :OpenMM:`Force`).

        Parameters
        ----------
        context
            The context at which this collective variable should be evaluated

        Returns
        -------
        unit.Quantity
            The value of this collective variable at the given context


        Example
        -------
        In this example, we compute the values of the backbone dihedral angles and
        the radius of gyration of an alanine dipeptide molecule in water:

        >>> import cvpack
        >>> import openmm
        >>> from openmmtools import testsystems
        >>> model = testsystems.AlanineDipeptideExplicit()
        >>> top = model.mdtraj_topology
        >>> backbone_atoms = top.select("name N C CA and resid 1 2")
        >>> phi = cvpack.Torsion(*backbone_atoms[0:4])
        >>> psi = cvpack.Torsion(*backbone_atoms[1:5])
        >>> radius_of_gyration = cvpack.RadiusOfGyration(
        ...     top.select('not water')
        ... )
        >>> for cv in [phi, psi, radius_of_gyration]:
        ...     cv.addToSystem(model.system)
        >>> context = openmm.Context(
        ...     model.system, openmm.VerletIntegrator(0)
        ... )
        >>> context.setPositions(model.positions)
        >>> print(phi.getValue(context))
        3.1415... rad
        >>> print(psi.getValue(context))
        3.1415... rad
        >>> print(radius_of_gyration.getValue(context))
        0.29514... nm
        """
        state = get_single_force_state(self, context, getEnergy=True)
        value = value_in_md_units(state.getPotentialEnergy())
        return mmunit.Quantity(value, self.getUnit())

    def getEffectiveMass(self, context: openmm.Context) -> mmunit.Quantity:
        r"""
        Compute the effective mass of this collective variable at a given
        :OpenMM:`Context`.

        The effective mass of a collective variable :math:`q({\bf r})` is defined as
        :cite:`Chipot_2007`:

        .. math::

            m_\mathrm{eff}({\bf r}) = \left(
                \sum_{i=1}^N \frac{1}{m_i} \left\|
                    \frac{dq}{d{\bf r}_i}
                \right\|^2
            \right)^{-1}

        .. note::

            This method will be more efficient if the collective variable is the only
            force in its force group (see :OpenMM:`Force`).

        Parameters
        ----------
        context
            The context at which this collective variable's effective mass should be
            evaluated

        Returns
        -------
        unit.Quantity
            The effective mass of this collective variable at the given context

        Example
        -------
            In this example, we compute the effective masses of the backbone dihedral
            angles and the radius of gyration of an alanine dipeptide molecule in water:

            >>> import cvpack
            >>> import openmm
            >>> from openmmtools import testsystems
            >>> model = testsystems.AlanineDipeptideExplicit()
            >>> top = model.mdtraj_topology
            >>> backbone_atoms = top.select("name N C CA and resid 1 2")
            >>> phi = cvpack.Torsion(*backbone_atoms[0:4])
            >>> psi = cvpack.Torsion(*backbone_atoms[1:5])
            >>> radius_of_gyration = cvpack.RadiusOfGyration(
            ...     top.select('not water')
            ... )
            >>> for cv in [phi, psi, radius_of_gyration]:
            ...     _ = cv._setUnusedForceGroup(model.system)
            ...     _ = model.system.addForce(cv)
            >>> context = openmm.Context(
            ...     model.system, openmm.VerletIntegrator(0)
            ... )
            >>> context.setPositions(model.positions)
            >>> print(phi.getEffectiveMass(context))
            0.05119... nm**2 Da/(rad**2)
            >>> print(psi.getEffectiveMass(context))
            0.05186... nm**2 Da/(rad**2)
            >>> print(radius_of_gyration.getEffectiveMass(context))
            30.946... Da
        """
        return mmunit.Quantity(compute_effective_mass(self, context), self._mass_unit)
