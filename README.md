This is a template for a simple Grinder project.


# Libraries

Grinder itself is not included in this project.  Download it from:
http://grinder.sourceforge.net/download.html

Create a 'lib' directory and place into it the following .jar files:
* grinder.jar
* jython.jar
* grinder-xmlbeans.jar
* xbean.jar
* picocontainer-2.13.6.jar


# Scripts

There are a set of shell scripts in the bin directory.  For these scripts to work with grinder "as-is" (no further configuration) they need to be executed from the directory containing the tests.  This is a restriction by the way the default embedded jython is configured.

For example, to run the agent using the grinder.properties from the test directory:
    cd test
    ../bin/runAgent.sh
    
If it is not executed in this way then jython cannot find the .py scripts referenced aside from the one in grinder.properties itself.