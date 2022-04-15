# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Mom6(CMakePackage):
    """The MOM6 Ocean Model"""

    homepage = "https://github.com/mom-ocean/MOM6"
    git      = "https://github.com/angus-g/MOM6"

    maintainers = ['angus-g']

    variant('symmetric', default=True, description='symmetric memory?')

    version('master', branch='cmake', submodules=True)

    depends_on('fms')

    def cmake_args(self):
        args = [
            self.define_from_variant('SYMMETRIC')
        ]

        args.append(self.define('CMAKE_Fortran_COMPILER', self.spec['mpi'].mpifc))

        return args
