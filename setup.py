from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=["nyu_finger", "nyu_finger_sim"], package_dir={"": "python"}
)

setup(**d)
