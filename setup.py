# from distutils.dist import Distribution
from setuptools import setup, find_namespace_packages, Distribution
from mng.trkcampaigns import __version__, __name__


class BinaryDistribution(Distribution):
    def is_pure(self):
        return False


def parse_requirements(requirements):
    with open(requirements) as f:
        return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]


setup(name=__name__,
      version=__version__,
      description='Several sudoko solvers',
      long_description=open('README.md').read(),
      project_urls={'Source': 'https://bitbucket.intranet.mango.es/projects/BD/repos/mng-trkcampaigns/browse', },
      author='Santiago Panizza',
      author_email='santiago.panizza.sge@mango.com',
      packages=find_namespace_packages(include=['mng.*'], exclude=['test*']),
      include_package_data=True,
      distclass=BinaryDistribution,
      install_requires=parse_requirements('requirements.txt'),
      extras_require={},  # Install extra requires when running: pip install {pkg} interactive
      license="Apache License 2.0",
      python_requires=">= 3.7",
      classifiers=[
          "Private :: Do Not Upload",
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3.7',
      ],
      )