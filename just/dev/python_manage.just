# Manage Python environment for the project.

# Create virtual environment and install dependencies.
@python-i-venv-i-install:
    uv sync --frozen

# Update dependencies.
@python-i-venv-i-deps-upgrade:
    uv sync --upgrade