# Install Rust
# https://www.rust-lang.org/tools/install

# Install Rust
rust-i-install:
    #!/usr/bin/env bash
    set -euo pipefail
    if ! command -v rustup &> /dev/null; then
        curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y;
    else
        rustup update;
    fi

    rustup --version
    rustc --version

# Install updater for installed rust executables
# https://crates.io/crates/cargo-update

# Install updater for installed rust executables
@rust-i-install-i-upgrade:
    cargo install cargo-update &&\
    cargo install-update cargo-update &&\
    cargo install-update --version

# Make all for "Rust"
@rust-i-install-i-all: rust-i-install rust-i-install-i-upgrade