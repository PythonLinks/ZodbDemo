from zope.schema import Text, TextLine, Password
from zope.interface import Interface
from zopache.crud.interfaces import  (IContainer,
                                      ILeaf,
                                      IRootContainer,
                                      IEditable)
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

class IItem(ITreeBase,ILeaf,IEditable):
    pass

class ICategory( IContainer,ITreeBase,IEditable):
    pass

class IRootCategory(IRootContainer,ITreeBase,IEditable):
     pass

