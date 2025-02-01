import 'dev/rust.just'
import 'dev/just.just'
import 'dev/python_uv.just'
import 'dev/python_manage.just'
import 'dev/python_tools.just'
import 'dev/pre_commit.just'

# Init dev environment
@init-i-dev: && uv-i-install-i-all python-i-venv-i-install pre-commit-i-install-i-tool pre-commit-i-install-i-hooks
    echo "Init dev environment"