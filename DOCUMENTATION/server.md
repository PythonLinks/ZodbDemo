Here is documentation on [server.py](../server.py)
---------------------------

In server.py  is something called PythonConfiguration.
It imports config.json to create
the Python Path that the application uses to search for
Python definitions. 

So first take a look at server.py.
Server.py  defines all the things required to configure the servers.
That sets up the wsgi server, and calls the
[demo_application](./src/cromdemo/src/cromdemo/demo.py).

loader.py creates the Python Path using the files in config.json

In server.py the server is configured.
Cromlech is a toolkit.  There are many
ways to configure it.  This 
is but one possible configuration.
