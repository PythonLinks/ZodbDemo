import crom
from zopache.ttw.interfaces import IURLSegment
from ./interfaces import ITreeBase

@crom.adapter
@crom.sources(ITreeBase)
@crom.target(IURLSegment)
class IDemoAdaptor(object):
    def __init__(self,context):
        self.context=context
        
    def getSegment(self):
        return 'edit'
