from werkzeug.wrappers import Request as BaseRequest

class Request(BaseRequest):

    _params = {}

    _data = {}

    _input = {}

    def __init__(self, *args, **kwargs):
        super(Request, self).__init__(*args, **kwargs)
        self.build_input()
        self.headers = dict(self.headers)

    def build_input(self):
        self._params = self.args.to_dict()
        self._data = self.form.to_dict()
        self._input = self._params
        self._input.update(self._data)

    def input(self, key, default=None):
        if key in self._input:
            return self._input[key]
        return default

    def has(self, key):
        return key in self._input

    def file(self, key):
        if key in self.files:
            return self.files[key]
        return None

    def all(self):
        return self._input

    def header(self, key, default=None):
        if key in self.headers:
            return self.headers[key]
        return None

    def __str__(self):
        return '<Request {} {}>'.format(self.method, self.path)




