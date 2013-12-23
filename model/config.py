'''
Created on Dec 22, 2013

@author: Merle
'''

class Config(object):
    '''
    classdocs
    '''
    params = {}

    def __init__(self, params):
        '''
        Constructor
        '''
        self.params = params
    
    
    def getParam(self, name):
        return self.params[name]
    def setParam(self, name, value):
        self.params[name] = value
    def getParamList(self):
        return self.params