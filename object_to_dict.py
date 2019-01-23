# -*- coding: utf-8 -*-
# @Time    : 19-1-21 下午10:16
# @Author  : ccs
from django.db.models import sql
from django.db.models.expressions import SQLiteNumericMixin, Expression
from django.db.models.query import ModelIterable


class ObjectToDict(object):
    def __init__(self, model=None, query=None, using=None, hints=None):
        self.model = model
        self._db = using
        self._hints = hints or {}
        self.query = query or sql.Query(self.model)
        self._result_cache = None
        self._sticky_filter = False
        self._for_write = False
        self._prefetch_related_lookups = ()
        self._prefetch_done = False
        self._known_related_objects = {}  # {rel_field: {pk: rel_obj}}
        self._iterable_class = ModelIterable
        self._fields = None

    def _clone(self):
        """
        Return a copy of the current QuerySet. A lightweight alternative
        to deepcopy().
        """
        #可见，这样可以将本类初始化参数全部赋给c对象，作为c的属性
        c = self.__class__(model=self.model, query=self.query.chain(), using=self._db, hints=self._hints)
        c._sticky_filter = self._sticky_filter
        c._for_write = self._for_write
        c._prefetch_related_lookups = self._prefetch_related_lookups[:]
        c._known_related_objects = self._known_related_objects
        c._iterable_class = self._iterable_class
        c._fields = self._fields
        return c


    ####obj对象通过.__dict__转换成字典

    def _chain(self, **kwargs):
        """
        Return a copy of the current QuerySet that's ready for another
        operation.
        """
        obj = self._clone()
        if obj._sticky_filter:
            obj.query.filter_is_sticky = True
            obj._sticky_filter = False
        obj.__dict__.update(kwargs)
        return obj



###super初始化
class Func(SQLiteNumericMixin, Expression):
    """An SQL function call."""
    function = None
    template = '%(function)s(%(expressions)s)'
    arg_joiner = ', '
    arity = None  # The number of arguments the function accepts.

    def __init__(self, *expressions, output_field=None, **extra):
        if self.arity is not None and len(expressions) != self.arity:
            raise TypeError(
                "'%s' takes exactly %s %s (%s given)" % (
                    self.__class__.__name__,
                    self.arity,
                    "argument" if self.arity == 1 else "arguments",
                    len(expressions),
                )
            )
        super().__init__(output_field=output_field)
        self.source_expressions = self._parse_expressions(*expressions)
        self.extra = extra


class Aggregate(Func):
    contains_aggregate = True
    name = None
    filter_template = '%s FILTER (WHERE %%(filter)s)'
    window_compatible = True

    def __init__(self, *args, filter=None, **kwargs):
        self.filter = filter#将非公共参数直接在当前初始化
        super().__init__(*args, **kwargs)##将公共参数放到基类初始化，



if __name__ == '__main__':
    o_t_d =ObjectToDict()
    c = o_t_d._clone()
    print(c.__dir__())
    print(c.__dict__)