python-stack
============

A minimalistic call stack system for python using decorators.

Example:
```
  from stack import stack

  @stack('a')
  @stack('b')
  def base(s): pass

  @stack('a')
  def cat(s):
    print 'meow: %s' % s
    stack.next(s)

  @stack('b')
  def dog(s):
    print 'woof: %s' % s
    stack('a').next(s)
    stack.next(s)

  stack('a').next('HAI')
  meow: HAI

  stack('b').next('BAI')
  woof: BAI
  meow: BAI
```
