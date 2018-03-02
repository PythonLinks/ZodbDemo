Hello.
I am very glad that you want to install this package.

The first step is very easy.
git clone https://github.com/PythonLinks/ZodbDemo

I want this experience to be as nice as possible for everyone.
But that takes feedback.  Too many people just download software, and then
do not say anything.  A few days after you install it, I will ask you
how it went, but that requires your email address.

So please send me lozinski@PythonLinks.info an email, and I will give you
read permission on the required github zopache repository. 

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

I Recommend serving with Waittress.  It is from the Pyramid/Pylons
projoect, so it is quite ZODB compatible.

waitress-serve --listen=*:8080 server:application

You can now access
http://127.0.0.1:8080 on your browser.

There are 2 users created for the demo purposes:

  - username: admin, password: admin, right: manage, view
  - username: demo, password: demo, right: view

If you really want to use uwsgi, I recommend that first you
(read my notes)[./uwsgi/README].