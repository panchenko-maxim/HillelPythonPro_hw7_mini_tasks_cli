# Get user id for macOS and Linux

user_id := if shell("uname") == "Darwin" { shell("id -u") } else { shell("id --user") }

# Get path to root of the project directory

project_workdir := shell("pwd")