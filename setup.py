from setuptools import setup, find_packages

setup(
    name='my_calculator',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'my_calculator=calculator.__init__:main',
        ],
    },
)

