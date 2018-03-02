from zope.schema import Text, TextLine, Password
from zope.interface import Interface
from zopache.crud.interfaces import  (IEditableContainer,
                                      IEditableLeaf,
                                      IEditableRootContainer)
from cromlech.browser import IView


class ITab(IView):
    pass


class ILogin(Interface):

    username = TextLine(
        title='Username', required=True)

    password = Password(
        title='Password', required=True)


class ITreeBase(Interface):

    title = TextLine(
        title='Title', required=True)

    body = Text(
        title='Body', required=True)

class ITreeLeaf(ITreeBase,ILeaf):
    pass

class ITreeBranch( IEditableContainer,ITreeBase):
    pass

class IRootContainer(IIEditableRootContainer,ITreeBase):
     pass

