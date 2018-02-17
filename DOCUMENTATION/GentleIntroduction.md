A Gentle Introduction to the Cromlech Demo
================

So what does all of this software do?

Here are the detailed [Installation Instructions](./INSTALL.md).

OBJECT MODEL
------------

We basically have two object types.  Containers and Leafs.  A container can
contain other things.  Leaves cannot.  The current demo only has one
container, at the root.  I am working to be able to add more containers.
And leaves can be added to containers, but not to leaves.

There are two major views, and a number of minor views.  All views
are represented by Python Objects.  The display
may be defined in Python or in a
page template.

The two major views are the Collection (Or root) view, and the leaf view.
There are a numer of sub views. Tabs are used in the leaf view.  One can
view a leaf, edit a leaf, or possibly see the protected subview. I think
that there is also a user sub view, which shows you the logged in user. 

And then there are the form views.  One form to login.  One form to edit a
leaf.  Soon we will have a form to add leaves and another form to
add containers. 

Let us take a look at the layout templates.  

layout.pt is the leaf  layout.

tabs.pt is a set of tabs across the top of the screen.

leaf.pt displays a leaf. 

home.pt shows the root container view. 

Server Configuration
-------------------

The demo is not just an object model, it also
configures the application server. 

In the package root, server.py configures the application server.  loader.py
loads the Python Path using config.json.  You can read more about them
[here](./server.md)

Now we get to the interesting stuff. [app.py](../src/cromdemo/src/cromdemo/app.py)  That is where the application functionality
is defined.


When your browser goes
to a url, the wsgi server calls a Python application.  And it passest a
bunch of variables to that Python application in a request object.
Cromlech uses a concept called object publishing.  The
object publisher first looks up the object,
then it looks up the view on that object.
It executes the view and returns the result.

That is the simple story.  Security requirements make things even more
complex than that. You can either secure your views or not.  If you do not
secure your views, then the above description holds.  Everything is easy.
If you do secure your views or objects.  Cromlech wraps them in a security
proxy.  When you try to access them or call them, the security machinery
is invoked.

The first thing the security machinery does is to check if you are logged in.
If not, if you are the anonymous user, then you do not have permission, it
throws an exception, and you have a chance to login. If you are logged in,
then it it checks what permission is required, and whether you have that
permission or not.

This is a very simple security model.  If you want a much more sophisticated
model, I recommend zope.securitypolicy.


How does it know if you are logged in or not or who you are?
The request stores its values in a dictionary called
environ. That may include cookies.  And the cookies may include the
identity of the logged in user.  So before calling the application it has
to create a user session, and convert that cookie into a user name.  And
if there is a user name, it has to convert that name into a Zope principal
object, used by the security machinery, or into the unauthenticaed user.

And then at the end, when object publishing executes the view, to generate
the response object,  the security machinery will be
invoked.  Of course security is only invoked if you have used a decorator
to declare something to be a protected view.
If the called view is protected, the security will check if it is a logged
in principal,  what permissions are needed for
that view, and  if the principal has those permissions.  If all is
well, the view is rendered,  otherwise a security exception is thrown,
and the user is
redirected to a login page.

How is all this implemented?
Before you get to the Application several things happen in decorators.

Before calling the application, the sessiond decorator is called.  It checks
to see if there is a session, if so it sets
environ[“username”]= uername

If there is a username, it then creates a principal.

FILE SYSTEM STRUCTURE
====================
Okay, now let us take a loot at the structure of the software.

Here are the files.
The following files are included.

bootstrap.py
loader.py
server.py
          auth.py
          models.py
          security.py
          app.py
          browser
             forms.py
             layout.py
             views.py
             templates
                home.pt
                layout.pt
                leaf.pt
                tabs.pt

There are 4 templates. The layout gives the overall appearance.  There is a
home page tempjlate, a leaf template  with a link to a protected view.
And a tabs template.

There is a layout.py file.  It includes a layout object.  And within the
layout there can be two viewlets.  One to show a protected view.
And one to show actions. 
