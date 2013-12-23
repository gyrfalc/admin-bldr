'''
Created on Dec 22, 2013

@author: Merle
'''
import unittest
import model.schema
import model.table
import model.column
import doers.modeler
import model.config


class Test(unittest.TestCase):


    def testSchema(self):
        s = model.schema.Schema()
        t1 = model.table.Table()
        t2 = model.table.Table()
        ts = {t1, t2}
        s.setTables(ts)
        self.assertEquals(2, len(s.getTables()), "Table length does not match")
        
    def testTableNames(self):
        t = model.table.Table()
        t.setName("fabric_family_test")
        self.assertEquals("FabricFamilyTest", t.getClassName(), "Incorrect class name for table: " + t.getClassName())
        self.assertEquals("FabricFamilyTest.java", t.getClassFileName(), "Incorrect class file name for table: " + t.getClassFileName())
        
        
    def testTableModel(self):
        params = {"pkg_model": "com.csc.admin.model", "path_model":"../playground"}
        c = model.config.Config(params)       
        t1 = model.table.Table()
        t1.setName("fabric_family")
        c1 = model.column.Column()
        c1.setName("fabric_family_cd")
        c1.setType("string")
        c2 = model.column.Column()
        c2.setName("fabric_family_nm")
        c2.setType("string")
        columns = {c1, c2}
        t1.setColumns(columns)
        self.assertTrue(doers.modeler.buildTableModel(t1, c), "Failed to build table model")
        
    def testSchemaModel(self):
        params = {"pkg_model": "com.csc.admin.model", "path_model":"../playground"}
        c = model.config.Config(params)       
        t1 = model.table.Table()
        t1.setName("fabric_family")
        c1 = model.column.Column()
        c1.setName("fabric_family_cd")
        c1.setType("string")
        c2 = model.column.Column()
        c2.setName("fabric_family_nm")
        c2.setType("string")
        columns = {c1, c2}
        t1.setColumns(columns)  
        
        t2 = model.table.Table()
        t2.setName("fabric_family_fabric")
        c3 = model.column.Column()
        c3.setName("fabric_family_cd")
        c3.setType("string")
        c4 = model.column.Column()
        c4.setName("fabric_cd")
        c4.setType("string")
        c5 = model.column.Column()
        c5.setName("insr_dt")
        c5.setType("date")
        columns2 = {c3, c4, c5}
        t2.setColumns(columns2)
        
        s = model.schema.Schema()
        s.setTables({t1, t2})
        
        self.assertTrue(doers.modeler.buildSchemaSchemaModel(s, c), "Failed to build schema model")         
        
    def testColumn(self):
        c = model.column.Column()
        c.setName("fabric_nm")
        c.setType("string")
        self.assertEquals("fabric_nm", c.getName(), "column name does not match")
        print c.getMethodName()
        self.assertEquals("FabricNm", c.getMethodName(), "method name does not match")
        self.assertEquals("fabricNm", c.getPropertyName(), "property name does not match")

    def testConfig(self):
        params = {"pkg_model": "com.csc.admin.model", "pkg_dao":"com.csc.admin.dao"}
        c = model.config.Config(params)
        self.assertEquals("com.csc.admin.model", c.getParam("pkg_model"), "Config test failed")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSchema']
    unittest.main()