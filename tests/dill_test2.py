#!/usr/bin/env python
"""
demonstrate dill's ability to pickle different python types
"""

import dill as pickle
#pickle._trace(True)
#import pickle

typelist = []

# testing types
_none = None; typelist.append(_none)
_type = type; typelist.append(_type)
_bool = bool(1); typelist.append(_bool)
_int = int(1); typelist.append(_int)
_long = long(1); typelist.append(_long)
_float = float(1); typelist.append(_float)
_complex = complex(1); typelist.append(_complex)
_string = str(1); typelist.append(_string)
_unicode = unicode(1); typelist.append(_unicode)
_tuple = (); typelist.append(_tuple)
_list = []; typelist.append(_list)
_dict = {}; typelist.append(_dict)
_file = file; typelist.append(_file)
_buffer = buffer; typelist.append(_buffer)
_builtin = len; typelist.append(_builtin)
class _class:
    def _method(self):
        pass
class _newclass(object):
    def _method(self):
        pass
typelist.append(_class)
typelist.append(_newclass) # <type 'type'>
_instance = _class(); typelist.append(_instance)
_object = _newclass(); typelist.append(_object) # <type 'class'>
_object2 = object(); typelist.append(_object2)
_set = set(); typelist.append(_set)
_frozenset = frozenset(); typelist.append(_frozenset)
import array; _array = array.array("f"); typelist.append(_array)
def _function2():
    try: raise
    except:
      from sys import exc_info
      e, er, tb = exc_info()
      return er, tb
_exception = _function2()[0]; typelist.append(_exception)
def _function(x): yield x; typelist.append(_function)
# pickle fails on all below here -------------------------------------------
_traceback = _function2()[1]; typelist.append(_traceback)
_lambda = lambda x: lambda y: x; typelist.append(_lambda)
_cell = (_lambda)(0).func_closure[0]; typelist.append(_cell)
_method = _class()._method; typelist.append(_method)
_ubmethod = _class._method; typelist.append(_ubmethod)
_module = pickle; typelist.append(_module)
_code = compile('','','exec'); typelist.append(_code)
_dictproxy = type.__dict__; typelist.append(_dictproxy)
_dictprox2 = _newclass.__dict__; typelist.append(_dictprox2)
_methoddescrip = type.__dict__['mro']; typelist.append(_methoddescrip)
import array; _getsetdescrip = array.array.typecode; typelist.append(_getsetdescrip)
import datetime; _membdescrip = datetime.timedelta.days; typelist.append(_membdescrip)
_memdescr2 = type.__dict__['__weakrefoffset__']; typelist.append(_memdescr2)
_wrapperdescrip = type.__repr__; typelist.append(_wrapperdescrip)
_wrapdescr2 = type.__dict__['__module__']; typelist.append(_wrapdescr2)
_generator = _function(1); typelist.append(_generator)
_frame = _generator.gi_frame; typelist.append(_frame)
_xrange = xrange(1); typelist.append(_xrange)
_slice = slice(1); typelist.append(_slice)
_nimp = NotImplemented; typelist.append(_nimp)
_ellipsis = Ellipsis; typelist.append(_ellipsis)
try:
  __IPYTHON__ is True # is ipython
except NameError:
  _quitter = quit; typelist.append(_quitter)
#_property = property()
#_super = super(type)
#_staticmethod = staticmethod(0)
#_classmethod = ???
#_bytearray = bitearray([0])
#_memoryview = ???
#_array = array.array('i')
try:
  from numpy import ufunc as _numpy_ufunc
  typelist.append(_numpy_ufunc)
  from numpy import array as _numpy_array
  typelist.append(_numpy_array)
  from numpy import int32 as _numpy_int32
  typelist.append(_numpy_int32)
except ImportError:
  pass
#---------------
import weakref
_ref = weakref.ref(_instance); typelist.append(_ref)
##_deadref = weakref.ref(_class()); typelist.append(_deadref)
#_proxy = weakref.proxy(_instance); typelist.append(_proxy)
##_deadproxy = weakref.proxy(_class()); typelist.append(_deadproxy)
class _class2:
    def __call__(self):
        pass
_instance2 = _class2()
#_callable = weakref.proxy(_instance2); typelist.append(_callable)
##_deadcallable = weakref.proxy(_class2()); typelist.append(_deadcallable)
#---------------
#_dictitemiter = type.__dict__.iteritems()
#_defaultdict = collections.defautdict()
#_deque = collections.deque([0])
#---------------


if __name__ == '__main__':

  def pickles(x):
    #print type(x)
    try:
      p = pickle.loads(pickle.dumps(x))
      try:
        assert x == p
      except AssertionError, err:
        assert type(x) == type(p)
        print "weak: %s" % type(x)
    except (TypeError, pickle.PicklingError), err:
      print "COPY failure: %s" % type(x)
    return

  for member in typelist:
     #print "%s ==> %s" % (member, type(member)) # DEBUG
      pickles(member)
  for member in typelist:
     #print "%s ==> %s" % (member, type(member)) # DEBUG
      try:
          pickle.loads(pickle.dumps(member))
      except:
          print "PICKLE failure: %s" % type(member)

