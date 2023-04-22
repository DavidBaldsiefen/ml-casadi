from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=['ml_casadi', 'ml_casadi.torch', 'ml_casadi.common', 'ml_casadi.torch.modules', 'ml_casadi.torch.modules.nn', 'ml_casadi.torch.math', 'ml_casadi.torch.matrix', 'ml_casadi.torch.autograd'],
    package_dir={'': '.'}
)

setup(**setup_args)