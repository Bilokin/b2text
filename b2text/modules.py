import abc 
import inspect

PARTICLE_TEXT_TYPES = {'K': 'charged kaon',
                  'pi': 'charged pion',
                  'mu': 'muon',
                  'e': 'electron',
                  'p': 'proton',
                  'anti-p': 'anti-proton',
                  'pi0': 'neutral pion',
                  'D0': 'neutral D-meson',
                  'D*+': 'charged D*-meson',
                  'D*-': 'charged D*-meson'
}

PARTICLE_SYMBOL_TYPES = {'K': '$K$',
                  'pi': '$\pi$',
                  'mu': '$\mu$',
                  'e': '$e$',
                  'p': '$p$',
                  'anti-p': '$\bar{p}$',
                  'pi0': '$\pi^0$',
                  'D0': '$D^0$'
}

class Module(abc.ABC):
    def __init__(self, *args, **kw_args) -> None:
        self.args = args
        self.kw_args = kw_args
        cframe = inspect.currentframe()
        self.func = inspect.getframeinfo(cframe.f_back.f_back).function
        self.alternate = False

    def add_previous_module(self, last_module) -> None:
        self.previous_module = last_module
        if isinstance(last_module, self.__class__):
            self.alternate = True

    def get_particle_type(self, particle_list_name: str) -> str:
        for id in PARTICLE_TEXT_TYPES:
            if particle_list_name.startswith(id):
                return PARTICLE_TEXT_TYPES[id]
        return particle_list_name.split(':')[0]

    @abc.abstractmethod
    def execute(self) -> str:
        pass

class BlankModule(Module):
    def __init__(self, *args, **kw_args) -> None:
        super().__init__(*args, **kw_args)
        self.name = f'%{self.func}({args, kw_args})'

    def execute(self) -> None:
        return self.name

class SelectionCutModule(Module):
    def __init__(self, *args, **kw_args) -> None:
        super().__init__(*args, **kw_args)
        p_list = args[0]

    def execute(self) -> None:
        return self.name

class ReconstructDecayModule(Module):
    def __init__(self, *args, **kw_args) -> None:
        super().__init__(*args, **kw_args)
        self.decay_string = args[0]
        self.cut = args[1]

    def execute(self) -> None:
        from ROOT import Belle2
        decayDescriptor = Belle2.DecayDescriptor()
        if not decayDescriptor.init(self.decay_string):
            raise ValueError("Invalid decay string")
        mother_name = self.get_particle_type(decayDescriptor.getMother().getName())
        daughter_names = []
        ndaughters = decayDescriptor.getNDaughters()
        for i in range(0, ndaughters):
            daughter_names += [self.get_particle_type(decayDescriptor.getDaughter(i).getMother().getName())]
        result = f'We reconstruct the {mother_name} candidates by combining '
        if self.alternate:
            result = f'The {mother_name} candidates are reconstructed by combining '

        if ndaughters > 2:
            for i in range(0, ndaughters-2):
                result += daughter_names[i]
                result += ', '
        result += daughter_names[ndaughters-2] + ' and ' + daughter_names[ndaughters-1]
        result += ' candidates and '
        if not self.cut:
            result += 'applying no selection criteria.'
        else:
            split_cuts = self.cut.split(' and ')
            if len(split_cuts) == 1:
                result += f'applying ${split_cuts[0]}$ selection cut.'
            else:
                result += 'applying the following cuts:\n'
                result += '\\begin{itemize}\n'
                for cut in split_cuts:
                    result += f'    \\item ${cut}$\n'
                result += '\\end{itemize}\n'

        return result

class FillStdParticleListModule(Module):
    def __init__(self, *args, **kw_args) -> None:
        super().__init__(*args, **kw_args)
        self.func_types = {'stdK': 'kaon', 
                 'stdPi': 'pion',
                 'stdMu': 'muon',
                 'stdE': 'electron',
                 'stdPr': 'proton',
        }
        self.name = args[0]
        

    def execute(self) -> None:
        header = f'We select the {self.func_types[self.func]} particles using standard criteria "{self.name}", which is defined within the Belle II software.'
        if self.alternate:
            header = f'The {self.func_types[self.func]} particles are selected using "{self.name}" criteria'
            if self.previous_module.name == self.name:
                header += ' as well.'
            else:
                header += '.'
        return header