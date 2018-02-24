# -*- coding: utf-8 -*-


from zope.interface import implementer
from zope.location import Location, locate
from zopache.core import Leaf, Container, RootContainer
from .interfaces import ILogin, ITreeLeaf, ITreeBranch, IRootContainer
from dolmen.container import BTreeContainer

@implementer(ITreeBranch)
class TreeBranch(Container):
    icon='zmiicons/branch.svg'
    def __init__(self, title='', body=''):
        Container.__init__(self)
        self.title = title
        self.body = body        


@implementer(ITreeLeaf)
class TreeLeaf(Leaf):
    icon='zmiicons/leaf.svg'
    def __init__(self, title='', body=''):
        Leaf.__init__(self)
        self.title = title
        self.body = body



@implementer(IRootContainer)
class Root(RootContainer):
    title = u"Zodb Crud Demo"
    body=u'This is the root of the tree.'

