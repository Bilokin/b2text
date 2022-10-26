from b2text.path import Path
import b2text.modules as modules

def stdK(*args, **kw_args):
    module = modules.FillStdParticleListModule(*args, **kw_args)
    kw_args['path'].add_module(module)

def stdPi(*args, **kw_args):
    module = modules.FillStdParticleListModule(*args, **kw_args)
    kw_args['path'].add_module(module)

def stdMu(*args, **kw_args):
    module = modules.FillStdParticleListModule(*args, **kw_args)
    kw_args['path'].add_module(module)

def stdE(*args, **kw_args):
    module = modules.FillStdParticleListModule(*args, **kw_args)
    kw_args['path'].add_module(module)

def stdPr(*args, **kw_args):
    module = modules.FillStdParticleListModule(*args, **kw_args)
    kw_args['path'].add_module(module)