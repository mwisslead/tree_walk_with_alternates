from setuptools import setup

VERSION='0.0.1'

setup(
    name='tree_walk_with_alternates',
    version=VERSION,
    description='Tree walking library for data where alternate branches can be taken if key isn\'t found',
    author='Michael Wisslead',
    author_email='michael.wisslead@gmail.com',
    url='https://github.com/mwisslead',
    packages=['tree_walk_with_alternates'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
