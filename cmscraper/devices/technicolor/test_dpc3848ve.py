import unittest
from mock import mock
from cmscraper.devices.technicolor.dpc3848ve import DPC384ve
from cmscraper.scraper import Statistics
import os


def mocked_requests_get_ok(*args, **kwargs):
    class MockResponse:
        def __init__(self, content, status_code):
            self.content = content
            self.status_code = status_code

    with open(os.path.dirname(__file__) + '/test_data/dpc3848ve.php') as file:
        data = file.read()

    return MockResponse(data, 200)


class TestDPC348ve(unittest.TestCase):
    def setUp(self):
        pass

    @mock.patch('requests.get', side_effect=mocked_requests_get_ok)
    def test_parse_web_page_ok(self, mock_get):
        scraper = DPC384ve()
        page = scraper.get_modem_status_page()
        stats = scraper.parse_web_page(page)

        pwr_expected_list = [
            6.3,
            11.0,
            10.6,
            10.7,
            11.4,
            11.3,
            10.5,
            10.3,
            10.3,
            8.1,
            8.4,
            7.4,
            6.8,
            7.2,
            6.9,
            8.2,
            6.9,
            6.0,
            5.9,
            5.6,
            5.5,
            4.8,
            3.7,
            4.6]
        snr_expected_list = [
            34.48,
            37.35,
            37.09,
            36.61,
            36.61,
            36.61,
            36.61,
            36.38,
            36.61,
            35.08,
            35.59,
            30.82,
            32.32,
            34.92,
            34.48,
            35.59,
            34.48,
            34.48,
            34.48,
            34.34,
            34.34,
            34.34,
            33.83,
            33.83]

        expected_stats = Statistics()

        for ch in range(1, 25):
            self.assertEquals(
                pwr_expected_list[ch - 1], stats.downstream_channels_stats[ch].power)
            self.assertEquals(
                snr_expected_list[ch - 1], stats.downstream_channels_stats[ch].snr)


if __name__ == '__main__':
    unittest.main()
