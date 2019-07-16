#!/bin/bash -e

PID=$(cat /var/run/nodejs/nodejs.pid)
ctx logger info "Sending signal to process ${PID}"
kill -9 ${PID}
rm -rf /var/run/nodejs/nodejs.pid
