def title_class(object, title=None):

    class TitledObj(object.__class__):
        @property
        def title(self):
            return self.__title

        @title.setter
        def title(self, title):
            self.__title = title

    object.__class__ = TitledObj
    object.title = title

if __name__ == '__main__':
    class A():
        def __init__(self):
            self.a = 5
        def a_func(self):
            print 'A function : ', self.a
    a = A()
    a.a_func()
    title_class(a,'an example class')
    a.a_func()
    print a.title
    a.title = 'an awesome example'
    print a.title
