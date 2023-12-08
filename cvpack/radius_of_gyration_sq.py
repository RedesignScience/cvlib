"""
.. class:: RadiusOfGyrationSq
   :platform: Linux, MacOS, Windows

   :synopsis: The square of the radius of gyration of a group of atoms

.. classauthor:: Charlles Abreu <craabreu@gmail.com>

"""

from typing import Sequence

from cvpack import unit as mmunit

from .radius_of_gyration import _RadiusOfGyrationBase


class RadiusOfGyrationSq(_RadiusOfGyrationBase):
    """
    The square of the radius of gyration of a group of :math:`n` atoms:

    .. math::

        r_g^2({\\bf r}) = \\frac{1}{n} \\sum_{i=1}^n \\left\\|
            {\\bf r}_i - {\\bf r}_c({\\bf r})
        \\right\\|^2.

    where :math:`{\\bf r}_c({\\bf r})` is the geometric center of the group:

    .. math::

        {\\bf r}_c({\\bf r}) = \\frac{1}{n} \\sum_{i=j}^n {\\bf r}_j

    Optionally, the radius of gyration can be computed with respect to the center of
    mass of the group. In this case, the geometric center is replaced by:

    .. math::

        {\\bf r}_m({\\bf r}) = \\frac{1}{M} \\sum_{i=1}^n m_i {\\bf r}_i

    where :math:`M = \\sum_{i=1}^n m_i` is the total mass of the group.

    .. note::

        This collective variable is better parallelized than :class:`RadiusOfGyration`
        and might be preferred over :class:`RadiusOfGyration` when the group of atoms is
        large.

    Parameters
    ----------
        group
            The indices of the atoms in the group
        pbc
            Whether to use periodic boundary conditions
        weighByMass
            Whether to use the center of mass of the group instead of its geometric
            center

    Example
    -------
        >>> import cvpack
        >>> import openmm
        >>> from openmmtools import testsystems
        >>> model = testsystems.AlanineDipeptideVacuum()
        >>> num_atoms = model.system.getNumParticles()
        >>> rgsq = cvpack.RadiusOfGyrationSq(list(range(num_atoms)))
        >>> model.system.addForce(rgsq)
        5
        >>> platform =openmm.Platform.getPlatformByName('Reference')
        >>> integrator =openmm.VerletIntegrator(0)
        >>> context =openmm.Context(model.system, integrator, platform)
        >>> context.setPositions(model.positions)
        >>> print(rgsq.getValue(context, digits=6))  # doctest: +ELLIPSIS
        0.0871... nm**2

    """

    def __init__(
        self, group: Sequence[int], pbc: bool = False, weighByMass: bool = False
    ) -> None:
        num_atoms = len(group)
        super().__init__(2, f"distance(g1, g2)^2/{num_atoms}", group, pbc, weighByMass)
        for atom in group:
            self.addBond([atom, num_atoms])
        self._registerCV(mmunit.nanometers**2, group, pbc, weighByMass)
