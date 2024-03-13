import unittest
from unittest.mock import patch, MagicMock
from rest_client.rest_client import rest_stat, rest_read
from utils.utils import is_valid_url

from grpc import StatusCode
from proto_client.proto_client import grpc_stat, grpc_read

class TestFileClient(unittest.TestCase):

    def test_is_valid_url_valid(self):
        valid_urls = [
            "http://example.com",
            "https://example.com",
            "http://localhost:8000/",
            "https://localhost:8000/"
        ]
        for url in valid_urls:
            self.assertTrue(is_valid_url(url))

    def test_is_valid_url_invalid(self):
        invalid_urls = [
            "example.com",
            "ftp://example.com",
            "rrrrrrr//localhost:8000/pathdasda"
        ]
        for url in invalid_urls:
            self.assertFalse(is_valid_url(url))

    @patch("rest_client.rest_client.requests.get")
    def test_rest_stat_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "create_datetime": "2024-03-12T12:00:00",
            "size": 1000,
            "mimetype": "text/plain",
            "name": "example.txt"
        }
        mock_get.return_value = mock_response
        with patch("builtins.print") as mock_print:
            rest_stat("123456", "http://example.com")
            expected_output = {'create_datetime': '2024-03-12T12:00:00', 'size': 1000, 'mimetype': 'text/plain', 'name': 'example.txt'}
            mock_print.assert_called_with(expected_output)

    @patch("rest_client.rest_client.requests.get")
    def test_rest_stat_file_not_found(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        with patch("builtins.print") as mock_print:
            rest_stat("123456", "http://example.com")
            mock_print.assert_called_with("File not found.")

    @patch("rest_client.rest_client.requests.get")
    def test_rest_read_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"File content"
        mock_get.return_value = mock_response
        with patch("builtins.print") as mock_print:
            result = rest_read("123456", "http://example.com")
            self.assertEqual(result, b"File content")
            mock_print.assert_not_called()

    @patch("rest_client.rest_client.requests.get")
    def test_rest_read_file_not_found(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        with patch("builtins.print") as mock_print:
            result = rest_read("123456", "http://example.com")
            self.assertIsNone(result)
            mock_print.assert_called_with("File not found.")

if __name__ == "__main__":
    unittest.main()
