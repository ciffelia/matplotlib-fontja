#!/usr/bin/env bash

set -euxo pipefail

cd -P -- "$(dirname -- "${BASH_SOURCE[0]}")"

python_version=(3.7 3.8 3.9 3.10 3.11 3.12)
matplotlib_version=(3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8)

test_script="create_snapshot.py"
snapshot_dir="snapshot"

rm -rf "$snapshot_dir"
mkdir -p "$snapshot_dir"

for py in "${python_version[@]}"
do
  rye pin "$py" --no-update-requires-python
  for mpl in "${matplotlib_version[@]}"
  do
    rm -f requirements.lock requirements-dev.lock
    if rye add "matplotlib~=$mpl"; then
      rye sync
      python "$test_script" "$snapshot_dir/py${py}_mpl${mpl}.png"
    fi
  done
done
