import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN_YD = os.getenv('TOKEN_YD')


class TestYandexDiskCreateFolder:
    def setup_method(self):
        self.headers = {
            'Authorization': TOKEN_YD
        }

    def teardown_method(self):
        params = {
            'path': 'Folder-1',
            'permanently': 'true'
        }
        requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                        params=params, headers=self.headers)
        params = {
            'path': 'Folder-2',
            'permanently': 'true'
        }
        requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                        params=params, headers=self.headers)

    def test_create_folder_201(self):
        params = {
            'path': 'Folder-1'
        }
        response = requests.put(
            'https://cloud-api.yandex.net/v1/disk/resources',
            params=params, headers=self.headers)
        assert response.status_code == 201

    def test_create_folder_409(self):
        params = {
            'path': 'Folder-2'
        }
        response = requests.put(
            'https://cloud-api.yandex.net/v1/disk/resources',
            params=params, headers=self.headers)
        assert response.status_code == 201
        response = requests.put(
            'https://cloud-api.yandex.net/v1/disk/resources',
            params=params, headers=self.headers)
        assert response.status_code == 409
