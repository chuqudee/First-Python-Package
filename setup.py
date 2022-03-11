from setuptools import setup, find_packages

setup(
    name='First Python Package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='EDSA',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<chuqudee>/<First-Python-Package>',
    author='<Michael Okereafor>',
    author_email='<niky4u2nv@gmail.com>'
)