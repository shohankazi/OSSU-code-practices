""" 
# TCP => Transmission Control Protocol
1. Built on top of IP(Internet Protocol)
2. Assumes IP might lose some data - stores and retransmits data if it seems to be lost.
3. Handles "flow control" using a transmit window
4. Provides a nice reliable pipe

# TCP Connections / Sockets
In computer networking, an internet socket or network is an endpoint of a bidirectional inter-process communication flow across an internet Protocol-based computer network, such as the Internet.

    Process ====> Internet ====> Process

# TCP Port Numbers
1. A port is an application-specific or process-specific software communications endpoint
2. It allows multiple networked applications to coexist on the same server.
3. There is a list of well-known TCP port numbers

# Common TCP Ports

1. Telnet(23) - Login
2. SSH(22) - Secure Login
3. HTTP(80) 
4. HTTPS(443) - Secure
5. SMTP(25) - Mail
6. IMAP(143/220/993) - Mail Retrieval
7. POP(109/110) - Mail Retrieval
8. DNS(53) - Domain Name
9. FTP(21) - File Transfer
"""

# Sockets in Python
# Python has a built-in support for TCP Sockets

# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect('data.py4e.org',80)


# Application Protocol
""" 
1. Since TCP (and python) gives us a reliable socket, what do we want to do with the socket? What problem do we want to solve?
2. Application Protocols
    -> Mail
    -> World Wide Web
"""
# HTTP = Hyper Text Transfer Protocol
""" 
1. The dominant Application Layer protocol on the internet.
2. Invented for the web - to retrieve HTML, Images, Documents, etc
3. Extended to be data in addition to documents - RSS, Web services, etc. Basic Concept - Make a Connection - Request a document - Retrieve the document - Close the connection

The Hyper Text Transfer Protocol is the set of rules to allow browsers to retrieve web documents from servers over the internet.

"""

# What is a protocol?
""" 
1. A set of rules that all parties follow so we can predict each other's behavior
2. And not bump into each other
    -> On two-way roads in USA, drive on the right-hand side of the road
    -> On two-way roads in the UK, drive on the left-hand side of the road.
    
http://   www.dr-chuck.com/page1.htm
Protocol         host      document
"""

# Getting data from the server
""" 
1. Each the user clicks on an anchor tag with an href= value to switch to a new page, the browser makes a connection to the web server and issues a "GET" request - to GET the content of the page at the specific URL
2. The server returns the HTML document to the Browser which formats and displays the document to the user.
"""

# Internet Standards
""" 
1. The standards for all of the internet protocols(inner workings) are developed by an organization
2. Internet Engineering Task Force(IETF)
3. www.ietf.org
4. Standards are called "RFC's" - "Request for Comments"
"""

# An HTTP request in python

# import socket

# mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org',80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if (len(data)<1):
#         break
#     print(data.decode())
# mysock.close()

""" ASCII = American Standard Code for information Interchange """
# Representing Simple Strings
""" 
1. Each character is represented by a number between 0 and 256 stored in 8 bits of memory.
2. We refer to 8 bits of memory as a byte of memory.
3. The ord() function tells us the numeric value of a simple ASCII character.
"""
# print(ord('H'))
# print(ord('e'))
# print(ord('\n'))

# Multi-Byte Characters
""" To represent the wide range of characters computers must handle we represent characters with more than one byte 
    1. UTF-16 - Fixed length - Two bytes
    2. UTF-32 - Fixed length - Four bytes
    3. UTF-8 - 1-4 bytes
        -> Upwards compatible with ASCII
        -> Automatic detection between ASCII and UTF-8
        -> UTF-8 is recommended practice for encoding data to be exchanged between systems.
==> In Python 3, all strings are Unicode
"""

# Python3 and Unicode
""" 
1. In python 3, all strings internally are Unicode
2. Working with string variables in python programs and reading data from files usually "just works"
3. When we talk to a network resource using sockets or talk to a database we have to encode and decode data(usually to UTF-8)
"""

# Python strings to bytes
""" 
1. When we talk to an external resource like a network socket we sends bytes, so we need to encode python 3 strings into a given character encoding
2. When we read data from an external resource, we must decode it based on the character set so it is properly represented in Python 3 as a string.
"""

# Using urllib in python
""" Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file """

# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())
    

# Like a file

# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1
# print(counts)

# Reading web pages

# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
# for line in fhand:
#     print(line.decode().strip())

# What is web scraping?
""" 
1. When a program or script pretends to be a browser and retrieves web pages, looks at those web pages, extracts information, and then looks at more web pages.
2. Search engines scrape web pages - we call this "spidering the web" or "web crawling"
"""
# Why scrape?
""" 
1. Pull Data - particularly social data - who links to who?
2. Get your own data back out of some system that has no "export capability"
3. Monitor a site for new information
4. Spider the web to make a database for a search engine
"""
# Scraping Web Pages
""" 
1. There is some controversy about web page scraping and some sites are a bit snippy about it.
2. Republishing copyrighted information is not allowed
3. Violating terms of service is not allowed
    ==> The Easy way - Beautiful Soup
        1. You could do string searches the hard way 
        2. Or use the free software library called BEautifulSoup from www.crummy.com
"""
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html,'html.parser')

# # Retrieve all of the the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href',None))
    
# Summary 
""" 
1. The TCP/IP gives us pipes/sockets between applications
2. We designed application protocols to make use of these pipes
3. HyperText Transfer Protocol(HTTP) is a simple yet powerful
4. Python has good support for sockets, HTTP, and HTML parsing
"""
# import socket

# mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org',80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if (len(data)<1):
#         break
#     print(data.decode())
# mysock.close()

# Exercise network programming - first

# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')

# mysock.close()