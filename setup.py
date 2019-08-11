from setuptools import setup

setup(
    name='mylib',
    version='0.1',
    packages=['mylib',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    test_suite="mylib_tests"
)
