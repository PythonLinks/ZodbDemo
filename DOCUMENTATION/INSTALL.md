Installation instructions with Explanation
========================

These are installation instructions assuming that you have a debian server.
Python 3.4+ required.

First the commands, then explanations.

bash
git clone https://github.com/PythonLinks/Demo
cd ZodbDemo
virtualenv -p /usr/bin/python3 .
source bin/activate
python bootstrap.py
bin/buildout
pip install uwsgi
uwsgi --http :8081 -p1 --honour-stdin --static-map2 /favicon.ico=./favicon.ico --wsgi-file server.py

And then the username:password is admin:admin

If you do not have Python3.4 installed, probably best to use pyenv to install it.

Here is how to install venv.
$>curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
$>pyenv install 3.4.2

Read more at
https://docs.python.org/3/library/venv.html


First fire up bash, then get a copy of the git repository.

```
$>bash
$> git clone https://github.com/PythonLinks/CromlechDemo
```

Now we install a virtual env.

If your server's main python in python3.3+

```
$> pyvenv .
$> source bin/activate
```

#  OR WHAT I HAD TO DO ON LINUX WHERE THE DEFAULT PYTHON IS 2.something
```
$>virtualenv -p /usr/bin/python3 .
$> source bin/activate
```

When you first download this there is a file in the root called bootstrap.py.
you run
```
$>python bootstrap.py 
```
to create bin/buildout.

Then you run
```
$>bin/buildout
```

, it downlaods all the required software, and creates
all the files and directories needed to run the application.
In particular it creates config.json, which includes all the Python Path
information.

$>pip install uwsgi

And now we run the application.
```
$> uwsgi --http :8080 --static-map2 /favicon.ico=./favicon.ico --wsgi-file server.py
```

--honour-stdin
Allows you to  run a debugger on  the uwsgi.
it will allow you to use PDB without problems.

-p 1
Sets the number of processes.

--static-map2 /favicon.ico=./favicon.ico
Serves the favicon.ico.  The problem is without this
you will see more error messages which interfere with development.

Here is the command I use. 
 uwsgi --http :8081  -p1  --static-map2 /favicon.ico=./favicon.ico --honour-stdin --wsgi-file server.py

Note that port 8081 works for me, you may want a different port number.

And when you download a new versoin use the commands
```
$>bin/develop update
```
to update all the packages which have been downloaded.

And of coures in the unlikely event that  you install multiple times,
then your browser gets a key, but the server key is different.
So you get a jwt error. 