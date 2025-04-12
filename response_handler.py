import requests


class ResponseHandler:
    @staticmethod
    def handle(response):
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print("HTTP error occurred:", http_err)
            raise
        except requests.exceptions.Timeout as timeout_err:
            print("Timeout error occurred:", timeout_err)
            raise
        except requests.exceptions.ConnectionError as conn_err:
            print("Connection error occurred:", conn_err)
            raise
        except ValueError as json_err:
            print("JSON decoding error:", json_err)
            raise
        except requests.exceptions.RequestException as req_err:
            print("General request error occurred:", req_err)
            raise
