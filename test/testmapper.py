'''
Created on Dec 22, 2013

@author: Merle
'''
import unittest
import doers.mapper
import model.table
import model.column
import model.config

class Test(unittest.TestCase):
    
    params = {"pkg_model": "com.csc.admin.model", "path_model":"../playground", "path_mapper":"../playground", "path_mapper_interface":"../playground"}
    config = model.config.Config(params)       
   

    def setUp(self):
        pass
    
    def testMapperInterface(self):
        t = model.table.Table()
        t.setName("fabric_Family")
        self.assertEquals("FabricFamilyMap.xml", t.getMapperFileName())
        self.assertEquals("IFabricFamilyMap",t.getMapperInterfaceName())
        self.assertEquals("IFabricFamilyMap.java",t.getMapperInterfaceFileName());
        
    def testBuildMapperInterface(self):
       
        k1 = model.column.Column()
        k1.setName("fabric_cd")
        c2 = model.column.Column()
        c2.setName("fabric_nm")    
        c3 = model.column.Column()
        c3.setName("fabric_desc")
        t = model.table.Table()
        t.setName("fabric")
        t.setKeys({k1})
        t.setNonKeys({c2, c3})
        t.setColumns({k1,c2,c3})
        
        self.assertTrue(doers.mapper.buildMapperInterface(t, self.config), "Failed to build mapper file")
    

    def testBuildMap(self):
        
        k1 = model.column.Column()
        k1.setName("fabric_cd")
        c2 = model.column.Column()
        c2.setName("fabric_nm")    
        c3 = model.column.Column()
        c3.setName("fabric_desc")
        t = model.table.Table()
        t.setName("fabric")
        t.setKeys({k1})
        t.setNonKeys({c2, c3})
        t.setColumns({k1,c2,c3})
        
        self.assertTrue(doers.mapper.buildMapper(t, self.config), "Failed to build mapper file")
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBuildMap']
    unittest.main()