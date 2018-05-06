from bs4 import BeautifulSoup
import time
import csv
import requests

url = "http://192.168.0.1/Docsis_system.php"
TIMEOUT = 10


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

try:
    page = requests.get(url, timeout=TIMEOUT)
except Exception as e:
    print(str(e))
    exit(-1)

if page.status_code != 200:
    print('Cannot get device status')
    exit(-1)

soup = BeautifulSoup(page.content, 'html.parser')

values = list()
values_avg = list()
sum_pwr = list()
sum_snr = list()

tbody_data = soup.find('table', attrs={'class':'bm_docsisWanDSChannel'}).find('tbody')

timestamp = int(time.time())
for element in tbody_data.find_all('tr'):
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

    values.append([timestamp, ch, pwr, snr])
    sum_pwr.append(pwr)
    sum_snr.append(snr)

print([timestamp, mean(sum_pwr), mean(sum_snr)])

for t,ch,pw,snr in values:
    with open(str(ch) + '.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([t, pw, snr])

with open('avg.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([timestamp, "{:.2f}".format(mean(sum_pwr)), "{:.2f}".format(mean(sum_snr))])

