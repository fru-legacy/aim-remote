import pickle
import requests

class Run:
    def __init__(self, **kwargs):
        self.url = kwargs['url']
        self.params = {
            'repo': kwargs['repo'],
            'experiment': kwargs['experiment'],
            'run_hash': kwargs['run_hash'],
            'security_token': kwargs['security_token']
        }

    def __getitem__(self, key):
        url = self.url + '/aimremote/get_values/' + key
        return requests.get(url, params=self.params).json()

    def __setitem__(self, key, value):
        url = self.url + '/aimremote/set_values/' + key
        requests.post(url, params=self.params, json=value)

    def track(self, data, **kwargs):
        url = self.url + '/aimremote/track/'
        encoded = pickle.dumps([
            { 
                'data': data,
                'name': kwargs['name'],
                'step': kwargs['step'],
                'epoch': kwargs['epoch'],
                'context': kwargs['context']
            }
        ])
        requests.post(url, params=self.params, data=encoded)