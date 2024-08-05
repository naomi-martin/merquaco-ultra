import pathlib
from setuptools import setup, find_packages
#from merquaco.__init__ import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# Get requirements
REQUIREMENTS = (HERE / "requirements.txt").read_text()
requirements = REQUIREMENTS.splitlines()

setup(
    name="merquaco-ultra",
    version="0.0.1",
    description="Tools for QC on MERSCOPE datasets",
    author="Naomi Martin, Paul Olsen",
    author_email="naomi.martin@alleninstitute.org, paul.olsen@alleninstitute.org",
    url="https://github.com/naomi-martin/merquaco-ultra",
    license = "LICENSE",
    packages=find_packages(where="."),
	package_data={
		'': ['*.ilp'],
        'merquaco-ultra': ['../ilastik_models/*.ilp'],
    },
	include_package_data=True,
    install_requires=requirements,
    # entry_points={
    #     "console_scripts": [
    #         "merquaco = merquaco.quaco:run",
    #     ],
    # }
)
