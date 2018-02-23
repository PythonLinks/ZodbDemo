Support python3.4+ only


Deployment
----------

```bash
$> pyvenv . && source bin/activate
$> pip install -U pip setuptools
$> pip install -r requirements.txt
$> pip install -e .
```



To serve with `uwsgi`:

```bash
$> uwsgi --http :8080 --wsgi-file app.py
```
You may want to use the following wsgi options.
--honour-stdin
Allows you to  run a debugger on  the uwsgi.
it will allow you to use PDB without problems.

You could also server with waitress or gunicorn.

Using one of the servers as described above, You can now access
http://127.0.0.1:8080 on your browser.

There are 2 users created for the demo purposes:

  - username: admin, password: admin, right: manage, view
  - username: demo, password: demo, right: view

