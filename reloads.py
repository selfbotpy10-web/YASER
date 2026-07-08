# reloads.py

def reload_module(module):
    from importlib import reload
    return reload(module)
