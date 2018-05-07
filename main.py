from cmscraper.devices.technicolor.dpc3848ve import DPC384ve

def main():
    scraper = DPC384ve()
    page = scraper.get_modem_status_page()
    stats = scraper.parse_web_page(page)
    scraper.generate_csv_files(stats)
    
if __name__ == "__main__": 
    main()