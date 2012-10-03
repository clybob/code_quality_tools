code_quality_tools
==================

What is a code_quality_tools?
-----------------------------

code_quality_tools is a little API, in python, to collect some data about code quality of your application.


Usage
-----

- Get Pep8 errors and warnings without save output
'''
from code_quality_tools import CodeQualityCheck

check = CodeQualityCheck()
check.get_pep8_errors(path='application/path/')
'''

- Get Pep8 errors and warnings saving output
'''
from code_quality_tools import CodeQualityCheck

check = CodeQualityCheck()
check.get_pep8_errors(path='application/path/', output_file='pep8_errors.txt')
'''

- Get Pep8 errors and warnings passing extra options
'''
from code_quality_tools import CodeQualityCheck

check = CodeQualityCheck()
check.get_pep8_errors(path='application/path/', options=['--exclude=fixtures'])
'''

All examples above returns something as:
'''
{
    'total_errors': 1,
    'list_errors': ['./code_quality_tools.py:60:80: E501 line too long (98 characters)']
}
'''


Dependencies
------------

- Pep8 (http://pypi.python.org/pypi/pep8)
- PyFlakes (http://pypi.python.org/pypi/pyflakes)
- CloneDigger (http://pypi.python.org/pypi/clonedigger)
- JSHint (https://npmjs.org/package/jshint)
- CSSLint (https://npmjs.org/package/csslint)


Author
------

**Romulo Tavares**

- https://github.com/clybob


Colaborators
------------

**Zacarias Eugenio**


License
-------

