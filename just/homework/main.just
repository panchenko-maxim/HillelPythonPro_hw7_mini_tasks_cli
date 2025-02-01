import "vars.just"
import "configs.just"
import "docker.just"

# Make all actions needed for run homework from zero.
homework-i-docker-i-run: init-i-configs d-up

# Make all actions needed for purge homework related data.
homework-i-docker-i-purge: d-purge