python-stack
============

A minimalistic call stack system for python using decorators.

Example:
```
  @stack('a','b')
  def base(s): pass

  @stack('a')
  @stack('a')
  def cats(s):
    print 'cat: %s' % s
    stack.next(s)

  @stack('b')
  @stack('b','c')
  def dogs(s):
    print 'dog: %s' % s
    stack['a'].next(s)
    stack.next(s)

  stack['b'].next('OMGHAI')
  dog: OMGHAI
  cat: OMGHAI
  cat: OMGHAI
  dog: OMGHAI
  cat: OMGHAI
  cat: OMGHAI
```
