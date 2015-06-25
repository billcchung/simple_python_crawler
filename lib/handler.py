import os
from urllib.request import urlopen
from urllib.parse import urlparse
import threading
from lxml import html

class Handler(object):

    def __init__(self, config):
        self.dir = config['dirs']['output']
        if not os.path.exists(self.dir):  os.mkdir(self.dir)

    def crawl(self, entry, depth=2):
        url = entry.rstrip('/')
        f = os.path.join('outputs', url.replace(':','').replace('/','_')[:100])
        # check if the web is already processed.
        if os.path.exists(f) or depth <= 0:
            return 0
        print("Crawling: " + url)
        try:
            r = urlopen(url).read()
        except Exception as e:
            print("Exception at url: " + url + "reason: " + str(e))
            return 1
        with open(f, 'wb+') as output_file:
            output_file.write(r)
        h = html.fromstring(r)
        baseurl = self.get_baseurl(url)

        # getting links and process them.
        threads = []
        for e in h.cssselect('a'):
            link = e.get('href')
            if link and not link == '#':
                if not link.startswith('http'):
                    threads.append(threading.Thread(
                        target=self.crawl, args=[baseurl + link, depth-1]))
                else:
                    threads.append(threading.Thread(
                        target=self.crawl, args=[link, depth-1]))
        for thread in threads:
            thread.start()

    def get_baseurl(self, entry):
        return (urlparse(entry)[0] + "://" +  urlparse(entry)[1] + '/')






