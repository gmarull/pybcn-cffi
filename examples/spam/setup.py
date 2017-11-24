from distutils.core import setup, Extension

spammodule = Extension('spam', sources = ['spam.c'])

setup (name = 'Spam',
       version = '1.0',
       ext_modules = [spammodule])
