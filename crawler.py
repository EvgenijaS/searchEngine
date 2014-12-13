# -*- coding: utf-8 -*-
#komentar
import urlparse
import urllib
from bs4 import BeautifulSoup
#from urlparse import urlparse
def promena():
    print ':)'


    
def get_domain(url):
    try:
        parsed_uri = urlparse.urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        return domain
    except:
        print 'Error unicode' , url
        return ''

def makSites(link):
    return '.mk' in link

def crawl(url, max_links = 10000):
    urls = [url]
    visited = set([url])

    point_to = []
    point_to_added = set([])
        
    c = 1

        
    while len(urls) > 0:
        try:
            htmltext = urllib.urlopen(urls[0]).read()
        except:
            print 'ERROR!' + urls[0]
            
        soup = BeautifulSoup(htmltext)

        urls.pop(0)

        for tag in soup.findAll('a', href = True):
            tag['href'] = urlparse.urljoin(url, tag['href'])

            if url in tag['href'] and tag['href'] not in visited:
                urls.append(tag['href'])
                visited.add(tag['href'])
                c += 1
            elif url not in tag['href'] and get_domain(tag['href']) not in point_to_added:
                point_to.append(get_domain(tag['href']))
                point_to_added.add(get_domain(tag['href']))
##                print get_domain(tag['href'])
##                c += 1
##        if c % 1000 == 0:
##            print c
        print c
        if c > max_links:
            break

    return point_to, visited

def readURLS(file_name):
    file = open(file_name,'r')
    urls = file.read().split('\n')
    file.close()
    mk_urls = set([]) ## mk_urls = set(filter(mkSites,mk_urls)
    for line in urls:
        if '.mk' in line:
            mk_urls.add(line)
    
    return list(mk_urls)

        
def writeCrawledURLS(urls, file_name):
    file = open(file_name, 'a')
    for url in urls:
        file.write(url + '\n')
    file.close()
    
def crawlURLS():
    urls_to_crawl = readURLS('urls.txt')
    from_to = {}
    for url in urls_to_crawl:
        from_to[url]=[]
    
    for url in urls_to_crawl:
        point_links, crawled_links = crawl(url)
        writeCrawledURLS(point_links, 'crawled.txt')
        from_to[url] += point_links
    return from_to

##while True:
##    try:
##        crawlURLS()
##    except Exception ,e:
##        print 'error internet connection'
##        print e
##        print '-'*80
##        
url = 'http://www.macedonia.eu.org/'
p,v = crawl(url,1000)

for e in p:
    print e
print 'ok e uploadot'