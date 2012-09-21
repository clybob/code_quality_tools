import subprocess
import re


def execute(tool, path, output_file, options):
    command = [tool, path]
    command.extend(options)
    output = execute_shell_command(command, output_file)
    return output


def execute_shell_command(command, stdout=None):
    if stdout is None:
        lines = get_errors(command, stdout)
    else:
        lines = save_output_file_and_get_errors(command, stdout)

    count_errors = len(lines)
    errors = {'total_errors': count_errors, 'list_errors': lines}

    return errors


def get_errors(command, stdout):
    stdout = subprocess.PIPE
    result = subprocess.Popen(command, stdout=stdout)
    output, error = result.communicate()
    lines = output.splitlines()
    return lines


def save_output_file_and_get_errors(command, stdout):
    output_file = open(stdout, 'w')
    result = subprocess.Popen(command, stdout=output_file)
    output, error = result.communicate()
    output_file.close()

    output_file = open(stdout, 'r')
    lines = output_file.read().splitlines()
    output_file.close()
    return lines


def get_pep8_errors(path='.', output_file=None, options=[]):
    return execute('pep8', path, output_file, options)


def get_pyflakes_errors(path='.', output_file=None, options=[]):
    return execute('pyflakes', path, output_file, options)


def get_jshint_errors(path='.', output_file=None, options=[]):
    return execute('jshint', path, output_file, options)


def get_jslint_errors(path='.', output_file=None, options=[]):
    return execute('jslint', path, output_file, options)


def get_csslint_errors(path='.', output_file=None, options=[]):
    options.extend(['--format=compact'])
    return execute('csslint', path, output_file, options)


def get_clonedigger_errors(path='.', output_file='output_clonedigger.html',
    options=[]):
    options.extend(['--output=%s' % output_file])
    execute('clonedigger', path, None, options)

    output_clonedigger = open(output_file)
    result_clonedigger = output_clonedigger.read()
    output_clonedigger.close()

    porcentage = re.search('(?<=duplicates \()\d+', result_clonedigger)
    porcentage = porcentage.group()

    total_clones = re.search('(?<=Clones detected: )\d+', result_clonedigger)
    total_clones = total_clones.group()

    result = {'total_clones': total_clones, 'percentage_clones': porcentage}
    return result
