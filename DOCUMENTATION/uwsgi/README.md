I tried using uwsgi.
I tried hard. It is well knowne, Ithought, great.  I should use it.
But it did not work.  Why did it not work?  Not sure.
It worked fine in development mode, but when I tried to run
it as a daemon, every second request would partially fail.
It could not find the object, but returend the surrounding
layout just fine.

And I had ohter problems with uwsgi.  Too many options.
Not clear error messages.  The app would fail, or not laod,
but hte uwsgi would keep running.

When I mentioned it to my mentor, he sympathised, as if he had had the same
problems. 

No point trying to fix it.

So I moved to Waitress. That is the first one mentioned
in Cromlech/cromdemo. And it the documentation
is over on the Pyramid Pylons page, so it must be ZODB compatile. 

Here are my notes on trying to use uwsgi.
 
To serve with `uwsgi`:

```bash
$> uwsgi --http :8080 --wsgi-file server.py
'''

You may want to use the following wsgi options.
--honour-stdin
Allows you to  run a debugger on  the uwsgi.
it will allow you to use PDB without problems.


You could also server with waitress or gunicorn.