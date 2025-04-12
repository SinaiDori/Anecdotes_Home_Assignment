from api_requests import get, post


def connectivity_test(url, credentials, params=None, headers=None):
    response = post(url, json=credentials)
    return response.get('accessToken')
