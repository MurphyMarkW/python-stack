import logging
import threading
import collections

class layer(object):
  '''
  A simple stack layer.
  '''
  def __init__(self,func,next=None):
    self.func = func
    self.next = next

  def __call__(self,*args,**kwargs):
    stack._stackmeta__LOCALS.called.append(self)
    try: return self.func(*args,**kwargs)
    finally: stack._stackmeta__LOCALS.called.pop()

class stackmeta(type):
  '''
  Stack metaclass - gives some nice syntactical sugar.
  '''
  __STACKS = dict()
  __LOCALS = threading.local()
  __LOCALS.called = collections.deque()

  def __getitem__(cls,key):
    return cls.__STACKS[key]

  def __setitem__(cls,key,val):
    cls.__STACKS[key] = val

  @property
  def next(cls):
    try: return stackmeta.__LOCALS.called[-1].next
    except IndexError: return None

class stack(object):
  '''
  A simple stack decorator.
  '''
  __metaclass__ = stackmeta

  def __init__(self,stack): self.stack = stack

  def __call__(self,func):
    try: stack[self.stack] = layer(func,next=stack[self.stack])
    except KeyError: stack[self.stack] = layer(func)
    return func

  def next(self,*args,**kwargs):
    return stack[self.stack](*args,**kwargs)
