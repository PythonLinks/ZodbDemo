# -*- coding: utf-8 -*-

import os

HERE = os.path.dirname(os.path.abspath(__file__))



# We setup the cache for Chameleon templates
template_cache = os.path.join(HERE, 'cache')
if not os.path.exists(template_cache):
    os.makedirs(template_cache)
os.environ["CHAMELEON_CACHE"] = template_cache

# Bootstrapping the Crom registry
from crom import monkey, implicit
monkey.incompat()
implicit.initialize()

# Read the ZCML
# This is not a mandatory stage.
# Actually, what the ZCML loading does is grok the packages
# This can be done manually, using `crom.configure`
from cromlech.configuration.utils import load_zcml
load_zcml(os.path.join(HERE, 'app.zcml'))

# Load translation
# This is needed only if we want internationalization
from cromlech.i18n import load_translations_directories
load_translations_directories()

# Adding the event dispatcher
# Use only if you have event handlers or plan to have some.
from cromlech.events import setup_dispatcher
setup_dispatcher()


def populate_db(db):
    """We create two leaves here.. We get the DB connection object.
    We need to open and to close it. It doesn't need to return anything.
    Make sure to use a transaction manager to have it correctly persisted.
    """
    import transaction
    from cromdemo.models import Root, Leaf
    from cromlech.zodb import Connection

    with Connection(db, transaction_manager=transaction.manager) as conn:
        conn = db.open()
        root = conn.root()
        if not hasattr(root,'appRoot'):        
            appRoot=Root()
            appRoot.__name__='root'
            root.appRoot=appRoot
            appRoot['green'] = Leaf('Green leaf', 'A summer leaf')        
            appRoot['yellow'] = Leaf('Yellow leaf', 'An automn leaf')
            transaction.manager.commit()


# We read the zodb conf and initialize it
from cromlech.zodb import init_db
with open('zodb.conf', 'r') as fd:
        zodb_config = fd.read()
        db = init_db(zodb_config)
        populate_db(db)



# Getting the crypto key and creating the JWT service
# We chose the JWT signed cookie for the demo
# `cromlech.sessions` proposed different backends.
# Or you can use the WSGI session middleware of your choice.
from cromlech.sessions.jwt import key_from_file
from cromlech.sessions.jwt import JWTCookieSession

key = key_from_file(os.path.join(HERE, 'jwt.key'))
session_wrapper = JWTCookieSession(key, 300)

# Create the application, including the middlewares.
from cromdemo.wsgi import demo_application
from cromlech.zodb.middleware import ZODBApp
zodb_application = ZODBApp(demo_application, db, key="zodb.connection")
application = session_wrapper(zodb_application)
