import subprocess
import config


def execute_one_line(command):
    if command is not None:
        if config.start_by_root and config.normal_user != "":
            command = "su " + config.normal_user + " -c " + command
        if "exit" in command:
            return "Error: Unfortunately I do not accept exit"
        command += "; exit 0"
        return subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True).decode('utf-8')
    else:
        return "Error: Command is null"


def execute_sudo(command, passwd):
    if command is not None:
        return execute_one_line("echo \"" + passwd + "\" | sudo -S " + command)
    else:
        return "Error: Command is null"


def split_command(message):
    commands = message.split(' ')
    args = ""
    for arg in commands:
        if commands.index(arg) > 0:
            args += arg + " "
    return args
