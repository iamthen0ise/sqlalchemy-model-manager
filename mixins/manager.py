""" Active record mixin
"""

from mixins.session import SessionBinderMixin


class ActiveRecordMixin(SessionBinderMixin):
    """Active Record Mixin
    """
    __abstract__ = True

    def _set(self, **kwargs):
        for col in kwargs.keys():
            setattr(self, col, kwargs[col])
        return self

    def save(self):
        self.session.add(self)
        self.session.commit()
        return self

    @classmethod
    def create(cls, **kwargs):
        return cls()._set(**kwargs).save()

    def update(self, **kwargs):
        return self._set(**kwargs).save()

    def delete(self):
        self.session.delete(self)
        self.session.flush()
