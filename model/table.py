'''
Created on Dec 22, 2013

@author: Merle
'''

import doers.util

class Table(object):
    '''
    classdocs
    '''
    name = "";
    columns = {}
    keys = {}
    nonkeys = {}
    permissions = {'C','R','U','D'}

        
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
        
    def getClassName(self):
        return doers.util.toLeadingCamelCase(self.name)     
    
    def getClassFileName(self):
        return self.getClassName() + '.java'
    
    def getMapperFileName(self):
        return self.getClassName() + "Map.xml"
    
    def getMapperInterfaceName(self):
        return "I" + self.getClassName() + "Map"
    def getMapperInterfaceFileName(self):
        return self.getMapperInterfaceName() + '.java'
    
    def getColumns(self):
        return self.columns
    def setColumns(self, p_columns):
        self.columns = p_columns
    
    def getKeys(self):
        return self.keys
    def setKeys(self, p_keys):
        self.keys = p_keys
    
    def getNonKeys(self):
        return self.nonkeys
    def setNonKeys(self, p_nonkeys):
        self.nonkeys = p_nonkeys
        
    def getPermissions(self):
        return self.permissions
    def setPermissions(self, p_permissions):
        self.permissions = p_permissions
        
    def allowInsert(self):
        return 'C' in self.permissions
    def allowUpdate(self):
        return 'U' in self.permissions
    def allowDelete(self):
        return 'D' in self.permissions
        