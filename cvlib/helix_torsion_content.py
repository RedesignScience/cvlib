"""
.. class:: HelixTorsionContent
   :platform: Linux, MacOS, Windows
   :synopsis: Fractional alpha-helix torsion content of a sequence of residues

.. classauthor:: Charlles Abreu <craabreu@gmail.com>

"""

from typing import Iterable

import openmm
from openmm import app as mmapp
from openmm import unit as mmunit

from .cvlib import AbstractCollectiveVariable, QuantityOrFloat, in_md_units


class HelixTorsionContent(openmm.CustomTorsionForce, AbstractCollectiveVariable):
    """
    Fractional :math:`\\alpha`-helix Ramachandran content of a sequence of `n` residues:

    .. math::

        \\alpha_{\\phi,\\psi}({\\bf r}) = \\frac{1}{2(n-2)} \\sum_{i=2}^{n-1} \\left[
            B_m\\left(
                \\frac{\\phi_i({\\bf r}) - \\phi_{\\rm ref}}{\\theta_{\\rm tol}}
            \\right) +
            B_m\\left(
                \\frac{\\psi_i({\\bf r}) - \\psi_{\\rm ref}}{\\theta_{\\rm tol}}
            \\right)
        \\right]

    where :math:`\\phi_i({\\bf r})` and :math:`\\psi_i({\\bf r})` are the Ramachandran dihedral
    angles of residue :math:`i`, :math:`\\phi_{\\rm ref}` and :math:`\\psi_{\\rm ref}` are their
    reference values in an alpha helix :cite:`Hovmoller_2002`, and :math:`\\theta_{\\rm tol}` is
    the threshold tolerance around these refenrences. The function :math:`B_m(x)` is a smooth
    `boxcar function <https://en.wikipedia.org/wiki/Boxcar_function>`_

    .. math::
        B_m(x) = \\frac{1}{1 + x^{2m}}

    where :math:`m` is an integer parameter that controls its steepness.

    .. note::

        The residues must be from a single chain and be ordered in sequence. The :math:`\\phi` and
        :math:`\\psi` angles of the first and last residues are not considered. They are used to
        compute the dihedral angles of the second and penultimate residues, respectively.

    Parameters
    ----------
        residues
            The residues in the sequence
        phiReference
            The reference value of the phi dihedral angle in an alpha helix
        psiReference
            The reference value of the psi dihedral angle in an alpha helix
        tolerance
            The threshold tolerance around the reference values
        halfExponent
            The parameter :math:`m` of the boxcar function

    Raises
    ------
        ValueError
            If some residue does not contain a :math:`\\phi` or :math:`\\psi` angle

    Example
    -------
        >>> import cvlib
        >>> import openmm as mm
        >>> from openmm import app, unit
        >>> from openmmtools import testsystems
        >>> model = testsystems.LysozymeImplicit()
        >>> residues = [r for r in model.topology.residues() if 59 <= r.index <= 79]
        >>> print(*[r.name for r in residues])
        LYS ASP GLU ALA GLU LYS LEU PHE ASN GLN ASP VAL ASP ALA ALA VAL ARG GLY ILE LEU ARG
        >>> helix_content = cvlib.HelixTorsionContent(residues)
        >>> model.system.addForce(helix_content)
        6
        >>> platform = openmm.Platform.getPlatformByName('Reference')
        >>> integrator = openmm.VerletIntegrator(0)
        >>> context = openmm.Context(model.system, integrator, platform)
        >>> context.setPositions(model.positions)
        >>> print(helix_content.evaluateInContext(context, 6))
        0.918571 dimensionless

    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        residues: Iterable[mmapp.topology.Residue],
        phiReference: QuantityOrFloat = -63.8 * mmunit.degrees,
        psiReference: QuantityOrFloat = -41.1 * mmunit.degrees,
        tolerance: QuantityOrFloat = 25 * mmunit.degrees,
        halfExponent: int = 3,
    ) -> None:
        def find_atom(residue: mmapp.topology.Residue, name: str) -> int:
            for atom in residue.atoms():
                if atom.name == name:
                    return atom.index
            raise ValueError(f"Could not find atom {name} in residue {residue.name}{residue.id}")

        phi_ref, psi_ref, tol = map(in_md_units, [phiReference, psiReference, tolerance])
        num_torsions = 2 * (len(residues) - 2)
        super().__init__(f"{1/num_torsions}/(1+x^{2*halfExponent}); x=(theta-theta_ref)/{tol}")
        self.addPerTorsionParameter("theta_ref")
        for i in range(1, len(residues) - 1):
            self.addTorsion(
                find_atom(residues[i - 1], "C"),
                find_atom(residues[i], "N"),
                find_atom(residues[i], "CA"),
                find_atom(residues[i], "C"),
                [phi_ref],
            )
            self.addTorsion(
                find_atom(residues[i], "N"),
                find_atom(residues[i], "CA"),
                find_atom(residues[i], "C"),
                find_atom(residues[i + 1], "N"),
                [psi_ref],
            )
        self._registerCV(mmunit.dimensionless, residues, phi_ref, psi_ref, tol, halfExponent)
