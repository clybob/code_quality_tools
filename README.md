code_quality_tools
==================

[![Build Status](https://secure.travis-ci.org/tarsis/code_quality_tools.png?branch=clonedigger_inconsistency)](https://travis-ci.org/tarsis/code_quality_tools)

What is a code_quality_tools?
-----------------------------

code_quality_tools is a little API, in python, to collect some data about code quality of your source code (python, css, js).


What metrics can I get?
-----------------------

+ Pep8 -> ```get_pep8_errors()```
+ PyFlakes -> ```get_pyflakes_errors()```
+ JSHint -> ```get_jshint_errors()```
+ CSSLint -> ```get_csslint_errors()```
+ CloneDigger -> ```get_clonedigger_errors()```
+ ALL -> ```get_all_errors()```


Usage
-----

Get Pep8, PyFlakes, JSHint or CSSLint errors and warnings without save output:
``` python
from code_quality_tools import CodeQualityCheck

check = CodeQualityCheck()
check.get_pep8_errors(path='application/path/')  # or
check.get_pyflakes_errors(path='application/path/')  # or
check.get_jshint_errors(path='application/path/')  # or
check.get_csslint_errors(path='application/path/')
```

Get Pep8, PyFlakes, JSHint or CSSLint errors and warnings saving output:
``` python
from code_quality_tools import CodeQualityCheck

check = CodeQualityCheck()
check.get_pep8_errors(path='application/path/', output_file='pep8_errors.txt')  # or
check.get_pyflakes_errors(path='application/path/', output_file='pyflakes_errors.txt')  # or
check.get_jshint_errors(path='application/path/', output_file='jshint_errors.txt')  # or
check.get_csslint_errors(path='application/path/', output_file='csslint_errors.txt')
```

Get Pep8, PyFlakes, JSHint or CSSLint errors and warnings passing extra options:
``` python
from code_quality_tools import CodeQualityCheck

check = CodeQualityCheck()
check.get_pep8_errors(path='application/path/', options=['--exclude=some/path/'])  # or
check.get_pyflakes_errors(path='application/path/', options=['--exclude=some/path/'])  # or
check.get_jshint_errors(path='application/path/', options=['--exclude=some/path/'])  # or
check.get_csslint_errors(path='application/path/', options=['--exclude=some/path/'])
```

All examples above returns something as:
``` python
{
    'total_errors': 1,
    'list_errors': ['./code_quality_tools.py:60:80: E501 line too long (98 characters)']
}
```

Get CloneDigger percentage or total of code duplicate without save output:
``` python
from code_quality_tools import CodeQualityCheck

check = CodeQualityCheck()
check.get_clonedigger_errors(path='application/path/')
```

Get CloneDigger percentage or total of code duplicate saving output:
``` python
from code_quality_tools import CodeQualityCheck

check = CodeQualityCheck()
check.get_clonedigger_errors(path='application/path/', output_file='clonedigger_statistics.html')
```

Get CloneDigger percentage or total of code duplicate passing extra options:
``` python
from code_quality_tools import CodeQualityCheck

check = CodeQualityCheck()
check.get_clonedigger_errors(path='application/path/', options='--ignore-dir=some/path/')
```

All examples of CloneDigger returns something as:
``` python
{
    'total_clones': 1,
    'percentage_clones': 100
}
```

Get all metrics of code quality:
``` python
from code_quality_tools import CodeQualityCheck

check = CodeQualityCheck()
check.get_all_errors(path='application/path/')
```

This example returns something as:
``` python
{
    'pep8': {
        'total_errors': 1, 
        'list_errors': ['./code_quality_tools.py:75:80: E501 line too long (98 characters)']
    }, 
    'clonedigger': {
        'percentage_clones': 26,
        'total_clones': 7
    },
    'csslint': {
        'total_errors': 1,
        'list_errors': ["./tests/fixtures/csslint.css: line 1, col 1, Warning - Don't use IDs in selectors."]
    },
    'jshint': {
        'total_errors': 1,
        'list_errors': ['tests/fixtures/jshint.js: line 1, col 11, Missing semicolon.']
    },
    'pyflakes': {
        'total_errors': 1,
        'list_errors': ["./tests/fixtures/pyflakes.py:1: 're' imported but unused"]
    }
}
```

Dependencies
------------

- Pep8 (http://pypi.python.org/pypi/pep8)
- PyFlakes (http://pypi.python.org/pypi/pyflakes)
- CloneDigger (http://pypi.python.org/pypi/clonedigger)
- JSHint (https://npmjs.org/package/jshint)
- CSSLint (https://npmjs.org/package/csslint)

Contributing
------------

To contribute, send a pull request or create an issue.

Speaking of quality, there's a test suite included. You can use it to check
if something is broke or to use as a starting point for your own tests.

To run the tests just clone, install and run the test suite.

```
git clone git://github.com/clybob/code_quality_tools.git
pip install -e .
make test
```

Author
------

**Romulo Tavares**

- https://github.com/clybob


Colaborators
------------

**Zacarias Eugenio**


License
-------

