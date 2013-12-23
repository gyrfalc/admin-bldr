'''
Created on Dec 22, 2013

@author: Merle
'''

class Schema(object):
    '''
    classdocs
    '''

    tables = {}
    name = ""

    def setName(self, p_name):
        self.name = p_name
    def getName(self):
        return self.name
        
    def setTables(self, p_tables):
        self.tables = p_tables
    def getTables(self):
        return self.tables
    
    