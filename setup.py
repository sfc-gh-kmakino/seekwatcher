from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import numpy

setup(
    name='seekwatcher',
    version="0.13",
    cmdclass={'build_ext': build_ext},
    ext_modules=[
        Extension(
            'seekwatcher.rundata',
            ['seekwatcher/rundata.pyx'],
            include_dirs = [numpy.get_include()]),
        Extension(
            'seekwatcher.blkparse',
            ['seekwatcher/blkparse.pyx'],
            include_dirs = [numpy.get_include()])
    ],
    scripts=['cmd/seekwatcher'],
    packages=['seekwatcher'])
