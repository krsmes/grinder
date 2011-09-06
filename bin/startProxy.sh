#!/bin/sh

SCRIPT_DIR=`dirname $0`
. ${SCRIPT_DIR}/setGrinderEnv.sh
CLASSPATH=${CLASSPATH}:${LIB_EXTRA}/picocontainer-2.13.6.jar:${LIB_EXTRA}/grinder-xmlbeans.jar:${LIB_EXTRA}/xbean.jar

java -cp ${CLASSPATH} net.grinder.TCPProxy -console -http > grinder.py
