# -*- coding: utf-8 -*-


from zope.interface import implementer
from zope.location import Location, locate
from zopache.crud import Leaf, Container
from .interfaces import ILogin, ITreeLeaf, ITreeBranch, IRootContainer

@implementer(ITreeBranch)
class TreeBranch(Container):

    def __init__(self, title='', body=''):
        Container.__init__(self)
        self.title = title
        self.body = body        


@implementer(ITreeLeaf)
class TreeLeaf(Leaf):

    def __init__(self, title='', body=''):
        Leaf.__init__(self)
        self.title = title
        self.body = body



@implementer(IRootContainer)
class Root(TreeBranch):
    title = u"Demo Root"

