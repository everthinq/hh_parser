from scrapy.cmdline import execute

def main():
    execute(['scrapy', 'crawl', 'hh_parser', '-s', 'LOG_ENABLED=0'])
    #execute(['scrapy', 'crawl', 'hh_parser'])


if __name__ == '__main__':
    main()