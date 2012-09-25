# encoding: utf-8

import unittest
import sys
from os.path import join, abspath, dirname
sys.path.insert(0, abspath(join(dirname(''))))
import code_quality_tools


class TestCodeQualityTools(unittest.TestCase):
    path_fixtures = 'tests/fixtures/'

    def test_get_pep8_errors(self):
        path_fixture = self.path_fixtures + 'pep8.py'
        errors = code_quality_tools.get_pep8_errors(path_fixture)
        self.assertEqual(errors['total_errors'], 3)
        self.assertEqual(len(errors['list_errors']), 3)

    def test_get_pyflakes_errors(self):
        path_fixture = self.path_fixtures + 'pyflakes.py'
        errors = code_quality_tools.get_pyflakes_errors(path_fixture)
        self.assertEqual(errors['total_errors'], 2)
        self.assertEqual(len(errors['list_errors']), 2)

    def test_get_jshint_errors(self):
        path_fixture = self.path_fixtures + 'jshint.js'
        errors = code_quality_tools.get_jshint_errors(path_fixture)
        self.assertEqual(errors['total_errors'], 2)
        self.assertEqual(len(errors['list_errors']), 2)

    def test_get_jslint_errors(self):
        path_fixture = self.path_fixtures + 'jslint.js'
        errors = code_quality_tools.get_jslint_errors(path_fixture)
        import pdb; pdb.set_trace()
        self.assertEqual(errors['total_errors'], 5)
        self.assertEqual(len(errors['list_errors']), 5)

    def test_get_csslint_errors(self):
        path_fixture = self.path_fixtures + 'csslint.css'
        errors = code_quality_tools.get_csslint_errors(path_fixture)
        self.assertEqual(errors['total_errors'], 6)
        self.assertEqual(len(errors['list_errors']), 6)

    def test_get_clonedigger_errors(self):
        path_fixture = self.path_fixtures + 'clonedigger.py'
        errors = code_quality_tools.get_clonedigger_errors(path_fixture)
        self.assertEqual(errors['total_clones'], 1)
        self.assertEqual(errors['percentage_clones'], 100)


if __name__ == '__main__':
    unittest.main()
