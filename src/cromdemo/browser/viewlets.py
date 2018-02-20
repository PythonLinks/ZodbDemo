# -*- coding: utf-8 -*-

from crom import order
from crom.utils import sort_components
from dolmen.message import receive
from dolmen.viewlet import viewlet, Viewlet
from cromlech.browser import IURL, slot
from cromlech.browser.directives import title
from cromlech.security import getSecurityGuards, permissions
from cromlech.browser import IView
from . import tal_template, ITab
from .layout import SiteHeader, AdminHeader, Footer
from .layout import ContextualActions, AboveContent, Breadcrumbs
from dolmen.breadcrumbs import BreadcrumbsRenderer
import operator

@viewlet
@slot(AboveContent)
class Messages(Viewlet):

    template = tal_template('messages.pt')

    def update(self):
        self.messages = list(receive())
        self.available = bool(len(self.messages))


@viewlet
@slot(Footer)
class Footer(Viewlet):

    def render(self):
        return """
<div class='container'>

<h3>Credits</h3>
  <em>
<p>The 
<a href="https://github.com/PythonLinks/ZodbDemo#Introduction">ZODB Demo</a>
is built using the 
<a href="http://https:python.org">Python</a>&nbsp;language,&nbsp;
the object-oriented&nbsp;<a href="http://www.zodb.org/en/latest/">ZODB</a>
&nbsp;database,&nbsp;
the <a href='https://github.com/Cromlech'>Cromlech</a> toolkit, 
<a href="http://uwsgi-docs.readthedocs.io/en/latest/">uwsgi</a>,&nbsp;
<a href="https://readthedocs.org/projects/webob/">WebOb</a>, 
<a href="https://readthedocs.org/projects/zopeinterface/">Zope.Interface</a>
&nbsp;and many other libraries.&nbsp; Thanks to the innumerable open source volunteers who made this project possible.&nbsp;&copy; Christopher Lozinski 2018.&nbsp; Provided to you by <a href="http://PythonLinks.info">PythonLinks.info</a></p>
  </em>
</div>"""


@viewlet
@slot(SiteHeader)
class Cromlech(Viewlet):

    def render(self):
        baseurl = self.request.script_name
        if not baseurl.startswith('/'):
            baseurl = '/' + baseurl
        return "<h1><a href='%s'>ZODB Demo</a></h1>" % baseurl


@viewlet
@title('Logout')
@slot(SiteHeader)
@permissions('View')
class Logout(Viewlet):

    def render(self):
        return """
<div class='header-action pull-right'><a href='%s/logout'>Logout</a></div>
""" % self.request.script_name


@viewlet
@slot(AdminHeader)
class WelcomeMaster(Viewlet):
    """Greets a logged in superuser on the index.
    """
    def render(self):
        username = self.request.environment['REMOTE_USER']
        return "<p>Welcome, master %s !</p>" % username


@viewlet
@slot(Breadcrumbs)
class BreadcrumsViewlet(Viewlet):
    """Shows where we are in the tree.
    """
    def render(self):
       renderer = BreadcrumbsRenderer(self.view.context, self.request)
       renderer.update()
       return renderer.render()


def sort_key(component):
    explicit = order.get_policy(component[1], order.dotted_name, 0)
    return (explicit, component[1].__module__, component[1].__class__.__name__)


@viewlet
@slot(ContextualActions)
class Tabs(Viewlet):
    template = tal_template('tabs.pt')

    def tabs(self):
        url = IURL(self.context, self.request)
        result = []
        
        for id, view in self._tabs:
            result.append( {
                'active': self.view.__class__ is view,
                'title': title.get(view) or id,
                'url': '%s/%s' % (url, id),
            })
        result.sort(key=operator.itemgetter('title'))
        return result
    
    def update(self):
        #tabs = ITab.all_components(self.context, self.request)
        tabs=IView.all_components(self.context, self.request)
        predict, _ = getSecurityGuards()
        if predict is not None:
            tabs = (
                (name, tab) for name, tab in tabs
                if predict(tab, swallow_errors=True) is not None)

        self._tabs = sort_components(tabs, key=sort_key)
        self.available = len(self._tabs) > 0
