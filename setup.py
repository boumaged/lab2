from setuptools import setup
setup(
name='calculator',
version='1.0.0',
py_modules=['calculator'],
install_requires=[],
entry_points={
'console_scripts': [
'calculator=calculator:main',
],
},
)


