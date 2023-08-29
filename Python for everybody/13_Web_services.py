# Data on the Web
""" 
1. With the HTTP Request/Response well understood and well supported, there was a natural move toward exchanging data between programs using these protocols.
2. We needed to come up with an agreed way to represent data going between applications and across networks.
3. There are two commonly used formats: XML and JSON
"""
# XML = eXtensible Markup Language
""" 
1. Primary purpose is to help information systems share structured data.
2. It started as a simplified subset of the Standard Generalized Markup Language(SGML), and is designed to be relatively human-legible
"""
# XML Terminology
""" 
1. Tags indicate the beginning and ending of elements.
2. Attributes - Keyword/value pairs on the opening tag of XML
3. Serialize/De-serialize - Convert data in one program into a common format that can be stored and/or transmitted between systems in a programming language-independent manner.
"""

# XML Basics
""" 
1. Start Tag
2. End Tag
3. Text Content
4. Attribute

<person>
<name>Chuck</name>
<phone type="intl"> +17343034456 </phone>
<email hide="yes"/>
</person>

"""
# XML Schema
""" 
Describing a "contract" as to what is acceptable XML 
1. Description of the legal format of an XML document
2. Expressed in terms of constraints on the structure and content of documents.
3. Often used to specify a "contract" between systems - "My system will only accept XML that conforms to this particular Schema"
4. If a particular piece of XML meets the specification of the schema - it is said to "validate"
"""

# XML Document

""" <person>
    <lastname>Severance</lastname>
    <age>17</age>
    <dateborn>2001-04-17</dateborn>
</person> """

# XML schema contract
""" <xs:complexType name = "person">
<xs:sequence>
<xs:element name="lastname" type="xs:string"/>
<xs:element name="age" type="xs:integer"/>
<xs:element name="dateborn" type="xs:date"/>
</xs:sequence>
</xs:complexType> """

# Many XML Schema Languages
""" 
1. Document Type Definition(DTD)
2. Standard Generalized Markup Language(ISO 8879:1986 SGML)
3. XML Schema from W3C - (XSD)
"""
# XSD XML Schema (W3C spec)
""" 
1. We will focus on the world wide web (W3C) version
2. It is often called "W3C Schema" because "Schema" is considered generic
3. More commonly it is called XSD because the file names end in .xsd
"""