import sys

from django.core.exceptions import ImproperlyConfigured
from importlib import import_module

from .conf import conf



def find(name):
    for finder in finders:
        filepath = finder.find(name)
        if filepath is not None:
            return filepath

    raise ICanHazTemplateNotFound(name)



def _get_finders():
    ret = []
    for finder_path in conf.ICANHAZ_FINDERS:
        modpath, cls_name = finder_path.rsplit(".", 1)
        try:
            mod = import_module(modpath)
        except ImportError:
            e = sys.exc_info()[1]
            raise ImproperlyConfigured(
                "ImportError %s: %s" % (modpath, e.args[0]))

        try:
            cls = getattr(mod, cls_name)
        except AttributeError:
            e = sys.exc_info()[1]
            raise ImproperlyConfigured(
                "AttributeError %s: %s" % (cls_name, e.args[0]))

        ret.append(cls())

    return ret



# Instantiate finders
finders = _get_finders()



class ICanHazTemplateNotFound(Exception):
    pass
