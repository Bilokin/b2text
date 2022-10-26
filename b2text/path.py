from b2text.modules import Module

class Path:
    def __init__(self) -> None:
        self.modules = []

    def execute(self) -> str:
        result: str = ''
        for module in self.modules:
            result += module.execute()
            result += '\n'
        return result

    def add_module(self, module: Module) -> None:
        if len(self.modules) > 0:
            module.add_previous_module(self.modules[-1])
        self.modules += [module]
