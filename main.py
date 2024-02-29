import requests
import sys


class GitIgnoreIO():

    API_URL = "https://www.toptal.com/developers/gitignore/api/list?format="

    def __init__(self) -> None:
        pass

    def get_ignore_io(self):
        params = {
            'format': 'Rust',
        }

        response = requests.get('https://www.toptal.com/developers/gitignore/api/list', params=params)  # noqa: E501
        print(response)


if __name__ == "__main__":
    a = GitIgnoreIO()
    a.get_ignore_io()
