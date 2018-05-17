# mixins/session.py
""" This module provides Session binding and access
"""
from utils.classproperty import classproperty


class SessionBinderMixin:
    """ Binds session access to model class
    """
    _session = None

    @classmethod
    def bind_session(cls, session):
        """Binds session to model"""
        cls._session = session

    @classproperty
    def session(cls):
        """Class property for direct session access
        """
        if not cls._session:
            raise RuntimeError('No Model Implement')
        return cls._session

    @classproperty
    def objects(cls):
        """Provides simple Model manager interface
        i.e. Django-styled Model.objects
        """
        return cls.session.query(cls)
