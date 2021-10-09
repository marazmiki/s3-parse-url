#!/bin/bash

PORT=5300
DIR="$(realpath .)"

if [ ! -d "${DIR}/source" ]; then
  DIR="${DIR}/docs"
fi

# Please, do not add sphinx and sphinx-reload to the project
# with poetry add!
poetry run pip install sphinx sphinx-reload
poetry run sphinx-reload -p "${PORT}" "${DIR}"
