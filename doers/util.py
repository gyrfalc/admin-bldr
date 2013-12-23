'''
Created on Dec 22, 2013

@author: Merle
'''

PKG_MODEL = "package com.csc.admin.model;"



def toCamelCase(instr):
    '''
    takes underscore delimited name and builds camelCase; does not capitalize the first letter
    '''
    tokens = instr.split('_')
    newstr = "";
    i = 0
    for token in tokens:
        #print token
        if i== 0:
            newstr = token.lower()
        else:
            newstr = newstr + token.lower().capitalize()
        i += 1
    return newstr

def toLeadingCamelCase(instr):
    '''
    takes underscore delimited name and builds CamelCase with leading capital
    '''
    tokens = instr.split('_')
    newstr = "";
    for token in tokens:
        #print token
        newstr = newstr + token.lower().capitalize()
    return newstr    