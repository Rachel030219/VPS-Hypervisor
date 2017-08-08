import subprocess


def execute_one_line(command):
    if command != '':
        try:
            return subprocess.check_output(command, shell=True)
        except subprocess.CalledProcessError as e:
            return "Error: " + str(e.returncode)
    else:
        return "Error: Command is none"


def execute_sudo(command, passwd):
    if command != '':
        return execute_one_line("echo \"" + passwd + "\" | sudo -S " + command)
    else:
        return "Error: Command is none"


def split_command(message):
    commands = message.split(' ')
    args = ''
    for arg in commands:
        if commands.index(arg) > 0:
            args += arg + " "
    return args
