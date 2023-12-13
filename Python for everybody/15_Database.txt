# Random Access
""" 
1. When you can randomly access data
2. How can you layout data to be most efficient?
3. Sorting might not be the best idea
"""
# Relational Databases
""" 
Relational databases model data by storing rows and columns in tables. The power of the relational database lies in its ability to efficiently retrieve data from those tables and in particular where there are multiple tables and the relationships between those tables involved in the query.
"""
# Terminology
""" 
1. Database - contains many tables
2. Relation (or table) - contains tuples and attributes
3. Tuple (or row) - a set of fields that generally represents an "object" like a person or a music track
4. Attribute (also column or field) - one of possibly many elements of data corresponding to the object represented by the row.

A relation is defined as a set of tuples that have the same attributes. A tuple usually represents an object and information about that object. Objects are typically physical objects or concepts. A relation is usually described as a table, which is organized into rows and columns. All the data referenced by an attribute are in the same domain and conform to the same constraints.
"""

# SQL
""" 
1. Structured Query Language is the language we use to issue commands to the database
    => Create a table
    => Retrieve some data
    => Insert data
    => Delete data
"""

# Web Applications w/Databases
""" 
1. Application Developer - Builds the logic for the application, the look and feel of the application - monitors the application for problems
2. Database Administrator - Monitors and adjusts the database as the program runs in production
3. Often both people participate in the building of the "Data Model"
"""
# Database Administrator
""" 
A database administrator (DBA) is a person responsible for the design, implementation, maintenance, and repair of an organization's database. The role includes the development and design of database strategies, monitoring and improving database performance and capacity, and planning for future expansion requirements. They may also plan, coordinate, and implement security measures to safeguard the database.
"""

# Database Model
""" 
A database model or database schema is the structure or format of a database, described in a formal language supported by the database management system. In other words, a "database model" is the application of a data model when used in conjunction with a database management system.
"""

# Common Database System
""" 
1. Three major Database Management Systems in wide use
    => Oracle - Large, commercial, enterprise-scale, very very tweak able
    => Mysql - simpler but very fast and scalable - commercial open source
    => SqlServer - Very nice - from Microsoft (also access)
2. Many other smaller projects, free and open source
    => HSQL, SQLite, postgres, ...
"""
#SQL Summary

""" 
Insert = INSERT INTO Users(name,email) VALUES('Kristin','kf@umich.edu)
Delete = DELETE FROM Users WHERE email='ted@umich.edu'
Update = UPDATE Users SET name="Charles" WHERE email="csev@umich.edu"
Select = SELECT * FROM Users WHERE email='csev@umich.edu'
SELECT * FROM Users WHERE email='csev@umich.edu'
SELECT * FROM Users ORDER BY email
"""

""" 
1. Tables pretty much look like big fast programmable spreadsheets with rows, columns, and commands
2. The power comes when we have more than one table and we can exploit the relationships between the tables
"""

# Database Design

""" 
1. Database Design is an art form of its own with particular skills and experience
2. Our goal is to avoid the really bad mistakes and design clean and easily understood database
3. Others may performance tune things later
4. Database design starts with a picture
"""

# Building a Data Model
""" 
1. Drawing a picture of the data objects for our application and then figuring out how to represent the objects and their relationships
2. Basic Rule - Don't put the same string data in twice - use a relationship instead
3. When there is one thing in the "real world" there should be one copy of that in the database
"""
# For each "piece of info"
""" 
1. Is the column an object or an attribute of another object?
2. Once we define objects, we need to define the relationships between objects.
"""
# Database Normalization(3NF)
""" 
1. There is 'tons' of database theory - way too much to understand without excessive predicate calculus
2. Do not replicate data - reference data - point at data
3. Use integers for keys and for references
4. Add a special "key" column to each table which we will make references to. By convention, many programmers call this column "id"
"""
# Three kinds of keys
""" 
1. Primary Key - generally an integer auto-increment field
2. Logical key - What the outside world uses for lookup
3. Foreign key - generally an integer key pointing to a row in another table
"""
# Key RULES
""" 
1. Never use your logical key as the primary key
2. Logical keys can and do change, albeit slowly
3. Relationships that are based on matching string fields are less efficient than integers
"""
# Foreign Keys
""" 
1. A foreign key is when a table has a column that contains a key which points to the primary key of another table
2. When all primary keys are integers, then all foreign keys are integers - this is good - very good
"""
# Relational Power
""" 
1.By removing the replicated data and replacing it with references to a single copy of each bit of data we build a "web" of information that the relational database can read through very quickly - even for very large amounts of data
2. Often when you want some data it comes from a number of tables linked by these foreign keys
"""
# The JOIN Operation
""" 
1. The JOIN operation links across several tables as part of a select operation
2. You must tell the JOIN how to use the keys that make the connection between the tables using an ON clause
"""
# Many to Many
""" 
1. Sometimes we need to model a relationship that is many-to-many
2. We need to add a "connection" table with two foreign keys
3. There is usually no separate primary key
"""

# Complexity Enables Speed
""" 
1. Complexity makes speed possible and allows you to get very fast results as the data size grows
2. By normalizing the data and linking it with integer keys, the overall amount of data which the relational database must scan is far lower than if the data were simply flattened out
3. It might seem like a tradeoff - spend some time designing your database so it continues to be fast when your application is a success.
"""
# Additional SQL Topics
""" 
1. Indexes improve access performance for things like string fields
2. Constraints on data - (cannot be NULL,etc)
3. Transactions - allow SQL operations to be grouped and done as a unit
"""
# Summary
""" 
1. Relational database allow us to scale to very large amounts of data.
2. The key is to have one copy of any data element and use relations and joins to link the data to multiple places
3. This greatly reduces the amount of data which much be scanned when doing complex operations across large amounts of data
4. Database and SQL design is a bit of an art form 
"""