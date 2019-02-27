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

import requests
import csv
import time
import os
import argparse
import pymongo as mongo
import datetime


class Statistics(object):
    def __init__(self):
        self.downstream_channels_stats = dict()

    def mean(self, numbers):
        return float(sum(numbers)) / max(len(numbers), 1)

    def calculatePowerMean(self):
        values = list()
        for ch in self.downstream_channels_stats:
            values.append(self.downstream_channels_stats[ch].power)

        return self.mean(values)

    def calculateSNRMean(self):
        values = list()
        for ch in self.downstream_channels_stats:
            values.append(self.downstream_channels_stats[ch].snr)

        return self.mean(values)
    
    def persistInMongodb(self, host='127.0.0.1', port=27017):
        client = mongo.MongoClient(host, port)
        db = client['cmsraper']
        
        post_data = {'download': {}}
        ch_data = dict()

        ds = self.downstream_channels_stats

        # post_data['timestamp'] = int(time.time())
        post_data['timestamp'] = datetime.datetime.utcnow()

        for ch in ds:
            ch_data = dict()
            ch_data['power'] = ds[ch].power
            ch_data['snr'] = ds[ch].snr
            post_data['download'][str(ch)] = ch_data

        ch_data = dict()
        ch_data['power'] = self.calculatePowerMean()
        ch_data['snr'] = self.calculateSNRMean()
        post_data['download']["0"] =  ch_data
        db.stats.insert_one(post_data)


    def persistInCSV(self, output_path=None):
        timestamp = int(time.time())
        ds = self.downstream_channels_stats
        path = './' if output_path is None else output_path + '/'
        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except BaseException:
                raise

        for ch in ds:
            with open(path + str(ch) + '.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([timestamp, ds[ch].power, ds[ch].snr])

        with open(path + 'avg.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([timestamp,
                             "{:.2f}".format(self.calculatePowerMean()),
                             "{:.2f}".format(self.calculateSNRMean())])


class ChannelStatistics(object):
    def __init__(self):
        self.channel_number = None
        self.modulation = None
        self.frequency = None
        self.power = None
        self.snr = None
        self.ber = None
        self.correctables = None
        self.uncorrectables = None


class Scraper():
    DEFAULT_TIMEOUT = 10

    def __init__(self, http_client_timeout=DEFAULT_TIMEOUT):
        self.http_client_timeout = http_client_timeout
        self.device_name = None
        self.url = None
        self.stats = None

    def parse_web_page(self, page):
        pass

    def get_modem_status_page(self):
        try:
            page = requests.get(self.url, timeout=self.http_client_timeout)
        except Exception as e:
            print(str(e))
            exit(-1)

        if page.status_code != 200:
            print('Cannot get device status')
            exit(-1)

        return page
