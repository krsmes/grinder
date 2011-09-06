#!/bin/sh

SCRIPT_DIR=`dirname $0`

TEST_DIR=.

LIB_DIR=${SCRIPT_DIR}/../lib

CLASSPATH=`echo *.jar ${LIB_DIR}/*.jar | sed 's/ /:/g'`:${TEST_DIR}

GRINDERPROPERTIES=${TEST_DIR}/grinder.properties
