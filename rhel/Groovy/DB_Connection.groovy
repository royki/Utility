import groovy.sql.Sql

def sql = Sql.newInstance("jdbc:mysql://ndb", "root","root", "com.mysql.jdbc.Driver")
def latestValue = sql.execute('SELECT * FROM ops ORDER BY mname DESC LIMIT 1')
 println(latestValue)


/*
 sql.eachRow('show tables'){ row ->  
        println row[0]  
    }  
*/