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