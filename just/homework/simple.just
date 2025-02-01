import "vars.just"

# Show user id
@echo-i-user-id:
    echo {{ user_id }}

# Show project workdir
@echo-i-project-workdir:
    echo {{ project_workdir }}

# Run homework without docker. Example.
homework-i-run:
    @python cli.py

# Cleanup after homework without docker. Example.
homework-i-purge:
    @echo Goodbye