'''
Created on Dec 22, 2013

@author: Merle
'''

if __name__ == '__main__':
    pass

 
import xml.etree.ElementTree as etree 

print "Opening file..."

tree = etree.parse('../playground/test-read.xml')
root = tree.getroot()

for child in root:
    print child.tag, child.attrib
    
print "Iterate through tables ..."
for table in root.iter('table'):
    print table.tag, table.attrib

    for column in table:
        print "Column attribute name = " + column.attrib["name"]
        print column.tag, column.attrib
    
    
    
print "Done"