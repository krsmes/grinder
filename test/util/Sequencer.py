# Run many scripts in sequence.
#
# Scripts are defined in Python modules (helloworld.py, goodbye.py)
# specified in grinder.properties:
#
#   script.01=helloworld
#   script.02=goodbye

from net.grinder.script.Grinder import grinder

from java.util import TreeMap

import Simple

# TreeMap is the simplest way to sort a Java map.
scripts = TreeMap(grinder.properties.getPropertySubset("script."))

# Ensure modules are initialised in the process thread.
for module in scripts.values(): print("import %s" % module)
for module in scripts.values(): exec("import %s" % module)

def createTestRunner(module):
    exec("x = %s.TestRunner()" % module)
    return x


class TestRunner:
    def __init__(self):
        self.testRunners = [createTestRunner(m) for m in scripts.values()]
    
    def __call__(self):
        for testRunner in self.testRunners: testRunner()
