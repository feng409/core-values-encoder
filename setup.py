from distutils.core import setup
import cve

setup(
    # py_modules=['cve.society'],
    py_modules=['cve.society', 'cve.society2', 'cve.society3'],
    name='cve',
    entry_points={'console_scripts': ['society=cve.command:main']},
    version='0.1',
    description='core socialist values encoding',
    author='chemf',
    author_email='eoyohe@gmail.com',
    url='https://github.com/feng409/core-values-encoder',
)
