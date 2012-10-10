# encoding: utf-8

from distutils.core import setup

setup(
    name='CodeQualityTools',
    version='0.1.0',
    author='Romulo Tavares',
    author_email='clybob@hotmail.com',
    packages=['code_quality_tools'],
    license='GPL',
    url='https://github.com/clybob/code_quality_tools.git',
    description='code_quality_tools is a little API, in python, ' +
                'to collect some data about code quality of your ' +
                'source code (python, css, js).',
    long_description=open('README.md').read(),
    install_requires=['pep8', 'pyflakes', 'clonedigger'],
    entry_points={
        'console_scripts': ['code_quality_tools = install:main']
    },
)
