from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='cromdemo',
      version=version,
      description="",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
          "Programming Language :: Python",
          ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='ZPL2.1',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['cromdemo'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'crom',
          'cromlech.browser',
          'cromlech.configuration',
          'cromlech.dawnlight',
          'cromlech.grok',
          'cromlech.i18n',
          'cromlech.location',
          'cromlech.security',
          'cromlech.webob',
          'dolmen.forms.base',
          'dolmen.forms.ztk',
          'dolmen.message',
          'dolmen.tales',
          'dolmen.template',
          'dolmen.view',
          'dolmen.viewlet',
          'setuptools',
          'zope.interface',
          'zope.location',
          'zope.schema',
      ],
      entry_points={
           'paste.app_factory': [
                'demo = cromdemo.wsgi:demo_application',
                ],
           'fanstatic.libraries': [
               'zmiicons = zopache.zmi:library',
                ],
      },
      )

