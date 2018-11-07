from setuptools import setup

setup(
    packages=['cve'],
    name='cve',
    entry_points={'console_scripts': ['cve=cve.command:main']},
    version='0.1',
    description='core socialist values encoding',
    author='chemf',
    author_email='eoyohe@gmail.com',
    url='https://github.com/feng409/core-values-encoder',
)
