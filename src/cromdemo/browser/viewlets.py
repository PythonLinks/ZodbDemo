# -*- coding: utf-8 -*-

from crom import order
from crom.utils import sort_components
from dolmen.message import receive
from dolmen.viewlet import viewlet, Viewlet
from cromlech.browser import IURL, slot
from cromlech.browser.directives import title
from cromlech.security import getSecurityGuards, permissions

from . import tal_template, ITab
from .layout import SiteHeader, AdminHeader, Footer
from .layout import ContextualActions, AboveContent


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
  <em>
    <a href='https://github.com/Cromlech'>Browse the cromlech repository</a>
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


def sort_key(component):
    explicit = order.get_policy(component[1], order.dotted_name, 0)
    return (explicit, component[1].__module__, component[1].__class__.__name__)


@viewlet
@slot(ContextualActions)
class Tabs(Viewlet):
    template = tal_template('tabs.pt')

    def tabs(self):
        url = IURL(self.context, self.request)
        for id, view in self._tabs:
            yield {
                'active': self.view.__class__ is view,
                'title': title.get(view) or id,
                'url': '%s/%s' % (url, id),
            }

    def update(self):
        tabs = ITab.all_components(self.context, self.request)
        predict, _ = getSecurityGuards()
        if predict is not None:
            tabs = (
                (name, tab) for name, tab in tabs
                if predict(tab, swallow_errors=True) is not None)

        self._tabs = sort_components(tabs, key=sort_key)
        self.available = len(self._tabs) > 0
