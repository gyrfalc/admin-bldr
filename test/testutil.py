'''
Created on Dec 22, 2013

@author: Merle
'''
import unittest
import doers.util

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testCamelCase(self):
        print "testing camel case..."
        rslt = doers.util.toCamelCase("table_name")
        print "result = " + rslt
        self.assertEqual(rslt, "tableName")
        
    def testLeadingCamelCase(self):
        self.assertEquals("LeadingCamelCase", doers.util.toLeadingCamelCase("leaDing_caMel_cAse"), "Failed to create leading camel case")
        
 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()