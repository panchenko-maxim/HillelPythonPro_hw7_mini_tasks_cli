import "vars.just"

# Up services with build
d-up:
    @export user_id={{ user_id }} &&\
    export project_workdir={{ project_workdir }} &&\
    COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
    	docker compose \
    	  up \
          --build

## Up services with build and watch changes
#d-up-i-watch:
#    @export user_id={{ user_id }} &&\
#    COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
#    	docker compose \
#    	  up \
#          --build \
#          --watch

# Run app. For interact with app in "interactive" mode with "tty" enabled.
d-run-i-app:
    @export user_id={{ user_id }} &&\
    export project_workdir={{ project_workdir }} &&\
    COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
    	docker compose \
            run \
            --rm --build \
            app

# Build services
d-build:
    @export user_id={{ user_id }} &&\
    export project_workdir={{ project_workdir }} &&\
    COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
    	docker compose \
    		build

# Purge all data related with services
d-purge:
    @export user_id={{ user_id }} &&\
    export project_workdir={{ project_workdir }} &&\
    COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
    	docker compose \
    	    down \
    	    --volumes --remove-orphans --rmi local --timeout 0

# Get information about current compose configuration
d-compose-inspect:
    @export user_id={{ user_id }} &&\
    export project_workdir={{ project_workdir }} &&\
    COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
    	docker compose config