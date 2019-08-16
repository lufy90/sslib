#!/bin/env python36
# filename: cmdmain.py
# Author: lufei
# Date: 20190327 14:01:29
# this is a sslib script

import sys

class Main():
  def __init__(self):
    self.name = sys.argv[0]
    self.args = sys.argv[2:]
    try:
      self.opt = sys.argv[1]
    except IndexError as e:
      self.opt = 'help'

  def execute(self, options):
    ''' options: class of options '''
    opts = options(self.opt, self.args)
    opts.execute()

class Options():
  def __init__(self, name, args=None):
    self.name = name
    self.args = args
    self.call_options = {
      'help': self.usage,
      'test': self.test,
      } 

  def usage(self, *args, **kwargs):
    ''' Options help '''
    print('Manuals')

  def test(self, *args, **kwargs):
    print(args)

  def execute(self):
    try:
      self.call_options[self.name](self.args)
    except KeyError as e:
      print('Unknown option: ',self.name)
      self.call_options['help'](self.args)
if __name__ == '__main__':
  main = Main()
  main.execute(Options)

