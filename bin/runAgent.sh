#!/bin/sh

SCRIPT_DIR=`dirname $0`
. ${SCRIPT_DIR}/setGrinderEnv.sh

java -cp ${CLASSPATH} -Dgrinder.runs=1 -Dgrinder.useConsole=false net.grinder.Grinder ${GRINDERPROPERTIES}
