#!/bin/bash -e

tempdir=$(mktemp -d)
ctx download-resource-and-render ${resource_path} ${tempdir}/index.html
lftp -e "put -a ${tempdir}/index.html" -u ${username},${password} ${endpoint}
rm -rf ${tempdir}
