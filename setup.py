from setuptools import setup, find_packages
import os

version = '1.1dev'

tests_require = [
    'zope.app.authentication',
    'zope.app.testing',
    'zope.app.zcmlfiles',
    'zope.configuration',
    'zope.securitypolicy',
    'zope.testbrowser',
    ]

setup(name='zeam.form.viewlet',
      version=version,
      description="zeam.form forms in a viewlet",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='zeam form viewlet',
      author='Sylvain Viollon',
      author_email='thefunny@gmail.com',
      url='http://pypi.python.org/pypi/zeam.form.viewlet',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['zeam', 'zeam.form'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'zeam.form.base',
        'grokcore.viewlet',
        'megrok.pagetemplate',
        ],
      tests_require = tests_require,
      extras_require = {'test': tests_require},
      )
