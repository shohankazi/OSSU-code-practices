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