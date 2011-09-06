@echo off

SCRIPT_DIR=%~dp0
call %SCRIPT_DIR%\setGrinderEnv.cmd

java -cp %CLASSPATH% net.grinder.TCPProxy -console -http > grinder.py
