# -*- coding: utf-8 -*-


from zope.interface import implementer
from zope.location import Location, locate
from zopache.crud import Leaf, Container
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
class Root(Container):
    title = u"Demo Root"
    body=u'This is the root of the tree.'
    def __init__(self):
       BTreeContainer.__init__(self)        
       #Needed For Cut Copy Paste
       self.pasteFolder=Container()
       self.__name__='root'    
