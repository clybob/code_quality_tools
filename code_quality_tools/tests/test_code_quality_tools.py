# encoding: utf-8

import unittest
import os

from os.path import isfile

from code_quality_tools import CodeQualityCheck


class TestCodeQualityTools(unittest.TestCase):
    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
    path_fixtures = os.path.join(ROOT_PATH, 'fixtures/')
    check = CodeQualityCheck()
    out_files = {
        'pep8': 'pep8_errors.txt',
        'pyflakes': 'pyflakes_errors.txt',
        'jshint': 'jshint_errors.txt',
        'csslint': 'csslint_errors.txt',
        'clonedigger': 'clonedigger_errors.txt'
    }

    def tearDown(self):
        for out_file in self.out_files.values():
            try:
                os.remove(out_file)
            except Exception:
                pass

    def test_get_pep8_errors(self):
        path_fixture = self.path_fixtures + 'pep8.py'
        errors = self.check.get_pep8_errors(path_fixture)
        self.assertEqual(errors['total_errors'], 3)
        self.assertEqual(len(errors['list_errors']), 3)

    def test_get_pep8_errors_with_extra_options(self):
        path_fixture = self.path_fixtures + 'pep8.py'
        errors = self.check.get_pep8_errors(
            path_fixture,
            options=['--ignore=E302']
        )
        self.assertEqual(errors['total_errors'], 1)
        self.assertEqual(len(errors['list_errors']), 1)

    def test_get_pep8_errors_saving_in_output_file(self):
        output_file = self.out_files['pep8']
        path_fixture = self.path_fixtures + 'pep8.py'
        self.check.get_pep8_errors(path_fixture, output_file)
        self.assertTrue(isfile(output_file))

    def test_get_pyflakes_errors(self):
        path_fixture = self.path_fixtures + 'pyflakes.py'
        errors = self.check.get_pyflakes_errors(path_fixture)
        self.assertEqual(errors['total_errors'], 2)
        self.assertEqual(len(errors['list_errors']), 2)

    def test_get_pyflakes_errors_saving_in_output_file(self):
        output_file = self.out_files['pyflakes']
        path_fixture = self.path_fixtures + 'pyflakes.py'
        self.check.get_pyflakes_errors(path_fixture, output_file)
        self.assertTrue(isfile(output_file))

    def test_get_jshint_errors(self):
        path_fixture = self.path_fixtures + 'jshint.js'
        errors = self.check.get_jshint_errors(path_fixture)
        self.assertEqual(errors['total_errors'], 2)
        self.assertEqual(len(errors['list_errors']), 2)

    def test_get_jshint_errors_saving_in_output_file(self):
        output_file = self.out_files['jshint']
        path_fixture = self.path_fixtures + 'jshint.js'
        self.check.get_jshint_errors(path_fixture, output_file)
        self.assertTrue(isfile(output_file))

    def test_get_jshint_errors_with_extra_options(self):
        path_fixture = self.path_fixtures
        errors = self.check.get_jshint_errors(
            path_fixture,
            options=['--extra-ext', '.jss']
        )
        self.assertEqual(errors['total_errors'], 4)
        self.assertEqual(len(errors['list_errors']), 4)

    def test_get_csslint_errors(self):
        path_fixture = self.path_fixtures + 'csslint.css'
        errors = self.check.get_csslint_errors(path_fixture)
        self.assertEqual(errors['total_errors'], 6)
        self.assertEqual(len(errors['list_errors']), 6)

    def test_get_csslint_errors_saving_in_output_file(self):
        output_file = self.out_files['csslint']
        path_fixture = self.path_fixtures + 'csslint.py'
        self.check.get_csslint_errors(path_fixture, output_file)
        self.assertTrue(isfile(output_file))

    def test_get_csslint_errors_with_extra_options(self):
        path_fixture = self.path_fixtures + 'csslint.css'
        errors = self.check.get_csslint_errors(
            path_fixture,
            options=['--errors=ids']
        )
        self.assertEqual(errors['total_errors'], 1)
        self.assertEqual(len(errors['list_errors']), 1)

    def test_get_clonedigger_errors(self):
        path_fixture = self.path_fixtures + 'clonedigger.py'
        errors = self.check.get_clonedigger_errors(path_fixture)
        self.assertEqual(errors['total_errors'], 1)
        self.assertEqual(errors['percentage_errors'], 100)
        self.assertTrue(errors['list_errors'])
        self.assertFalse(isfile('output_clonedigger.html'))

    def test_get_clonedigger_errors_saving_in_output_file(self):
        output_file = self.out_files['clonedigger']
        path_fixture = self.path_fixtures + 'clonedigger.py'
        self.check.get_clonedigger_errors(path_fixture, output_file)
        self.assertTrue(isfile(output_file))

    def test_get_all_errors(self):
        errors = self.check.get_all_errors(self.path_fixtures)

        tasks = ['pep8', 'pyflakes', 'jshint', 'csslint', 'clonedigger']
        for task in tasks:
            self.assertTrue('total_errors' in errors[task].keys())
            self.assertTrue('list_errors' in errors[task].keys())
            self.assertTrue('percentage_errors' in errors[task].keys())

if __name__ == '__main__':
    unittest.main()
