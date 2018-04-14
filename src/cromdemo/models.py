# -*- coding: utf-8 -*-

from zope.interface import implementer
from zopache.core import Leaf, Container, RootContainer
from .interfaces import ILogin, IItem, ICategory, IRootCategory

@implementer(ICategory)
class Category(Container):
    icon='zmiicons/branch.svg'
    def __init__(self, title='', body=''):
        Container.__init__(self)
        self.title = title
        self.body = body        


@implementer(IItem)
class Item(Leaf):
    icon='zmiicons/leaf.svg'
    def __init__(self, title='', body=''):
        Leaf.__init__(self)
        self.title = title
        self.body = body



@implementer(IRootCategory)
class RootCategory(RootContainer):
    title = u"Category Demo"
    body=u'This is the root of the category tree.'

