Introduction To Cromlech
=======================


Cromlech is a conceptual framework for building Python applications.  But
software needs more than concepts, it needs definitions, so Cromlech is 
a set of interfaces which define  those concepts, and
a specific implementation of those interfaces.


So what are the concepts driving Cromlech? They are carefully
specified  by the
[interface definitions](https://github.com/Cromlech/cromlech.browser/blob/crom/src/cromlech/browser/interfaces.py).  Cromlech WSGI Interfaces define what
services the wsgi server  must provide. 
You probably already have an intuitive understanding
of what are request and resposne.

Next up Cromlech defines publishers and Publication Root.  An object
pulisher starts at the publication root, traverses to an object, 
displays a view on it, and returns the Response.
And of course Cromlech defines the interfaces for  Forms, Templates URLs
and sessions. 

This demo shows how to build a wsgi application using the ZODB,
but Cromlech  also can work without wsgi and without the ZODB,
either as a Python Script or even behind an asyncio or
Tornado server.  Cromlech supports both routing and traversal.  It supports
view lookup on objects.  It supports sessions, and security.
