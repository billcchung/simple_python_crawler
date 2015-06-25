import re, os, sys
from urllib.request import urlopen
if not os.path.exists('outputs'): os.mkdir('outputs')

def crawl(entry):
    f = os.path.join('outputs', entry.replace('/','_')[:100])
    if os.path.exists(f): return 0
    print("Crawling: " + entry)
    content = urlopen(entry).read()
    with open(f, 'wb') as output_file: output_file.write(content)
    for url in re.findall(r'href=[\'"]?([^\'" >]+)', str(content)):
        if url.startswith('http'): crawl(url)  

if __name__ == '__main__':
    crawl(sys.argv[1])