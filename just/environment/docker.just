# Install Docker Engine and related on Ubuntu:
# https://docs.docker.com/engine/install/ubuntu/
# https://docs.docker.com/engine/install/linux-postinstall/
#
# Other options:
# https://docs.docker.com/get-docker/

# Install Docker Engine and related tools.
docker-i-install:
    #!/usr/bin/env bash

    # [bash_init]-[BEGIN]
    # Exit whenever it encounters an error, also known as a non–zero exit code.
    set -o errexit
    # Return value of a pipeline is the value of the last (rightmost) command to exit with a non-zero status,
    #   or zero if all commands in the pipeline exit successfully.
    set -o pipefail
    # Treat unset variables and parameters other than the special parameters ‘@’ or ‘*’ as an error when performing parameter expansion.
    set -o nounset
    # Print a trace of commands.
    set -o xtrace
    # [bash_init]-[END]

    sudo --validate && \
    sudo apt-get update && \
    sudo apt-get install --yes ca-certificates curl gnupg  && \
    sudo install --mode 0755 --directory /etc/apt/keyrings  && \
    curl --fail --silent --show-error --location https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor --output /etc/apt/keyrings/docker.gpg && \
    sudo chmod a+r /etc/apt/keyrings/docker.gpg && \
    echo \
     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
     sudo tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    sudo apt-get update && \
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin && \
    sudo docker run --rm hello-world && \
    sudo usermod --append --groups docker "${USER}" && \
    newgrp docker; \
    docker --version && \
    docker run --rm hello-world && \
    docker --version && \
    docker buildx version && \
    docker compose version && \
    echo "Done!" && \
    echo "Reboot shell. Better reboot entire system."