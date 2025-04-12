from abc import abstractmethod, ABC


class Plugin(ABC):
    def __init__(self, name):
        pass

    @abstractmethod
    def execute(self):
        pass
