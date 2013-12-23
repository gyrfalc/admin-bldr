'''
Created on Dec 22, 2013

@author: Merle
'''
import doers.util

class Column(object):
    '''
    classdocs
    '''
    name = "";
    type = "";

    
    def setName(self, p_name):
        self.name = p_name
    def getName(self):
        return self.name
    
    def setType(self, p_type):
        self.type = p_type
    def getType(self):
        return self.type
    
    def getJavaType(self):
        return self.type.lower().capitalize()
    
    def getPropertyName(self):
        return doers.util.toCamelCase(self.name) 
    
    def getMethodName(self):
        return doers.util.toLeadingCamelCase(self.name)
