from zope.schema import Text, TextLine, Password
from zope.interface import Interface
from zopache.crud.interfaces import  IContainer, ILeaf
from cromlech.browser import IView
from cromlech.browser.interfaces import IPublicationRoot

class ITab(IView):
    pass


class ILogin(Interface):

    username = TextLine(
        title='Username', required=True)

    password = Password(
        title='Password', required=True)


class ITreeLeaf(ILeaf):

    title = TextLine(
        title='Title', required=True)

    body = Text(
        title='Body', required=True)

class ITreeBranch( IContainer,ITreeLeaf):
    pass

class IRootContainer(IPublicationRoot,ITreeBranch):
     pass

