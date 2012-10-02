# encoding: utf-8

import unittest
import sys
from os.path import join, abspath, dirname
sys.path.insert(0, abspath(join(dirname(''))))
from code_quality_tools import CodeQualityCheck


class TestCodeQualityTools(unittest.TestCase):
    path_fixtures = 'tests/fixtures/'
    check = CodeQualityCheck()

    def test_get_pep8_errors(self):
        path_fixture = self.path_fixtures + 'pep8.py'
        errors = self.check.get_pep8_errors(path_fixture)
        self.assertEqual(errors['total_errors'], 3)
        self.assertEqual(len(errors['list_errors']), 3)

    def test_get_pyflakes_errors(self):
        path_fixture = self.path_fixtures + 'pyflakes.py'
        errors = self.check.get_pyflakes_errors(path_fixture)
        self.assertEqual(errors['total_errors'], 2)
        self.assertEqual(len(errors['list_errors']), 2)

    def test_get_jshint_errors(self):
        path_fixture = self.path_fixtures + 'jshint.js'
        errors = self.check.get_jshint_errors(path_fixture)
        self.assertEqual(errors['total_errors'], 2)
        self.assertEqual(len(errors['list_errors']), 2)

    def test_get_csslint_errors(self):
        path_fixture = self.path_fixtures + 'csslint.css'
        errors = self.check.get_csslint_errors(path_fixture)
        self.assertEqual(errors['total_errors'], 6)
        self.assertEqual(len(errors['list_errors']), 6)

    def test_get_clonedigger_errors(self):
        path_fixture = self.path_fixtures + 'clonedigger.py'
        errors = self.check.get_clonedigger_errors(path_fixture)
        self.assertEqual(errors['total_clones'], 1)
        self.assertEqual(errors['percentage_clones'], 100)

    def test_get_all_errors(self):
        errors = self.check.get_all_errors(self.path_fixtures)
        self.assertEqual(len(errors['pep8']), 2)
        self.assertEqual(len(errors['pyflakes']), 2)
        self.assertEqual(len(errors['jshint']), 2)
        self.assertEqual(len(errors['csslint']), 2)
        self.assertEqual(len(errors['clonedigger']), 2)

if __name__ == '__main__':
    unittest.main()
