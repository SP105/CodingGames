# from distutils.dist import Distribution
from setuptools import setup, Distribution, find_packages


class BinaryDistribution(Distribution):
    def is_pure(self):
        return False


def parse_requirements(requirements):
    with open(requirements) as f:
        return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]


setup(name='sp-coding-solutions',
      version='1.0',
      description='Repository for solutions for the CodingGame web',
      long_description=open('README.md').read(),
      project_urls={'Source': 'https://github.com/SP105/CodingGames', },
      author='Santiago Panizza',
      author_email='panizzasantiago@gmail.com',
      packages=find_packages(include=['*'], exclude=['test*']),
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