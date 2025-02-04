# CLI. Mini-tasks. File, Generate, Request, CSV

---

## 🏠 Homework

Homework related actions.

---
### ▶️ Run

Make all actions needed for run homework from zero. Including configuration.

```shell
just homework-i-docker-i-run
```

### 🚮 Purge

Make all actions needed for run homework from zero.

```shell
just homework-i-docker-i-purge
```

---
### ▶️ Run in "interactive"

 Run app. For interact with app in "interactive" mode with "tty" enabled.

```shell
just d-run-i-app 
```

For exit from container

```shell
exit
```

---
### 1) Run "Reading a file" task with cli

Create a file in "files_input" directory and enter the command

```shell
python main.py reading_a_file run --file "<filename>"
```

or if you create file with name "file.txt"

```shell
python main.py reading_a_file run
```

---
### 2) Run "User generator" task with cli

For get in terminal random 10 "name email" 

```shell
python main.py reading_a_file user_generator run
```

To get a specific number "name email" in the terminal

```shell
python main.py user_generator run --amount 5
```

To save in the folder "files_output" use the command (allowed format: txt, csv, json)

```shell
python main.py user_generator run --amount 10 --format-file "txt"
```
```shell
python main.py user_generator run --amount 9 --format-file "csv"
```
```shell
python main.py user_generator run --amount 15 --format-file "json"
```

---
### 3) Run "Reading a file" task with cli

---
### 🚮 Purge

Make all actions needed for purge homework related data.

```shell
just homework-i-docker-i-purge
```

---

## 🛠️ Development

### Install just

You must have [just] installed on your system for run different commands.

If you don't have [just] installed, you can find commands for installation here:

- [just.just](just/dev/just.just)

After installing [just], you can see all available commands with:

```bash
just --list
```

[just]: https://github.com/casey/just

### Initialize dev

Install dependencies and register pre-commit.

```shell
just init-i-dev
```

### ⚙️ Configure

Configure homework.

```shell
just init-i-configs
```

---

## 🐳 Docker

Use services in dockers.

### ▶️ Run

Just up/run services

```shell
just d-up
```

### 🚮 Purge

Purge all data related to services

```shell
just d-purge
```