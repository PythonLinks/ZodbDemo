 How does cromlech work?

Cromlech is a set of tools which you can string together any way you want.

The way that the demo strings them together is in a file called server.py. 

Server.py loads everything which is needed.  It bootstraps the application.

You can call app.py from a WSGI server, from an Async server such as Tornado,
or from the command line, maybe in a debugging session.  Maybe you would
want to turn it into a script, to be calledby a cron job.  It is quite
flexible. 

The first thing app.py needs to do, is to know where to find everything.
So it loads a config.json file with all of the Python Paths.

with Configuration('config.json') as config:
   ...

That is a very nice piece of magic, bucause it is now easy to modify the
app.py script.  One does not need to mess with buildout to do this. 

Now we need to actually  configure cromlech.  In app.py we give it
all the configuration information.

First create a registry.
  implicit.initialize()

Then create your database.
   with open(config['zodb']['config'], 'r') as fd:
           db = init_db_from_file(fd, init_db)

You can either route to different applications.
 router = urlmap.URLMap()
     router['/demo1'] = demo1

And then tell the middleware how to access the application.
If you are using the ZODB, then you want to use the ZODB wrapper.
    import cromlech.zodb.middleware.ZODBApp
    application = ZODBApp(router, db, key="zodb.connection")

Or if you just have one application
application = ZODBApp(demo1, db, key="zodb.connection")

ZODGApp  gets a connection the database,
and stores it in the Environ Variables.

There are a few other commands in server.py, but these are the most important
ones. 

When you want to work from the terminal, 
the easy way to do this is to just run
python app.py

You can then insert breakpoints or do whatever you want.

But say you want to write a script that runs in a cron job.
It is pretty easy to do that also.  Just modify server.py
By reading the path variales from a JSON file, Cromlech makes it
very easy to create multiple scripts which all work in the same environment. 
.
Session Wrappers
----------------
HTTP is a stateless protocol, so sessions are used to keep track
of logged in users.  When the HTTP request arrives, the server needs
to figure out who the user is.  There are several ways to do it.
Identity information can be encrypted in a Java Web Token inside a
cookie.  Use:
    
cromlech.sessions.jwt.JWTCookieSession

You can slso store the credentials on the file system.  Use
    https://github.com/Cromlech/cromlech.sessions.file

Or you can store the credentials in the ZODB.  USe zope.session

Thee is also [cromlech.sessions.redis](https://github.com/Cromlech/cromlech.sessions.redis) but it does not yet have a Crom branch.

And of course take a looka at [cromlech.sessions](https://github.com/Cromlech/cromlech.sessions) 

