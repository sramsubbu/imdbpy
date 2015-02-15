from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='IMDBClient',
      version=version,
      description="A third party imdb cli utility",
      long_description="""\
A third party utility for IMDb website using the omdbapi, written in python""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python IMDb cli',
      author='Ramasubramanian S',
      author_email='sramsubu@gmail.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
