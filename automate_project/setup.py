#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Victor Dashmohapatra",
    author_email='victordashmohapatra@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="this is basic end to end project",
    entry_points={
        'console_scripts': [
            'automate_project=automate_project.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='automate_project',
    name='automate_project',
    packages=find_packages(include=['automate_project', 'automate_project.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/victordashmohapatra/automate_project',
    version='0.0.1',
    zip_safe=False,
)
