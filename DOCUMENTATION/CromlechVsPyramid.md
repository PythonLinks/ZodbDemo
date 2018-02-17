Comparison of Cromlech and Pyramid
=================================

So why not just use Pyramid?  Pyramid is both too simple and too complex.
Worse yet, Pyramid really only serves wsgi sites.

Pyramid is too complex, becasue it is an entire framework.  You have to
import all of Pyramid. Or at least most of it.  In contrast Cromlech is
a collection of brilliantly factored tools, which can be used independently of
each other. 

But Pyramid is also too simple. 
The reason that I like Grok or Cromlech is
that they are rich environments.  They give you a lot of concepts to build
on.  In contrast Pyramid is quite stripped down.
Optimized for computer speed,
rather than ease of development. So Pyrmaid tossed out zope.security in foavor
simplistic Access Control Lists.  Pyramid hides the component registry under
a simpler api, and only uses it for view lookups. Pyramid does not include
zope.interface and CRUD.  Choose your own forms libraries. 
In particular the wonderfully expressive zope.securitypolicy has not
been ported to Pyramid.  Maybe it cannot be because Pyramid does nto use 
zope.security.

The other problem with Pyrmaid  is that itt only works
as a WSGI server, whereas Cromlech is more a collection of separate tools.
Let us take a look at the limitations of running Pyramid with Tornado.  
Reportedly you can only run Pyramid as a single thread.
https://stackoverflow.com/questions/29496870/how-to-use-pyramid-with-tornado
Whereas with Cromlech you can call app.py from a tornado process and run 
as many threads as you want. 

To summarize, Pyrmiad is a framework, not a collection of well factored tools.
And Pyramid strips out everything, optimizing computer performance
over development speed. 