from abc import abstractmethod, ABC
import uuid


class Plugin(ABC):
    def __init__(self, name: str, base_url="", credentials={}):
        self.name = name
        self.base_url = base_url
        self.credentials = credentials
        self.id = str(uuid.uuid4())

    @abstractmethod
    def execute(self):
        raise NotImplementedError()
