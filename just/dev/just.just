# Install Just
# https://just.systems/man/en/pre-built-binaries.html
# TODO: Make install with update.
# Can be installed with:
# - cargo install just
# - uv tool install just
# - curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash
# - etc.
#
# Install via cargo used, because it's more simple and easy to update. Also, it's better installed.
#
# ---
#
# Useful plugins for Justfile:
# - [JetBrains IDE Plugin](https://plugins.jetbrains.com/plugin/18658-just)
# - [Other](https://just.systems/man/en/editor-support.html)
#
# ---

# Install Just
just-i-install:
    #!/usr/bin/env bash
    set -euo pipefail
    if ! command -v just &> /dev/null; then
        cargo install just
    else
        cargo install-update just
    fi

    just --version

# Install "Just" completions for bash. If needed.
# https://github.com/casey/just?tab=readme-ov-file#shell-completion-scripts

# Install "Just" completions for bash. If needed.
@just-i-install-i-completions-i-bash:
    used_shell='bash' && \
    \
    command='eval "$(just --completions '"${used_shell}"')"' && \
    file="${HOME}/.${used_shell}rc" && \
    \
    grep --quiet --line-regexp --fixed-strings "${command}" "${file}" || \
    echo "${command}" >> "${file}"

# Make all for "Just"
@just-i-install-i-all: just-i-install just-i-install-i-completions-i-bash