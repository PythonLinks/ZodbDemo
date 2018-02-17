Why ZODB + Cromlech
=============

This article first tells why you would wnat to use
Cromlech

The software tools you use determine the concepts you can leverage.


The ZODB gives us a persistent graph of Objects.  Cromlech
then allows us to traverse that graph, and select the appropriate
view for those objects. We can also adapt objects.  And do security on
Objects or views.  Most importantly it is not a framework, it is a toolkit.
So we only use what we want to use. 


Why Cromlech?
-------------

Why would one choose a relatively unknown framework Cromlech over other
platforms with larger installed bases?  Because it is more expressive.
Cromlech gives you better
flexibility, productivity and
for managing complexity than its competitors.
While Grok, Zope and Pyramid are these large
frameworks. Cromlech does something
I had not thought possible,  the individual components
can be used separately from each
other.
Cromlech is literally a tool chest.
So you do not have to import the whole framework, just the parts that
you need.  You can pull in whichever
pieces you want. You can replace whichever pieces you do not want. 


And while Flask and Pyramid are quite stripped down,
Cromlech, like Grok and Zope gives you
a rich collection of concepts on which to build. And finally Cromlech will
support you in building very
complex applications with multiple Databases, asynchronous bits,
web-sockets, etc…

I invite you to read [Cromlech Vs Django](./CromlechVsDjango.md)

I invite you to read [Cromlech Vs Pyramid](./CromlechVsPyramid.md)


I did a full API
Cromlech has been used in multiple different applications. 
/ ReactJS app
a Solr + ArangoDB app for uploading files. 


