#!/bin/env python36
# filename: ssautolib.py
# Author: lufei
# Date: 20190829 10:00:03


import pkgutil
import sys
import importlib
import os

def get_sub(pkg_name, sub_modules):
  '''get a list of all modules in pkg_name, sub_modules should be a empty list. '''
  try:
    pkg = importlib.import_module(pkg_name)
    for _, sub_name, ispkg in pkgutil.iter_modules(pkg.__path__):
      if ispkg:
        get_sub(pkg.__name__+'.'+sub_name, sub_modules)
      else:
        sub_modules.append(importlib.import_module(pkg.__name__+'.'+sub_name))

  except Exception as e:
    print(type(e).__name__, e)

def get_subclass(module, baseclass):
  '''get all sub classes of baseclass from module even those in sub modules, 
module is a package object, baseclass is the base class'''
  try:
    if hasattr(module, '__path__'):
      # module is a package object
      sub_modules = []
      get_sub(module.__name__, sub_modules)   # get sub only accept strings.
      sub_class = []
      for mod in sub_modules:
        sub_class.append(get_tests(mod))
      return sub_class
    else:
      return [x for x in vars(module).values() if ssissubclass(x,baseclass)] 
  except Exception as e:
    print(e)
    return []

def ssissubclass(a,b): 
  '''tell if a is subclass of b'''
  try:
    return issubclass(a,b)
  except TypeError:
    return False

def get_module_names_by_path(path, prefix=''):
  '''get a list of all modules in path'''
  module_names = []

  def _get_module(subpath, prefix, module_names):
    for md in pkgutil.iter_modules(path=subpath, prefix=prefix):
      if md[2]:
        _get_module(os.path.join(subpath, md[1]), md[1]+'.', module_names)
      else:
         module_names.append(md[1])
  _get_module(path, prefix, module_names)
  return module_names



def get_module_names_by_path__(path):
  '''get a list of all modules in path'''
  path = os.path.abspath(path)
  module_names = []
  try:
    files = os.listdir(path)
  except Exception as e:
    print(type(e).__name__, e)
    return []
  for i in files:
    if i[-3:] == '.py' or os.path.isdir(os.path.join(path,i)):
      module_names.append(i)
    elif i[0] != '_' and os.path.isdir(os.path.join(path,i)):
      module_names.append(i)
    else:
      pass

  return module_names

def get_modules_by_path__(path):
  '''get a list of all modules in path'''
#  while path[-1] == '/':
  path = os.path.abspath(path)
  dpath = os.path.dirname(path)
  bpath = os.path.basename(path)
  sys.path.insert(0, dpath)
  sub_modules = []
  get_sub(bpath, sub_modules)
  sys.path.pop(0)
  return sub_modules

