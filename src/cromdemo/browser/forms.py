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
from zopache.core.baseform import Form

from zopache.core.breadcrumbs import Breadcrumbs
from zopache.crud.forms  import  AddForm 
from ..interfaces import ITab, IItem, IRootCategory, ICategory

from ..auth import Auth
from ..interfaces import  ILogin
from zopache.crud.interfaces import ILeaf, IContainer
from cromdemo.models import  Category
from cromdemo.models import  Item
from dolmen.container import IBTreeContainer, BTreeContainer
from dolmen.template import TALTemplate
from zopache.crud.interfaces import IApp

@form_component
@name('addItem')
@context(IBTreeContainer)
@target(ITab)
@title("Add Item")
@permissions('Manage')
class AddContent(AddForm):
    subTitle='Add an Item'
    implements = IApp
    interface = IItem
    ignoreContent = True
    factory=Item


@form_component
@name('addCategory')
@context(IBTreeContainer)
@target(ITab)
@title("Add Category")
@permissions('Manage')
class AddContentContainer(AddForm):
    subTitle='Add a Tree Branch'
    implements = IApp
    interface = ICategory
    ignoreContent = True
    factory=Category



    
@form_component
@name('login')
@context(Auth)
class Login(Form,Breadcrumbs):
    subTitle='Login Form'
    title="ZODB Crud Demo"
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
