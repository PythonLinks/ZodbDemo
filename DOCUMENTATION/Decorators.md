CROMLECH Decorators
==================================

Let us start with wrappers.  Things that wrap around another function.


APPLICATION DECORATORS
---------------------
Cromlech has a lot of decorators   Some are used for
configuration.  This
document explains what is going on.

First question, what is a decorator.  Don't feel bad if you are not sure.
Other languages generally do not have decorators.  I have used them
for a long time, but I had to look them up to really understand.  And maybe
still I do not think in terms of decorators.  The good news, is that you
can genrally ignore the details, and just focus on what they do.

Worst yet there are two kinds of decorators in Cromlech.  Regular decorators
and configurtion decorators.  And it is not really possible to tell the
difference.

So regular decorators are just that, decorators.  Functions that return
functions.  Configuration decorators are more complex.  At start up time
the code is read and those configuration decorators are processed.  They
are used to populate the component registry, so that at run time the
appropriate view can be looked up.  View lookup is based on permission,
context class, URL segment and request type (Post or Get).

First we will do pure decorators, no
configuration. Then the configuration decorators.

Security Decorators
------------------
You can optionally wrap view and model objects in security decorators. When
you try to call a view, the security machinery is invoked.  If the user
does not hae the right permissions, an error is thrown, and usually a login
screen pops up. If a model object is wrapped in a security proxy, access
the to the model object invokes the security machinery.  And of course
you have the option to not wrap objects in securty proxies.

There are of course many different security proxies possible.  A good place
to start is in [security.py](../src/cromdemo/src/cromdemo).

Also take a look at [cromlech.security](https://github.com/Cromlech/cromlech.security/tree/crom)

Configuration Decorators
------------------------
When the application is first started, the code is scanned to read in
  configuratin information.  That informaiton is stored in the cromlech
  component registry.  The information is defined using the following
  decorators. 

View Decorators
-----------------
Well these are the most important configuration decorators.  They define
who can see which view.  Here are several.
  
@view_component
  Tells Cromlech that the folloiwng object should be treated as a view. 

@name('logout')
  Tells cromlech that urls that end in '/logout' should use this view.
  
@context(SomeInterface)
  Tells cromlech that objects which implement SomeInterface can display this
  view. If SomeInterface is 'Interface', then all objects with an Interface
  can display this view.  The argument can also be a class.

@context(Unauthorized)
  So if an object has as security wrapper which throws an exception, then this view should be displayed.

@target(ITab)
  NOT SURE WHAT THIS ONE DOES
  
@permissions('ViewProtected')
  The user has to have that permission to view this object.
  
@implementer(IProtectedComponent)
  NOT SURE WHAT THIS ONE DOES

@viewlet
  This means that this viewlet goes inside another larger view.
  
@slot(ProtectedHeader)
  Where does it go?  Well in the slot called 'ProtectedHeader'

@form_component
  This view is actually a form.   



In general Cromlech has great detailed documentation, but it is all hidden in the doc tests. So always look for it there.





