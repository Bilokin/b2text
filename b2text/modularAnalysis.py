from b2text.path import Path
import b2text.modules as modules

def inputMdst(*args, **kwargs):
    module = modules.BlankModule(*args, **kwargs)
    kwargs['path'].add_module(module)

def cutAndCopyList(*args, **kwargs):
    module = modules.BlankModule(*args, **kwargs)
    kwargs['path'].add_module(module)

def variablesToNtuple(*args, **kwargs):
    module = modules.BlankModule(*args, **kwargs)
    kwargs['path'].add_module(module)

def reconstructDecay(*args, **kwargs):
    module = modules.ReconstructDecayModule(*args, **kwargs)
    kwargs['path'].add_module(module)