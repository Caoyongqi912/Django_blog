import requests


class RequestPool:
    def __init__(self):
        self.res = None

    def requestTool(self, method, url):
        if method == 'GET':
            try:
                self.res = requests.get(url=url)
            except Exception as e:
                print(e)
                return False
        else:
            try:
                self.res = requests.post(url=url)
            except Exception as e:
                print(e)
                return False

        return self.res
