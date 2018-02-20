# -*- coding: utf-8 -*-

from os import path
from cromlech.browser import IView
from cromlech.webob.response import Response
from dolmen.template import TALTemplate
from dolmen.view import View, make_layout_response
from dolmen.forms.base import Form as BaseForm
from cromlech.location import get_absolute_url


TEMPLATE_DIR = path.join(path.dirname(__file__), 'templates')


def tal_template(name):
    return TALTemplate(path.join(TEMPLATE_DIR, name))


class ITab(IView):
    pass


class Form(BaseForm):
    responseFactory = Response
    make_response = make_layout_response
    template = tal_template('form.pt')

    def bootstrap_widgets(self):
        """Adds the needed css classes for bootstrap styles.
        """
        for widget in self.fieldWidgets:
            widget.defaultHtmlClass.append('form-control')
            yield widget


class Page(View):
    responseFactory = Response
    make_response = make_layout_response
    title = 'ZODB Demo'

    def url(self, *args):
          if len(args)==0:
               return get_absolute_url(self.context, self.request)
          else:
               return  get_absolute_url((args)[0], self.request)

    def objectHref(self,obj,name):
        return self.href(self.url(obj),name)
    
    def href(self,url,name):
           result ='<a href=\"'
           result += url
           result+='\">'
           if name != None:
              result += name
           result +='</a>'
           return result

class ErrorPage(Page):
    code = 400

    def make_response(self, *args, **kws):
        response = make_layout_response(self, *args, **kws)
        response.status_code = self.code
        return response
