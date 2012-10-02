import subprocess
import re


class CodeQualityCheck():

    def __execute(self, tool, path, output_file, options):
        command = [tool, path]
        command.extend(options)
        output = self.__execute_shell_command(command, output_file)
        return output

    def __execute_shell_command(self, command, stdout=None):
        if stdout is None:
            lines = self.__get_errors(command, stdout)
        else:
            lines = self.__save_output_file_and_get_errors(command, stdout)

        count_errors = len(lines)
        errors = {'total_errors': count_errors, 'list_errors': lines}

        return errors

    def __get_errors(self, command, stdout):
        stdout = subprocess.PIPE
        result = subprocess.Popen(command, stdout=stdout)
        output, error = result.communicate()
        output_lines = output.splitlines()

        lines = [line for line in output_lines if self.__validate_line(line)]
        return lines

    def __validate_line(self, line):
        return line and ' errors' not in line

    def __save_output_file_and_get_errors(self, command, stdout):
        output_file = open(stdout, 'w')
        result = subprocess.Popen(command, stdout=output_file)
        output, error = result.communicate()
        output_file.close()

        output_file = open(stdout, 'r')
        lines = output_file.read().splitlines()
        output_file.close()
        return lines

    def get_pep8_errors(self, path='.', output_file=None, options=[]):
        return self.__execute('pep8', path, output_file, options)

    def get_pyflakes_errors(self, path='.', output_file=None, options=[]):
        return self.__execute('pyflakes', path, output_file, options)

    def get_jshint_errors(self, path='.', output_file=None, options=[]):
        return self.__execute('jshint', path, output_file, options)

    def get_csslint_errors(self, path='.', output_file=None, options=[]):
        options.extend(['--format=compact'])
        return self.__execute('csslint', path, output_file, options)

    def get_clonedigger_errors(self, path='.', output_file='output_clonedigger.html', options=[]):
        options.extend(['--output=%s' % output_file])
        self.__execute('clonedigger', path, None, options)

        output_clonedigger = open(output_file)
        result_clonedigger = output_clonedigger.read()
        output_clonedigger.close()

        regex_percentage = '(?<=duplicates \()\d+'
        regex_total = '(?<=Clones detected: )\d+'

        porcentage = re.search(regex_percentage, result_clonedigger)
        porcentage = int(porcentage.group())

        total_clones = re.search(regex_total, result_clonedigger)
        total_clones = int(total_clones.group())

        result = {
            'total_clones': total_clones,
            'percentage_clones': porcentage
        }
        return result

    def get_all_errors(self, path='.'):
        errors = {
            'pep8': self.get_pep8_errors(path),
            'pyflakes': self.get_pyflakes_errors(path),
            'jshint': self.get_jshint_errors(path),
            'csslint': self.get_csslint_errors(path),
            'clonedigger': self.get_clonedigger_errors(path)
        }
        return errors
