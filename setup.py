from setuptools import setup, find_packages

setup(
    name='weather',
    version='0.90',
    description='Weather Underground client library',
    author='Austin Gabel',
    author_email='agabel@gmail.com',
    url='https://github.com/agabel/python-underground',
    packages=find_packages(),
    license='MIT License',
    install_requires=['simplejson >= 2.1.0',],
    keywords='weather, underground',
)
