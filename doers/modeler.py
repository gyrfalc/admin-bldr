'''
Created on Dec 22, 2013

@author: Merle
'''

def buildSchemaSchemaModel(schema, config):
    print "===================================================================="
    print "creating model objects for schema " + schema.getName() + "..."
    
    retval = True
    
    for table in schema.getTables():
        if buildTableModel(table, config) != True:
            retval = False
            break
        

    print "creating model objects for schema " + schema.getName() + "...DONE"
    
    return retval

def buildTableModel(table, config):
    
    print "creating model for " + table.getName() + "..."
    
    try:
        fileout = open(config.getParam("path_model") + "/" + table.getClassFileName(), 'w')
        fileout.write("package " + config.getParam("pkg_model") + ";")
        fileout.write("\n")
        # standard date import, can always clean up code later
        fileout.write("\nimport java.util.Date;")
        fileout.write("\n")
        #
        fileout.write("\npublic class " + table.getClassName())
        fileout.write("\n{")
        fileout.write("\n")
        columns = table.getColumns()
        for column in columns:
            fileout.write("\n\tprivate " + column.getJavaType() + " " + column.getPropertyName() + ";")
        fileout.write("\n")
        for column in columns:
            # build the getter
            fileout.write("\n\tpublic " + column.getJavaType() + " get" + column.getMethodName() + "() {")
            fileout.write("\n\t\treturn " + column.getPropertyName() + ":")
            fileout.write("\n\t}")
            # build the setter
            fileout.write("\n\tpublic " + column.getJavaType() + " set" + column.getMethodName() + "(" + column.getJavaType() + " val) {")
            fileout.write("\n\t\t" + column.getPropertyName() + " = val:")
            fileout.write("\n\t}")
            
            
            
        fileout.write("\n}")
        fileout.close()
        return True
    except Exception as e:
        print "Failed to build table model: ", e
        raise
