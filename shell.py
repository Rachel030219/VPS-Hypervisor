import subprocess


def execute_one_line(command):
    commands = command.split(' ')
    args = ''
    for arg in commands:
        if commands.index(arg) > 0:
            args += " " + arg
    if args != '':
        try:
            return subprocess.check_output(args, shell=True)
        except subprocess.CalledProcessError as e:
            return "Error " + str(e.returncode)
    else:
        return "Error: Command is none"
