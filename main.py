from cmscraper.devices.technicolor.dpc3848ve import DPC384ve

def main():
    scraper = DPC384ve()
    scraper.parse_statistics_from_modem()
    
if __name__ == "__main__": 
    main()