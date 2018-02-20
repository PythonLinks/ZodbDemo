# -*- coding: utf-8 -*-

from crom import target, order
from dawnlight.core import ResolveError
from dolmen.message import send
from dolmen.view import name, context, view_component
from cromlech.browser.exceptions import HTTPFound
from cromlech.security import Unauthorized
from zope.interface import Interface
from zope.interface.interfaces import ComponentLookupError
from dolmen.container import IBTreeContainer
from . import tal_template, ITab, Page, ErrorPage
from ..models import Root, Leaf
from cromdemo.interfaces import IRootContainer
from ..auth import logout
from cromlech.browser.directives import title

@view_component
@name('logout')
@context(Interface)
class Logout(Page):
    
    def update(self):
        logout()

    def render(self):
        send('You have been logged out.')
        raise HTTPFound(location='/')


@view_component
@name('index')
@title('View')
@context(IBTreeContainer)
class RootIndex(Page):
    title='ZODB Demno'
    subTitle='View a Branch'
    template = tal_template('home.pt')

@view_component
@name('index')
@target(ITab)
@context(Leaf)
@order(10)
class LeafIndex(Page):
    template = tal_template('leaf.pt')
    subTitle='View a Leaf'
    title='ZODB Demno'

@view_component
@name('')
@context(Unauthorized)
class NoAccess(ErrorPage):
    code = 403

    def render(self):
        return "No access for you !"


@view_component
@name('')
@context(ResolveError)
class NotFound(ErrorPage):
    code = 404

    def render(self):
        return """<h1>
  <i class="glyphicon glyphicon-ban-circle"></i> Not found
</h1>
<p>The resource was not found !</p>
"""
