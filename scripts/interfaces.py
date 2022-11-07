from abc import ABC, abstractmethod
from contextlib import AbstractAsyncContextManager

class ModelInterface(ABC):
    @abstractmethod
    def __init__(self,):
        pass

    @abstractmethod
    def load_model(self,):
        pass

    @abstractmethod
    def predict(self,):
        pass


class DataProcessingInterface(ABC):
    @abstractmethod
    def __init__(self,):
        pass
    
    @abstractmethod
    def load_data(self,):
        pass
    
    @abstractmethod
    def process_data(self,):
        pass

class EvaluatingInterface(ABC):
    @abstractmethod
    def __init__(self):
        self.metrics = []

    @abstractmethod
    def evaluate(self, true, preds):
        results = {}
        for metrics in self.metrics:
            results[metrics.__name__] = metrics(true, preds)
        return results