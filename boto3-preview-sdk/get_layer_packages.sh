export PKG_DIR="python"

rm -rf ${PKG_DIR} && mkdir -p ${PKG_DIR}


docker run --rm -v $(pwd):/foo -w /foo lambci/lambda:build-python3.8 \
    python3 -m pip install ./botocore-1.27.4-py3-none-any.whl -t ${PKG_DIR}


docker run --rm -v $(pwd):/foo -w /foo lambci/lambda:build-python3.8 \
    python3 -m pip install ./boto3-1.24.4-py3-none-any.whl -t ${PKG_DIR}
