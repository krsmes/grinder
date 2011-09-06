#!/bin/sh

SCRIPT_DIR=`dirname $0`
. ${SCRIPT_DIR}/setGrinderEnv.sh

java -cp ${CLASSPATH} net.grinder.Grinder ${GRINDERPROPERTIES}
