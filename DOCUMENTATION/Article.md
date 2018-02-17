Here is the Cromlech talk proposal for PyCON USA 2018.

This talk describes Cromlech, a modern version of Zope.

Zope was the first Web Server Framework. While it is still heavily used in Plone it has mostly been forgotten and disrespected. Grok simplified Zope security and configuration, but under the hood it created a worse tangle. Cromlech reproduces the Grok concepts, but has been massively refactored and simplified.

I write as a user of Cromlech. I am using Cromlech to  modernize Zopache.  Zopache is a browser-based Javascript IDE.  I have been using Zopache internally for 4 years now, I want to open source it.  Zopache is designed to e an easy-to-use way for people to start using Zope libraries.  I am using Cromlech to port Zopache from Python 2 and Grok to Python 3 and Cromlech, and am just thrilled with what I have seen.   So it is my privileged to be able to report on Cromlech to the wider Python community. The world needs to know about the great work which has been done on Cromlehc.

So let us look at what these packages have to offer.

Cromlech is a package for servers.  Usually it runs behind a WebOb
wsgi server, but it can also be run from the command line, from asynio, or from
Tornado, or as a cron job.

Zope and Cromlech support object publishing.  Find an object, find the appropriate view on the object, execute the view, and return either some json, a web page or a viewlet for that object.

Cromlech supports multiple ways to find an object.  Either routing or traversal of one or more object or relational  databases can be performed.  One can mix and match, for example, first route, then traverse, then route again.

Zopache simplifies finding objects.  It only does traversal of one ZODB.

Once the python model object has been identified, Cromlech is usually configured to look up a view on that object, executes it and returns the result.
Once you have found the object, views are looked up using a component registry.  Cromlech offers a tree of registries.  If registration cannot be found in one registry, it is looked for in the parent registry.

Zopache registers the views on basic web objects  for you.  These include HTML, CSS and Javascript objects.


Like zope.security, Cromlech has a concept of principals. who have permissions.  Cromlech allows one to wrap either views or objects in security proxies.  They can then only be accessed if the current principal has the correct permissions.  Otherwise an exception is thrown, and usually the application redirects to a login page. 

Zopache simplifies this.  The admin user (principal) has CRUD permission, the anonymous user has only view permission.  That is typical for most
early-stage websites.

There are two times when security proxies are accessed.  If a view is wrapped in a  security proxy, then when the view is called, the security proxy is first executed.  If there is permission the view is executed, if not an exception is thrown and the user is usually redirected to a login panel.

During traversal, or routing, objects can also be wrapped in a security proxy.  Those objects  can then only be accessed if the user has the appropriate permissions, or else again an exception is thrown.

A wonderful and unique thing about Cromlech is that security proxies on views and objects are  optional and can be mixed and matched.

Every prototype application needs CRUD.  Zope.interface defines the editable attributes on an object.  Zeam.form creates the Crud forms.  The older zope.formlib and z3c.form are in a well earned retirement.  They required way to many adaptations to be understandable.   Code for a Zeam.form will be shown.
You can see it [here](https://github.com/PythonLinks/CromlechDemo/blob/master/src/cromdemo/src/cromdemo/browser/forms.py).

Zopache simplifies cromlech by providing CRUD forms for containers, HTML, CSS and Javascript objects.

##Adapters
Adapters are an important part of the Zope world.  They are not unique to the Cromlech, but they do deserve to be covered.  Views are adaptors of the displayed objects, but there are other types of adaptors.  The best example I know or
are the adapters in the Zopache ZMI which manages the objects in a container.  One needs to be able to select, delete, rename, copy and move those objects.  The zopache.zmi, provides this functionality, through-the-web.    In a
rich application, there are so many different possibilities, that adapters are most needed.

When using the ZMI on different objects, they need to be treated differently.  Some objects are not allowed to be deleted.  Other
objects are not allowed to be renamed.   .  Some objects have canonical URL's.  This was covered in my ZODB talk, the slide will be shown again.  When these objects are renamed, the canonical index name needs to be changed.  When they are deleted, the canonical name needs to be deleted.  Some objects may be indexed in catalogs.  On deletion they need to be removed from the catalog.

We are really operating on a graph of objects, and different objects interact differently with that graph.  Some objects may be referenced from another part of the tree.  Deleting that object, may require that a reference to that object be changed to None.

Some objects may have copies in another part of the tree.  A so called Siamese Twin.  For example content objects may be present in the authors home directory, and in a shared published group directory.  I believe Reddit does this, although maybe not in Python.  Renaming or moving that object requires that its siamese twin also be moved or renamed..  Zopache.ZMI adaptors support all of these different use cases.  As the complexity of the object graph increases, Adaptors make it easy to keep things correctly organized.

 ##Sessions
 Since HTTP is a stateless protocol, Sessions are an important part of modern web applications.  Cromlech supports, JWT sessions, file sessions and Redis sessions.   In server.py, the application gets wrapped in a session manager.  Before finding the model object, the session manager is invoked and the person is authenticated or declared to be the unauthenticated principal.

##Cromlech is a toolkit
Zope and grok were massive frameworks,  you could not throw out any part.
 Miraculously,  cromlech is more of a toolset.  One can build lots of different server configurations with Cromlech.  One can choose which pieces to use.

 The first thing one does in Cromlech is to configure the server.  I will show you the configuration file for Zopache, and explain what every line does.

Here is a description of the  [configuration file](https://github.com/PythonLinks/CromlechDemo/blob/master/configuration.txt).  It will be included in this talk.

Competition.
[Here ](https://github.com/PythonLinks/CromlechDemo/blob/master/DOCUMENTATION/CromlechVsDjango.md)
is the comparison of Pyramid and Cromlech. It will be included in this talk.

##Pyramid.
[Here ](https://github.com/PythonLinks/CromlechDemo/blob/master/DOCUMENTATION/CromlechVsPyramid.md)
is the comparison of Pyramid and Cromlech. It will be included in this talk.