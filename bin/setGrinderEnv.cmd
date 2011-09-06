@echo off
setlocal ENABLEDELAYEDEXPANSION

set SCRIPT_DIR=%~dp0

set TEST_DIR=.

set LIB_DIR=${SCRIPT_DIR}\..\lib

if defined CLASSPATH (set CLASSPATH=%CLASSPATH%;.) else (set CLASSPATH=%TEST_DIR%)
for /R %LIB_DIR% %%G in (*.jar) do set CLASSPATH=!CLASSPATH!;%%G

GRINDERPROPERTIES=%TEST_DIR%\grinder.properties
