def show_me(instance):
    class_name = instance.__class__.__name__
    attrs = sorted((vars(instance).keys()))
    inst_attrs_names = ', '.join(attrs[:-1]) + f' and {attrs[-1]}' if len(attrs) > 1 else attrs[0]

