#!/bin/bash
# Wrapper for manus.js
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
node "$DIR/manus.cjs" "$@"
