"""
.. class:: Torsion
   :platform: Linux, MacOS, Windows
   :synopsis: The torsion angle formed by four atoms

.. classauthor:: Charlles Abreu <craabreu@gmail.com>

"""

import openmm
from openmm import unit as mmunit

from .cvlib import AbstractCollectiveVariable


class Torsion(openmm.CustomTorsionForce, AbstractCollectiveVariable):
    """
    The torsion angle formed by four atoms:

    .. math::

        \\varphi({\\bf r}) = {\\rm atan2}\\left(\\frac{
            ({\\bf r}_{2,1} \\times {\\bf r}_{3,4}) \\cdot {\\bf u}_{2,3}
        }{
            {\\bf r}_{2,1} \\cdot {\\bf r}_{3,4} - ({\\bf r}_{2,1} \\cdot {\\bf u}_{2,3})
                                                   ({\\bf r}_{3,4} \\cdot {\\bf u}_{2,3})
        }\\right),

    where :math:`{\\bf r}_{i,j} = {\\bf r}_j - {\\bf r}_i`,
    :math:`{\\bf u}_{2,3} = {\\bf r}_{2,3}/\\|{\\bf r}_{2,3}\\|`,
    and `atan2 <https://en.wikipedia.org/wiki/Atan2>`_ is the arctangent function that receives
    the numerator and denominator above as separate arguments.

    Parameters
    ----------
        atom1
            The index of the first atom
        atom2
            The index of the second atom
        atom3
            The index of the third atom
        atom4
            The index of the fourth atom
        pbc
            Whether to use periodic boundary conditions

    Example:
        >>> import cvlib
        >>> import openmm as mm
        >>> system = mm.System()
        >>> [system.addParticle(1) for i in range(4)]
        [0, 1, 2, 3]
        >>> torsion = cvlib.Torsion(0, 1, 2, 3, pbc=False)
        >>> system.addForce(torsion)
        0
        >>> integrator = mm.VerletIntegrator(0)
        >>> platform = mm.Platform.getPlatformByName('Reference')
        >>> context = mm.Context(system, integrator, platform)
        >>> positions = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 1]]
        >>> context.setPositions([mm.Vec3(*pos) for pos in positions])
        >>> print(torsion.getValue(context, digits=6))
        1.570796 rad

    """

    def __init__(  # pylint: disable=too-many-arguments
        self, atom1: int, atom2: int, atom3: int, atom4: int, pbc: bool = False
    ) -> None:
        super().__init__("theta")
        self.addTorsion(atom1, atom2, atom3, atom4, [])
        self.setUsesPeriodicBoundaryConditions(pbc)
        self._registerCV(mmunit.radians, atom1, atom2, atom3, atom4, pbc)
