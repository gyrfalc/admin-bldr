'''
Created on Dec 22, 2013

@author: Merle
'''
import xml.etree.ElementTree as ET 

if __name__ == '__main__':
    pass


# create a basic xml file
xmlout = open('../playground/test-write.xml', 'w')
xmlout.write('<?xml version="1.0" encoding="UTF-8" ?>')
xmlout.write('\n<data>')
xmlout.write('\n</data>')
xmlout.close()
print 'basic XML file created...'

# read file
#tree = etree.parse('../playground/test-write.xml')
#root = tree.getroot()
#print 'basic XML file read...'

#  The following code does not build a nice document
# I will want to write these documents by hand


# add nodes and save
# build a tree structure
root = ET.Element("data")

action = ET.SubElement(root, "action")
action.set("name", "example")

response = ET.SubElement(action, "response")
response.set("page", "example.jsp")
# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)
tree.write("../playground/output.xml")
print 'output file written'