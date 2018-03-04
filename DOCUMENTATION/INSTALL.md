Hello.
I am very glad that you want to install this package.
The instructions are below.

First I ask you to send me. lozinski@PythonLinks.info
an email.  And say
a few words aout why you are interested in the ZODB.


The rest of the directions follow.


Support python3.4+ only

Deployment
----------

```bash
$> pyvenv . && source bin/activate
$> pip install -U pip setuptools
$> pip install -r requirements.txt
$> pip install -e .
```
And then to run the debugging version.
./serve dev
To stop the development version
type ctrl-c ^c

To run the daemon
./serve daemon

To stop the deamon:
./serve stop


There are 2 users created for the demo purposes:

  - username: admin, password: admin, right: manage, view
  - username: demo, password: demo, right: view

If you really want to use uwsgi, I recommend that first you
(read my notes)[./uwsgi/README].