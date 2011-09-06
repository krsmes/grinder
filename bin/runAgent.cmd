@echo off

SCRIPT_DIR=%~dp0
call %SCRIPT_DIR%\setGrinderEnv.cmd

java -cp %CLASSPATH% -Dgrinder.runs=1 -Dgrinder.useConsole=false net.grinder.Grinder %GRINDERPROPERTIES%
