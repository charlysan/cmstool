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

import matplotlib.pyplot as plt
import numpy as np
import datetime
import time
import os
from mpld3._server import serve
from mpld3 import fig_to_html


def convertfunc(x): return datetime.datetime.fromtimestamp(int(x))


import argparse


def main():
    """Main function that is called when cmstats_cli is run on the command line"""
    parser = argparse.ArgumentParser(
        description='A Python tool that plots cablemodem statistics scraped from modem status web page')

    parser.add_argument('--ch', action='store', dest='CHANNEL', default=None,
                        type=int, help='Plot single channel')

    parser.add_argument('--chs', action='store', dest='CHANNELS', default=None,
                        type=int, nargs='+', help='Plot multiple channels (e.g. 1 4 7 12)')

    parser.add_argument('--chr', action='store', dest='CHANNEL_RANGE', default=None,
                        type=int, nargs='+', help='Plot a range of channels (e.g. 0 24)')

    args = parser.parse_args()

    channels = [0]

    if args.CHANNEL is not None:
        channels = [args.CHANNEL]
    elif args.CHANNELS is not None:
        if len(args.CHANNELS) < 2:
            print(
                'You must specify at least two channels (e.g. cmstats_cli --chs 3 7 12')
        channels = args.CHANNELS
    elif args.CHANNEL_RANGE is not None:
        if len(args.CHANNEL_RANGE) != 2:
            print('You must specify two channels (e.g. cmstats_cli --chr 0 24)')
        channels = []
        for i in range(args.CHANNEL_RANGE[0], args.CHANNEL_RANGE[-1] + 1):
            channels.append(i)

    plot(channels)


def plot(channels=[0]):
    plt.rcParams.update({'figure.max_open_warning': 0})

    FIG_SIZE_X = 12
    FIG_SIZE_Y = 7
    PLOT_POWER_LINE_WIDTH = 1.2
    PLOT_POWER_COLOR = 'blue'
    PLOT_SNR_LINE_WIDTH = 1.2
    PLOT_SNR_COLOR = 'red'

    SNR_MIN_THRESHOLD = 30  # For limiting SNR y axis plot
    SNR_MIN_Y_VALUE_1 = 32
    SNR_MAX_Y_VALUE_1 = 40
    SNR_MIN_Y_VALUE_2 = 5
    SNR_MAX_Y_VALUE_2 = 40

    figures = dict()

    for x in channels:
        f = './data/' + str(x) + '.csv'
        exists = os.path.isfile(f)
        if not exists:
            continue

        data = np.genfromtxt(f, delimiter=',', skip_header=0)
        start = 1
        end = 10

        timestamp = np.genfromtxt(
            f, delimiter=',', unpack=True, converters={
                0: convertfunc}, usecols=0)
        power = np.genfromtxt(f, delimiter=',', unpack=True, usecols=1)
        snr = np.genfromtxt(f, delimiter=',', unpack=True, usecols=2)

        avg_snr = sum(snr) / float(len(snr))
        avg_pwr = sum(power) / float(len(power))
        sd_snr = np.std(np.array(snr))
        sd_pwr = np.std(np.array(power))

        # Print statistics to STDOUT
        print('Ch ' + str("{:02d}".format(x)) + ': PWR avg: ' + str("{:05.2f}".format(avg_pwr)) +
              ' dBmV / PWR std: ' + str("{:05.2f}".format(sd_pwr)) +
              ' - SNR avg: ' + str("{:05.2f}".format(avg_snr)) +
              ' dB  / SNR std: ' + str("{:05.2f}".format(sd_snr)))

        figures[x] = plt.figure(x, figsize=(FIG_SIZE_X, FIG_SIZE_Y))

        # Power Plot
        ax1 = plt.subplot(211)  # 2 rows, 1 column, subplot #1
        plt.plot(
            timestamp,
            power,
            linewidth=PLOT_POWER_LINE_WIDTH,
            color=PLOT_POWER_COLOR)
        plt.title('Channel ' + str(x), fontsize=22)
        plt.ylabel('Power (dBmV)')
        plt.xlabel('datetime')
        plt.grid(True)

        # SNR Plot
        ax2 = plt.subplot(212)  # 2 rows, 1 column, subplot #2
        plt.plot(
            timestamp,
            snr,
            linewidth=PLOT_SNR_LINE_WIDTH,
            color=PLOT_SNR_COLOR)
        plt.ylabel('SNR (dB)')
        plt.xlabel('datetime')
        plt.grid(True)

        # Limit SNR Y axis based on minimum value for better visualization
        axes = plt.gca()
        axes.set_ylim([SNR_MIN_Y_VALUE_1, SNR_MAX_Y_VALUE_1])

        if min(snr) < SNR_MIN_THRESHOLD:
            axes.set_ylim([SNR_MIN_Y_VALUE_2, SNR_MAX_Y_VALUE_2])

    # Serve all plots in the same html page
    html_sum = ''
    for x in figures:
        html = fig_to_html(figures[x])
        html_sum = html_sum + html

    serve(html_sum, open_browser=False, ip="0.0.0.0")


if __name__ == "__main__":
    main()
