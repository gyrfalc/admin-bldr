'''
Created on Dec 22, 2013

@author: Merle
'''

def buildMapper(table, config):
    
    try:
        print "building mapper XML file for " + table.getName() + "..."
        fileout = open(config.getParam("path_mapper") + "/" + table.getMapperFileName(), 'w')
        fileout.write('<!DOCTYPE mapper')
        fileout.write('\n\tPUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"')
        fileout.write('\n\t"http://mybatis.org/dtd/mybatis-3-mapper.dtd">')
 
        fileout.write('\n\n<mapper namespace="'+table.getClassName()+'">')
        
        #build result map
        fileout.write('\n\t<resultMap id="'+table.getClassName()+'Map" type="'+table.getClassName()+'">')
        #for each column
        for column in table.getColumns():
            fileout.write('\n\t\t<result property="'+column.getPropertyName()+'" column="'+column.getName()+'" />')
        fileout.write('\n\t</resultMap>')
        fileout.write('\n\n')
        
        #build list query
        fileout.write('\n\t<select id="list'+table.getClassName()+'" resultMap="'+table.getClassName()+'Map">')
        fileout.write('\n\t\tselect * from '+ table.getName()) 
        fileout.write('\n\t</select>')     
        
        #build select query
        fileout.write('\n\n\t<select id="sel'+table.getClassName()+'" resultMap="'+table.getClassName()+'Map" parameterType="'+table.getClassName()+'" >')
        fileout.write('\n\t\tselect * from '+ table.getName())
        fileout.write('\n\t\twhere ') 
        i = 0
        for column in table.getKeys():
            if i > 0:
                fileout.write('\n\t\tand')
            fileout.write('\n\t\t' + column.getName() + ' = #{'+column.getPropertyName()+'}')
            i += 1
        fileout.write('\n\t</select>')     
        
        #build insert query
        fileout.write('\n')
        fileout.write('\n\t<insert id="ins'+table.getClassName()+'" parameterType="'+table.getClassName()+'">')
        fileout.write('\n\t\tinsert into '+table.getName()+' (')
        i = 0
        for column in table.getColumns():
            fileout.write('\n\t\t\t')
            if i > 0:
                fileout.write(',')
            fileout.write(column.getName())
        fileout.write('\n\t\t)')
        fileout.write('\n\t\tvalues (')
        i = 0
        for column in table.getColumns():
            fileout.write('\n\t\t\t')
            if i > 0:
                fileout.write(',')
            fileout.write('#{'+column.getPropertyName()+'}')
            i += 1
        fileout.write('\n\t\t)')
        fileout.write('\n\t</insert>')
                
        #build update query
        fileout.write('\n')
        fileout.write('\n\t<update id="upd'+table.getClassName()+'" parameterType="'+table.getClassName()+'">')
        fileout.write('\n\t\tupdate ' + table.getName())
        i = 0
        for column in table.getNonKeys():
            fileout.write('\n\t\t')
            if i > 0:
                fileout.write(',')
            fileout.write('set ' + column.getName() + ' = #{' + column.getPropertyName() + '}')
            i += 1
        fileout.write('\n\t\twhere')
        i = 0
        for column in table.getKeys():
            if i > 0:
                fileout.write('and')
            i += 1
            fileout.write('\n\t\t' + column.getName() + ' = #{' + column.getPropertyName() + '}')
        fileout.write('\n\t</update>')      
        
        #build delete query
        fileout.write('\n')
        fileout.write('\n\t<delete id="del'+table.getClassName()+'" parameterType="'+table.getClassName()+'">')
        fileout.write('\n\t\tdelete from ' + table.getName())
        fileout.write('\n\t\twhere')
        i = 0
        for column in table.getKeys():
            if i > 0:
                fileout.write('and')
            i += 1
            fileout.write('\n\t\t' + column.getName() + ' = #{' + column.getPropertyName() + '}')
        fileout.write('\n\t</delete>')           

        fileout.write('\n</mapper>')
        fileout.close()
        
        return True
    
    except Exception as e:
        print "Failed to build mapper file: ", e
        raise
    
def buildMapperInterface(table, config):
    #write a file to the mapper path
    try:
        print "building mapper interface for " + table.getName() + "..."
        fileout = open(config.getParam("path_mapper_interface") + "/" + table.getMapperInterfaceFileName(), 'w')
        fileout.write('package ' + config.getParam("pkg_interface"))
        fileout.write('\n')
        fileout.write('\nimport ' + config.getParam("pkg_model") + '.' + table.getClassName() + ';')
        fileout.write('\n')
        fileout.write('\npublic interface ' + table.getMapperInterfaceName() + " {")
        
        #select list
        fileout.write('\n\tpublic List<'+table.getClassName()+'> list'+table.getClassName()+'();')
        #select row
        fileout.write('\n\tpublic '+table.getClassName()+' sel'+table.getClassName()+'('+table.getClassName() +' params);')
        #update row
        fileout.write('\n\tpublic void upd'+table.getClassName()+'('+table.getClassName() +' params);')
        #insert row
        fileout.write('\n\tpublic void ins'+table.getClassName()+'('+table.getClassName() +' params);')
        #delete row
        fileout.write('\n\tpublic void del'+table.getClassName()+'('+table.getClassName() +' params);')
        
        fileout.write('\n}')
        fileout.close()
        return True
    except Exception as e:
        print "Failed to build mapper class file: ", e
        raise
