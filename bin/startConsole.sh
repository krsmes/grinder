#!/bin/sh

SCRIPT_DIR=`dirname $0`
. ${SCRIPT_DIR}/setGrinderEnv.sh
CLASSPATH=${CLASSPATH}:${LIB_EXTRA}/picocontainer-2.13.6.jar

java -cp ${CLASSPATH} net.grinder.Console
