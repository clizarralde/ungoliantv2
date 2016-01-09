'''
Created on Jan 3, 2016

@author: igzo
'''
from src.main.Sites import sites
from src.model.Ungoliant import Ungoliant
from src.model.fetcher.JSFetcher import JSFetcher
from src.model.crawler.ComplexCrawler import ComplexCrawler
import logging




if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('ungoliant')

    url_sites = sites.keys()
    site = sites[url_sites[1]]
    
    spider = Ungoliant(site_config=site)
    
    spider.set_max_crawl(150)
    spider.set_crawler(ComplexCrawler())
    spider.set_fetcher(JSFetcher())
    
    crawled = spider.crawl()
    print len(crawled)
    print crawled