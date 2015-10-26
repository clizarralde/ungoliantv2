

class Ungoliant:
    
    def __init__(self, x_site ):
        
        self.logfile  = None 
        self.logger =  None
        

    def get_start_urls(self):
        pass
    
    
    def extract_links(self, page):
        pass
    
    
    def crawl(self):
        
        start_urls = self.get_start_urls()
        
        for url in start_urls:
            self.stack.push(url)

        finished = False
        
        output = []
        while not finished:
            
            url = self.stack.pop()
                    
            page = self.fetch(url)
            
            follow_urls = self.extract_links(page)
            if follow_urls:
                self.stack.push_all(follow_urls)
                
            elif self.stack.empty:
                finished = True
            
            item = self.scrap(url, page)
            
            output.append(item)
        
        self.store(output)
        
if __name__ == '__main__':
    
    x_site = "thecjm.org"
    
    spider = Ungoliant(x_site=x_site)
    
    spider.crawl()