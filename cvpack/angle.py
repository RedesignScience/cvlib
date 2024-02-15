"""
.. class:: Angle
   :platform: Linux, MacOS, Windows
   :synopsis: The angle formed by three atoms

.. classauthor:: Charlles Abreu <craabreu@gmail.com>

"""

import math

import openmm

from cvpack import unit as mmunit

from .cvpack import BaseCollectiveVariable


class Angle(openmm.CustomAngleForce, BaseCollectiveVariable):
    r"""
    The angle formed by three atoms:

    .. math::

        \theta({\bf r}) =
            \mathrm{acos}\left(
                \frac{{\bf r}_{2,1} \cdot {\bf r}_{2,3} }
                       {\| {\bf r}_{2,1} \| \| {\bf r}_{2,3} \|}
            \right),

    where :math:`{\bf r}_{i,j} = {\bf r}_j - {\bf r}_i`.

    Parameters
    ----------
        atom1
            The index of the first atom
        atom2
            The index of the second atom
        atom3
            The index of the third atom
        pbc
            Whether to use periodic boundary conditions

    Example:
        >>> import cvpack
        >>> import openmm
        >>> system =openmm.System()
        >>> [system.addParticle(1) for i in range(3)]
        [0, 1, 2]
        >>> angle = cvpack.Angle(0, 1, 2)
        >>> system.addForce(angle)
        0
        >>> integrator =openmm.VerletIntegrator(0)
        >>> platform =openmm.Platform.getPlatformByName('Reference')
        >>> context =openmm.Context(system, integrator, platform)
        >>> positions = [[0, 0, 0], [1, 0, 0], [1, 1, 0]]
        >>> context.setPositions([openmm.Vec3(*pos) for pos in positions])
        >>> print(angle.getValue(context, digits=6))
        1.570796 rad

    """

    yaml_tag = "!cvpack.Angle"

    def __init__(self, atom1: int, atom2: int, atom3: int, pbc: bool = False) -> None:
        super().__init__("theta")
        self.addAngle(atom1, atom2, atom3, [])
        self.setUsesPeriodicBoundaryConditions(pbc)
        self._period = 2 * math.pi
        self._registerCV(mmunit.radians, atom1, atom2, atom3, pbc)
