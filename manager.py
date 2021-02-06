class Manager:

    def __init__(self, _class):
        self._claas = _class

    def __str__(self):
        return f'Manager : {self._claas}'

    def search(self, **kwargs):
        results = []
        for key, value in kwargs.items():
            for obj in self._claas.object_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    results.append(obj)
        return results

    def get(self, **kwargs):
        for key, value in kwargs.items():
            for obj in self._claas.object_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    return obj
        return None
