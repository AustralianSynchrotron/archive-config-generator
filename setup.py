from setuptools import setup
import re

with open('archiveconfig/__init__.py') as file:
    version = re.search(r"__version__ = '(.*)'", file.read()).group(1)

setup(
    name='archiveconfig',
    version=version,
    maintainer='Robbie Clarken',
    maintainer_email='robbie.clarken@synchrotron.org.au',
    url='https://github.com/AustralianSynchrotron/archive-config-generator',
    license='MIT',
    packages=['archiveconfig'],
    install_requires=['click', 'jinja2'],
    entry_points={
        'console_scripts': [
            'archive-config-generator=archiveconfig.cli:main',
        ],
    },
    package_data={
        'archiveconfig': ['templates/*.xml'],
    },
)
