import requests

from apis.config import base_url

__author__ = 'Antonio Martín González'
__email__ = 'ant.martin.gonzalez@gmail.com'


def get_films(id: int = None, page: int = 1):
    url = base_url + '/films'
    if id is not None:
        url = url + f'/{id}'
        params = None
    else:
        params = f'page={page}'
    response = requests.get(url=url, params=params)
    return response
