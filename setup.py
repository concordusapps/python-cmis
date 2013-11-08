#!/usr/bin/env python
from setuptools import setup, find_packages
from imp import load_source


setup(
    name='cmis',
    version=load_source('', 'cmis/_version.py').__version__,
    description='A server architecture built on top of a solid foundation '
                'provided by flask, sqlalchemy, and various extensions.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    author='Concordus Applications',
    author_email='support@concordusapps.com',
    url='http://github.com/concordusapps/python-cmis',
    packages=find_packages('.'),
    dependency_links=[
        'git+git://github.com/concordusapps/python-cmislib.git@topics/py3k'
        '#egg=cmislib-dev',
    ],
    install_requires=[
        "cmislib == dev"
    ],
)
