#!/bin/sh

SCRIPT_DIR=`dirname $0`

TEST_DIR=.

LIB_DIR=${SCRIPT_DIR}/../lib
LIB_EXTRA=${LIB_DIR}/extra

CLASSPATH=${LIB_DIR}/grinder.jar
GRINDERPROPERTIES=${TEST_DIR}/grinder.properties
