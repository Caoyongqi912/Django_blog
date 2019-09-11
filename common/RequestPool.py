import requests


class RequestPool:
    def __init__(self):
        self.res = None

    def requestTool(self, method, url, headers=None):
        if method == 'GET':
            try:
                self.res = requests.get(url=url, headers=headers)
            except Exception as e:
                return False
        else:
            try:
                self.res = requests.post(url=url, headers=headers)
            except Exception as e:
                return False

        return self.res
