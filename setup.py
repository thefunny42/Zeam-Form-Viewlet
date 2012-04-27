from setuptools import setup, find_packages
import os

version = '1.2.1'

tests_require = [
    'zope.app.wsgi',
    'zope.testing',
    'zeam.form.base [test]',
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
        'grokcore.component',
        'grokcore.view',
        'grokcore.viewlet',
        'grokcore.chameleon',
        'martian',
        'megrok.pagetemplate',
        'setuptools',
        'zeam.form.base >= 1.0',
        ],
      tests_require = tests_require,
      extras_require = {'test': tests_require},
      )
