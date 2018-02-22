# -*- coding: utf-8 -*-
#This software is subject to the CV and Zope Public Licenses.

import uuid
from crom import target, order
from cromlech.browser import IURL
from cromlech.browser.exceptions import HTTPFound
from cromlech.browser.interfaces import IPublicationRoot
from cromlech.browser.directives import title
from cromlech.security import permissions
from dolmen.forms.base import Fields, FAILURE
from dolmen.forms.base import action, name, context, form_component
from dolmen.forms.base import apply_data_event
from dolmen.forms.base.errors import Error
from zope.interface import implementer, Interface

from zopache.core.breadcrumbs import Breadcrumbs
from zopache.core.baseform import Form
from zopache.crud.forms  import  AddForm 
from ..interfaces import ITab, ITreeLeaf, ITreeBranch

from ..auth import Auth
from ..interfaces import  ILogin
from zopache.crud.interfaces import ILeaf, IContainer
from cromdemo.models import  TreeBranch
from cromdemo.models import  TreeLeaf
from dolmen.container import IBTreeContainer, BTreeContainer
from dolmen.template import TALTemplate
from zopache.crud.interfaces import IApp

@form_component
@name('addLeaf')
@context(IBTreeContainer)
@target(ITab)
@title("Add Tree Leaf")
@permissions('Manage')
class AddContent(AddForm):
    label='Add a new Tree Leaf'
    implements = IApp
    interface = ITreeLeaf
    ignoreContent = True
    factory=TreeLeaf


@form_component
@name('addBranch')
@context(IBTreeContainer)
@target(ITab)
@title("Add Tree Branch")
@permissions('Manage')
class AddContentContainer(AddForm):
    label='Add a new Tree Branch'
    implements = IApp
    interface = ITreeBranch
    ignoreContent = True
    factory=TreeBranch



    
@form_component
@name('login')
@context(Auth)
class Login(Form,Breadcrumbs):
    subTitle='Login Form'
    title="ZODB Demo"
    fields = Fields(ILogin)
    ignoreContent = True
    @property
    def action_url(self):
        return self.request.url

    def acquireTitle(self):
        return "ZODB Demo"

    def breadcrumbs(self):
        return ''
    
    @action('Log me')
    def login(self):
        data, errors = self.extractData()
        if errors:
            form.errors = errors
            return FAILURE

        success = self.context.authenticate(
            data['username'], data['password'])
        if not success:
            self.errors.append(Error(
                title='Login failed',
                identifier=self.prefix,
            ))
            return FAILURE
        raise HTTPFound(self.request.url)
