#!/bin/bash

readonly TMP_DIR=$(mktemp -d -t update_py_requirements_XXXXXX)
python3 -m venv ${TMP_DIR}
cp "${BUILD_WORKSPACE_DIRECTORY}/requirements.txt" "${TMP_DIR}/requirements.txt"
pushd ${TMP_DIR}
source ./bin/activate

pip3 install -r requirements.txt --require-virtualenv
pip3 freeze -r requirements.txt --require-virtualenv > ${BUILD_WORKSPACE_DIRECTORY}/requirements_lock.txt

source ./bin/deactivate
popd
rm -rf ${TMP_DIR}