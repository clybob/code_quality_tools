import subprocess
import re
import os


class CodeQualityCheck():
    """This class is responsible to get metrics of code quality,
    using known python tools. The objective is to easily get
    data of code quality"""

    def __execute(self, tool, path, output_file, options, extension):
        """Prepares to execute a shell command"""

        number_of_lines = self.get_lines_per_language(path, extension)

        command = [tool, path]
        command.extend(options)
        output = self.__execute_shell_command(
            command, output_file, number_of_lines
        )
        return output

    def __execute_shell_command(self, command, stdout=None, lines_per_lang=0):
        """Executes a shell command and saves output in a file
        if stdout was passed"""

        if stdout is None:
            lines = self.__get_errors(command, stdout)
        else:
            lines = self.__save_output_file_and_get_errors(command, stdout)

        count_errors = len(lines)
        percentage_errors = float(count_errors) / float(lines_per_lang)
        percentage_errors = percentage_errors * 100
        percentage_errors = round(percentage_errors, 2)

        errors = {
            'total_errors': count_errors,
            'list_errors': lines,
            'percentage_errors': percentage_errors
        }

        return errors

    def __get_errors(self, command, stdout):
        """Executes a shell command and captures output"""

        stdout = subprocess.PIPE
        result = subprocess.Popen(command, stdout=stdout)
        output, error = result.communicate()
        output_lines = output.splitlines()

        lines = [line for line in output_lines if self.__validate_line(line)]
        return lines

    def __validate_line(self, line):
        """Removes blank lines and lines with total errors jshint"""

        return line and ' errors' not in line

    def __save_output_file_and_get_errors(self, command, stdout):
        """Executes a shell command, saves output in output_file and
        returns output to caller function"""

        output_file = open(stdout, 'w')
        result = subprocess.Popen(command, stdout=output_file)
        output, error = result.communicate()
        output_file.close()

        output_file = open(stdout, 'r')
        lines = output_file.read().splitlines()
        output_file.close()
        return lines

    def get_lines_per_language(self, path='.', language_extension='py'):
        """Gets total of lines per language extension"""

        LAST_LINE = 1
        command = 'find %s -name "*.%s" -exec cat {} \; | wc -l;' % (
            path, language_extension
        )
        number_of_lines = int(subprocess.check_output(command, shell=True))
        return number_of_lines + LAST_LINE

    def get_pep8_errors(self, path='.', output_file=None, options=[]):
        return self.__execute('pep8', path, output_file, options, 'py')

    def get_pyflakes_errors(self, path='.', output_file=None, options=[]):
        return self.__execute('pyflakes', path, output_file, options, 'py')

    def get_jshint_errors(self, path='.', output_file=None, options=[]):
        return self.__execute('jshint', path, output_file, options, 'js')

    def get_csslint_errors(self, path='.', output_file=None, options=[]):
        options.extend(['--format=compact'])
        return self.__execute('csslint', path, output_file, options, 'css')

    def get_clonedigger_errors(self, path='.', output_file=None, options=[]):
        """Clonedigger generates a output_file by default, this method read
        output file and returns a total of clones and percentage of clones"""

        if output_file is None:
            default_output_file = 'output_clonedigger.html'
        else:
            default_output_file = output_file

        options.extend(['--output=%s' % default_output_file])
        self.__execute('clonedigger', path, None, options, 'py')

        output_clonedigger = open(default_output_file)
        result_clonedigger = output_clonedigger.read()
        output_clonedigger.close()

        if output_file is None:
            os.remove(default_output_file)

        regex_percentage = '(?<=duplicates \()\d+'
        regex_total = '(?<=Clones detected: )\d+'

        percentage = re.search(regex_percentage, result_clonedigger)
        percentage = int(percentage.group())

        total_errors = re.search(regex_total, result_clonedigger)
        total_errors = int(total_errors.group())

        result = {
            'total_errors': total_errors,
            'percentage_errors': percentage,
            'list_errors': result_clonedigger
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
