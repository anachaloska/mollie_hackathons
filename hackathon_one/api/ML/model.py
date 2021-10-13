import pickle

class Model:
    def __init__(self, model_path: str = None):
        self._model = None
        self._model_path = model_path
        self.load()

    def load(self):
        try:
            self.model = pickle.load(open(self._model_path, 'rb'))
        except:
            self._model = None
        return self
