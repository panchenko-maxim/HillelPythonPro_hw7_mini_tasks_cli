# For see all this list of commands run:
# ```bash
# just --list
# ```
# All docs is only "one-liner".
#
# Plugin: https://plugins.jetbrains.com/plugin/18658-just
#

import 'just/dev.just'
import 'just/homework.just'
import 'just/environment.just'
import 'just/other.just'

# List of all commands
[private]
@list:
    just --list --justfile {{ justfile() }}