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

from mpld3._server import serve
from mpld3 import fig_to_html
import matplotlib.pyplot as plt
import numpy as np
import argparse
import datetime
import time
import os


def convertfunc(x): return datetime.datetime.fromtimestamp(int(x))


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

    parser.add_argument('--path', action='store', dest='DATA_PATH', default='./data',
                        type=str, help='Absolute path containing csv files (default: ./data)')

    parser.add_argument('--since', action='store', dest='SINCE_DATETIME', default=None,
                        type=str, help='Since datetime [format: Y-M-D H:M:S] (e.g. --since "2018-09-25 08:00:00")')

    parser.add_argument('--till', action='store', dest='TILL_DATETIME', default=None,
                        type=str, help='Till datetime [format: Y-M-D H:M:S] (e.g. --till "2018-09-28 18:00:00")')

    parser.add_argument('--ip', action='store', dest='IP', default='0.0.0.0',
                        type=str, help='Ip address at which the HTML will be served (default: 0.0.0.0)')

    parser.add_argument('--do_not_open_browser', action='store_false', dest='DO_NOT_OPEN_BROWSER',
                        help='Do not open a web browser after processing input')

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

    plot(
        channels=channels,
        path=args.DATA_PATH,
        datetime_start=args.SINCE_DATETIME,
        datetime_end=args.TILL_DATETIME,
        ip=args.IP,
        open_browser=args.DO_NOT_OPEN_BROWSER)


def plot(channels=[0], path='./data', datetime_start=None,
         datetime_end=None, ip='0.0.0.0', open_browser=True):
    '''Plot Power/SNR vs time for all the channels specified within channels list'''

    FIG_SIZE_X = os.getenv('FIG_SIZE_X', 12)
    FIG_SIZE_Y = os.getenv('FIG_SIZE_Y', 7)
    PLOT_TITLE_FONT_SIZE = os.getenv('PLOT_TITLE_FONT_SIZE', 12)
    PLOT_POWER_LINE_WIDTH = os.getenv('PLOT_POWER_LINE_WIDTH', 1.2)
    PLOT_POWER_COLOR = os.getenv('PLOT_POWER_COLOR', 'blue')
    PLOT_SNR_LINE_WIDTH = os.getenv('PLOT_SNR_LINE_WIDTH', 1.2)
    PLOT_SNR_COLOR = os.getenv('PLOT_SNR_COLOR', 'red')

    SNR_MIN_THRESHOLD = os.getenv('SNR_MIN_THRESHOLD', 30) # For limiting SNR y axis plot
    SNR_MIN_Y_VALUE_1 = os.getenv('SNR_MIN_Y_VALUE_1', 32)
    SNR_MAX_Y_VALUE_1 = os.getenv('SNR_MAX_Y_VALUE_1', 40)
    SNR_MIN_Y_VALUE_2 = os.getenv('SNR_MIN_Y_VALUE_2', 5)
    SNR_MAX_Y_VALUE_2 = os.getenv('SNR_MAX_Y_VALUE_2', 40)

    datetime_format = '%Y-%m-%d %H:%M:%S'

    figures = dict()

     # Do not print warning if more than 20 plots are opened
    plt.rcParams.update({'figure.max_open_warning': 0})

    print('')
    
    for c in channels:
        f = path + '/' + str(c) + '.csv'
        exists = os.path.isfile(f)
        if not exists:
            continue
        
        data = np.genfromtxt(f, delimiter=',')

        # Crop input based on start/end datetime
        start = None
        end = None

        if datetime_start is not None or datetime_end is not None:
            if datetime_start is not None:
                timestamp_from = int(
                    time.mktime(
                        datetime.datetime.strptime(
                            datetime_start,
                            datetime_format).timetuple()))
            if datetime_end is not None:
                timestamp_to = int(
                    time.mktime(
                        datetime.datetime.strptime(
                            datetime_end,
                            datetime_format).timetuple()))

            for i, line in enumerate(data):
                if datetime_start is not None and line[0] >= timestamp_from:
                    if start is None:
                        start = i
                if datetime_end is not None and line[0] >= timestamp_to:
                    if end is None:
                        end = i

        timestamp = np.genfromtxt(
            f, delimiter = ',', unpack=True, converters={0: convertfunc},
            skip_header=start if start is not None else 1,
            skip_footer=(len(data) - end) if end is not None else 0,
            usecols=0)
        power = np.genfromtxt(
            f, delimiter = ',', unpack=True,
            skip_header = start if start is not None else 1,
            skip_footer = (len(data) - end) if end is not None else 0,
            usecols=1)
        snr = np.genfromtxt(
            f, delimiter = ',', unpack=True,
            skip_header = start if start is not None else 1,
            skip_footer = (len(data) - end) if end is not None else 0,
            usecols = 2)

        avg_snr = sum(snr) / float(len(snr))
        avg_pwr = sum(power) / float(len(power))
        sd_snr = np.std(np.array(snr))
        sd_pwr = np.std(np.array(power))

        # Print statistics to STDOUT
        print('Ch ' + str("{:02d}".format(c)) + ': PWR avg: ' + str("{:05.2f}".format(avg_pwr)) +
              ' dBmV / PWR std: ' + str("{:05.2f}".format(sd_pwr)) +
              ' - SNR avg: ' + str("{:05.2f}".format(avg_snr)) +
              ' dB  / SNR std: ' + str("{:05.2f}".format(sd_snr)))

        figures[c] = plt.figure(c, figsize=(FIG_SIZE_X, FIG_SIZE_Y))

        # Power Plot
        plt.subplot(211)  # 2 rows, 1 column, subplot #1
        plt.plot(
            timestamp,
            power,
            linewidth=PLOT_POWER_LINE_WIDTH,
            color=PLOT_POWER_COLOR)
        plt.title('Channel ' + str(c), fontsize=PLOT_TITLE_FONT_SIZE)
        plt.ylabel('Power (dBmV)')
        plt.xlabel('datetime')
        plt.grid(True)

        # SNR Plot
        plt.subplot(212)  # 2 rows, 1 column, subplot #2
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
    for f in figures:
        html = fig_to_html(figures[f])
        html_sum = html_sum + html

    print('')
    serve(html_sum, open_browser=open_browser, ip=ip)


if __name__ == "__main__":
    main()