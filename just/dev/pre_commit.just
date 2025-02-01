# Use "uv" tool for better Python environments.
#
# ---
#
# Install pre-commit tool
# https://pre-commit.com/#install
#
# TODO: ? Move to prefligit, when it will support more environments (Node, etc)
# https://github.com/j178/prefligit

# Install pre-commit tool
@pre-commit-i-install-i-tool:
    uv tool install pre-commit --upgrade &&\
    pre-commit --version

# Install pre-commit hooks.
# https://pre-commit.com/#usage
# Don't needed to re-run this command after changes in .pre-commit-config.yaml
# !Important: Run this after each clone of the repository

# Install pre-commit hooks.
@pre-commit-i-install-i-hooks:
    @pre-commit install

## Update "rev" version of all pre-commit hooks.
## https://pre-commit.com/#updating-hooks-automatically
##
## Maybe, it is better to use "https://gitlab.com/vojko.pribudic.foss/pre-commit-update".
## It is has better update process. And it not update to unstable versions.
#
## Update "rev" version of all pre-commit hooks.
#@pre-commit-i-update-i-hooks:
#    @pre-commit autoupdate

# Run tools for files from commit.
pre-commit-i-run:
    @pre-commit run

# Run tools for all files.
@pre-commit-i-run-i-all:
    @pre-commit run --all-files

# Pre-commit run for folder:
# https://pre-commit.com/#pre-commit-run:~:text=git%20ls%2Dfiles%20%2D%2D%20%27*.py%27%20%7C%20xargs%20pre%2Dcommit%20run%20%2D%2Dfiles
# git ls-files -- your/folder | xargs pre-commit run --files