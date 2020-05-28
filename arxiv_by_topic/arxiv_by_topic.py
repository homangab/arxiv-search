#### Homanga Bharadhwaj wrote this quick and dirty script to easily search for papers on arxiv based on keywords and 
#### a timestamp beyond which to search. Suggestions to improve are welcome! Feel free to ping me at homanga@cs.toronto.edu


import numpy as np

import string


import pandas as pd
import time

import urllib
import urllib.request

import sys
import argparse

parser = argparse.ArgumentParser(description='Scrape arxiv papers')
parser.add_argument('keywords', nargs='+',
                   help='a list of keywords')
parser.add_argument('--time', help='a list of keywords')

baseurl = 'http://export.arxiv.org/api/query?search_query='

args = parser.parse_args()

keyword_list = args.keywords



date = pd.Timestamp(str(args.time), tz='US/Pacific')


i = 0
for keyword in keyword_list:
    if i ==0:
        url = baseurl + 'abs:' + keyword
        i = i + 1
                    
    else:
        url = url + '+AND+' + 'abs:' + keyword

url = url+ '&max_results=10000'        

      
try:        
    
    arxiv_page = urllib.request.urlopen(url).read()

    
    arxiv_page = str(arxiv_page)    

    
    begin=[]
    end = []
    begin_time=[]
    end_time = []




    start = 0
    while True:
        
        start = arxiv_page.find('<link title="pdf" href=',start)
        if start==-1:
            break
        begin.append(start)
        
        start = start + len('<link title="pdf" href=')    

    start = 0
    while True:
        
        start = arxiv_page.find('rel="related" type="application/pdf"/>',start)
        if start==-1:
            break
        end.append(start)
        start = start + len('rel="related" type="application/pdf"/>')    


    start = 0
    while True:
        
        start = arxiv_page.find('<published>',start)
        if start==-1:
            break
        begin_time.append(start)
        
        start = start + len('<published>')    

    start = 0
    while True:
        
        start = arxiv_page.find('</published>',start)
        if start==-1:
            break
        end_time.append(start)
        start = start + len('</published>')    



    rows = []
    for i in range(len(begin)):  

       
        
        paper_link = arxiv_page[begin[i]+24:end[i]-2]
        paper_timestamp = arxiv_page[begin_time[i]+11:end_time[i]]

        if pd.to_datetime(paper_timestamp) > date:
           print(i)
           rows.append([paper_link,paper_timestamp])


    import csv
    with open('arxiv.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


  

except:
    pass