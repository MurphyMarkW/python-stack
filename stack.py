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
    '''
    Injects the next layer.
    Calls the function.
    '''
    stack._stackmeta__TSTORE.layers.append(self)
    retval = self.func(*args,**kwargs)
    stack._stackmeta__TSTORE.layers.pop()
    return retval # TODO Wrap in a finally?

class stackmeta(type):
  '''
  Stack metaclass - gives some nice syntactical sugar.
  '''
  __STACKS = collections.defaultdict(list)
  __TSTORE = threading.local()
  __TSTORE.layers = collections.deque()

  def __getitem__(cls,key):
    return cls.__STACKS[key]

  @property
  def next(cls):
    return stackmeta.__TSTORE.layers[-1].next

class stack(object):
  '''
  A simple stack decorator.
  '''
  __metaclass__ = stackmeta

  def __init__(self,*stacks): self.stacks = stacks

  def __call__(self,func):
    for s in self.stacks:

      # Wire up the stack as it's populated.
      try: stack[s].append(layer(func,stack[s][-1]))
      except IndexError: stack[s].append(layer(func))

    # Return the original function.
    return func
