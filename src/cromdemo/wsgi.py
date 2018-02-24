# -*- coding: utf-8 -*-

from cromlech.browser.interfaces import IView
from cromlech.dawnlight import DawnlightPublisher
from cromlech.dawnlight import ViewLookup, view_locator
from cromlech.i18n import EnvironLocale
from cromlech.security import ContextualInteraction
from cromlech.security import ContextualSecurityGuards
from cromlech.security import security_check, security_predication
from cromlech.security import unauthenticated_principal as anonymous
from cromlech.webob.request import Request
from cromlech.browser import setSession

from .models import TreeLeaf, Root ,TreeBranch
from .auth import Auth, secured
from .security import secure_query_view



# Auth serves as a context for the `Login` form.
# It behaves like a dict but has an additional `authenticate` method
# used by the form.
auth = Auth({
    'demo': 'demo',
    'admin': 'admin',
})


# The publisher is a 2 times component that is in charge of looking up
# the model and the view, given an URL.
# It relies on traversers to handle the publishing.
# Here, we provide a custom way to retrieve views, using a security-aware
# function.
# See `dawnlight` and `cromlech.dawnlight` for more information.
publisher = DawnlightPublisher(
    view_lookup=ViewLookup(view_locator(secure_query_view)),
).publish


class Session(object):

    def __init__(self, session):
        self.session = session

    def __enter__(self):
        setSession(self.session)
        return self.session

    def __exit__(self, type, value, traceback):
        # Traceback or not, we reset the session thread-local.
        # Exiting the block, we don't want the session set.
        self.session = None  # Remove the reference.
        setSession()


@secured
def publish(environ, start_response, principal):

    # We instanciate an IRequest object.
    # Here, we use WebOB but you can implement your own
    # or adapt the one of your liking.
    # It will be use by all the browser component and the publishing
    # process.
    request = Request(environ)
    conn = environ["zodb.connection"]
    root=conn.root()
    root=root.appRoot

    #When serving behind a web server, we need to fix up the application_url
    if 'Host' in request.headers:
        request.host=request.headers['Host']
    
    #When serving behind an NGINX server,
    #the url is changed, so fix it
    import pdb;pdb.set_trace()
    if hasattr(request,'Host'):
       request.application_url = request.Host
  
    
    # The `Interaction` serves as the "who" in the security model.
    # The security model relies on 2 elements : the "who" and the "how".
    # The "how" is provided by the security guards declared with the
    # ContextualSecurityGuards context manager, in the `demo_application`
    # function.
    with ContextualInteraction(principal):

        if principal is anonymous:
            # This is a simple usecase of "members-only" for the demo :
            # We do not want anonymous users.
            # But we could continue and rely on the security checks to raise
            # security errors and redirect on the login form.
            login = IView.adapt(auth, request, name='login')
            login.update()
            return login()
        else:
            # The user is authenticated, we can call the publisher to
            # traverse and publish our objects.
            return publisher(request, root)


def demo_application(environ, start_response):
    # Security guards are the security context of the application
    # They have 2 layers : predicate and checks.
    # This context is thread-bound.
    # See `cromlech.security` documentation for more information.
    with ContextualSecurityGuards(security_predication, security_check):

        # We retrieve the session set by the session middleware and
        # persisted in the environ. We set it globally in the thread.
        # This will allow the authentication to make use of it.
        with Session(environ['session']):

            # We set the language of the application, extracting the
            # language preferences from the browser request.
            # See `cromlech.i18n` for more information.
            with EnvironLocale(environ):

                # We call our publishing function.
                # We provide a default user that can be overriden
                # by the `secured` decorator that will extract the
                # cached user from the session.
                response = publish(environ, start_response, anonymous)

                # We cook the WSGI response and return it.
                # Our application ends here.
                return response(environ, start_response)
