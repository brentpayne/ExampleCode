def my_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

mod = __import__('my_package.my_module', fromlist=['my_class'])
klass = getattr(mod, 'my_class')
