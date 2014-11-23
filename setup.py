#!/usr/bin/env python
from setuptools import setup

setup(name='mochad_logger',
      version='0.0.2',
      description='A Logging Utility for Mochad',
      author='Dan Brooks',
      author_email='dan@cs.uml.edu',
      url='http://www.github.com/mrdanbrooks/mochad_logger',
      scripts=['mochad_logger'],
      data_files=[('/etc/mochad_logger',['config/mochad_logger.conf']),
                  ('/etc/udev/rules.d',['debian/91-mochad-logger.rules'])],
      install_requires=['twisted']
      )
