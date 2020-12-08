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

from __future__ import print_function
from cmscraper.devices.technicolor.dpc3848ve import DPC384ve

import argparse


def main():
    """Main function that is called when cmscraper is run on the command line"""
    parser = argparse.ArgumentParser(
        description='A Python tool that extracts statistics data from modem status web page.')

    parser.add_argument('-d', action='store', dest='DEVICE_NAME', default=None,
                        type=str, help='Device Name (Supported devices: technicolor-dpc384ve)')

    parser.add_argument('-i', action='store', dest='MODEM_IP_ADDRESS', default=None,
                        type=str, help='Modem IP Address (Default: 192.168.0.1)')

    parser.add_argument('-o', action='store', dest='OUTPUT_PATH', default='data',
                        type=str, help='Output path to store statistics')

    parser.add_argument('-t', action='store', dest='HTTP_TIMEOUT', default=10,
                        type=int, help='HTTP Client Timeout (Default: 10s)')

    args = parser.parse_args()

    if args.DEVICE_NAME is None:
        print('You must specify a device name. Type cmscraper --help for more information.')
        exit(-1)
    elif args.DEVICE_NAME.upper() == 'TECHNICOLOR-DPC384VE':
        scraper = DPC384ve(
            host=args.MODEM_IP_ADDRESS,
            http_client_timeout=args.HTTP_TIMEOUT)

    page = scraper.get_modem_status_page()
    stats = scraper.parse_web_page(page)
    stats.persistInCSV(output_path=args.OUTPUT_PATH)


if __name__ == "__main__":
    main()
