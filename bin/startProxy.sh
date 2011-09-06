#!/bin/sh

SCRIPT_DIR=`dirname $0`
. ${SCRIPT_DIR}/setGrinderEnv.sh
CLASSPATH=${CLASSPATH}:${LIB_DIR}/picocontainer-2.13.6.jar:${LIB_DIR}/grinder-xmlbeans.jar:${LIB_DIR}/xbean.jar

java -cp ${CLASSPATH} net.grinder.TCPProxy -console -http > grinder.py
