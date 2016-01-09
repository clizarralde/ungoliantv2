'''
Created on Jan 3, 2016

@author: igzo
'''

import logging
from src.model.crawler.Crawler import Crawler

logger = logging.getLogger('ungoliant')


class RegularCrawler(Crawler):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def crawl(self, spider):
        
        logger.info("Starting the crawl")
        stack = []
        crawled_links = []
        visited = []

        start_urls = spider.get_urls(spider.get_url_config().start_url())
        
        for url in start_urls:
            stack.append(url)
        
        output = []
        limit = spider.get_max_crawl()

        while len(stack) > 0 and limit > 0:
        
            new_url = stack.pop()

            try:
                if(spider.url_filter.satisfy(spider.get_url_config(), new_url) and new_url not in crawled_links):
                        
                        crawled_links.append(new_url)
                        limit -= 1
        
                        content = spider.fetch(new_url)
                        if(content):
                            item = spider.scrap(new_url, content)
                            visited.append(new_url)
                            output.append(item)
                        
                            links = spider.extract_links(content)
                            urls = spider.filter(links)
                    
                            for url in urls:    
                                stack.append(url)
            except Exception as e:
                logger.warn("Error when fetching %s" % new_url)

        spider.store(output)
        spider.finish()
        
        logger.info("Finishing the crawl")
        
        return crawled_links
