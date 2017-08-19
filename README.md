# VPS-Hypervisor
Manage your VPS effectively on Telegram

### How to use

#### 0. Install pyTelegramBotAPI

Go to [Getting started](https://github.com/eternnoir/pyTelegramBotAPI#getting-started)

#### 1. Configuration

Copy `config.example.py` to `config.py` , then edit it.

#### 2. RUN

```shell
python hypervisor.py
```

#### 3. That's all

> Notice: this bot works only when sudo is installed.

### Documents

#### /run <COMMAND>

Run an one-line command and get the output.

#### /set_pw <PASSWORD>

Set your password to run command as root user.

#### /su_run <COMMAND>

Run command as root user.