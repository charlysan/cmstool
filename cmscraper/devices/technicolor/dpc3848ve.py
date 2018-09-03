# Copyright (c) 2018 charlysan

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from cmscraper.scraper import Scraper, Statistics, ChannelStatistics
from bs4 import BeautifulSoup
from os import getenv


class DPC384ve(Scraper):
    DEFAULT_TIMEOUT = 10

    def __init__(self, host=None, http_client_timeout=DEFAULT_TIMEOUT):
        Scraper.__init__(self, http_client_timeout=http_client_timeout)
        hostname = '192.168.0.1' if host is None else host
        self.url = "http://" + hostname + "/Docsis_system.php"

    def parse_web_page(self, page):
        soup = BeautifulSoup(page.content, 'html.parser')
        stats = Statistics()
        sum_pwr = list()
        sum_snr = list()

        tbody_data = soup.find(
            'table', attrs={
                'class': 'bm_docsisWanDSChannel'}).find('tbody')

        for element in tbody_data.find_all('tr'):
            ch_stats = ChannelStatistics()
            ch = element.find('td', attrs={'headers': 'ds_channel'})
            for s in ch.find_all('script'):
                s.extract()
            ch = int(ch.text)

            pwr = element.find('td', attrs={'headers': 'ds_power'})
            for s in pwr.find_all('script'):
                s.extract()
            pwr = float(pwr.text)

            snr = element.find('td', attrs={'headers': 'ds_snr'})
            for s in snr.find_all('script'):
                s.extract()
            snr = float(snr.text)

            sum_pwr.append(pwr)
            sum_snr.append(snr)

            ch_stats.channel_number = ch
            ch_stats.power = pwr
            ch_stats.snr = snr

            stats.downstream_channels_stats[ch] = ch_stats

        return stats
