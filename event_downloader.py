# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:37:05 2016

@author: jpbreuer
"""

from lxml import html
import requests
#import numpy as np

from datetime import date, timedelta as td

d1 = date(2012, 9, 30)
d2 = date(2014, 10, 2)

delta = d2 - d1

datelist = []
for i in range(delta.days + 1):
    datelist.append(d1 + td(days=i))

startindex = 0,93,365+93
stopindex = 92,365+92,len(datelist)-1

STATIONS = 'AATB','APTY','ARNM','ATHN','BKSN','BURE','CALG','CALM','DOMB','DOMC','DRBS','ESOI','FSMT','INVK','IRK2','IRK3','IRKT','JUNG','JUNG1','KERG','KGSN','KIEL','LMKS','MCMU','MCRL','MGDN','MOSC','MRNY','MWSN','MXCO','NAIN','NANM','NEWK','NRLK','NVBK','OULU','POTC','PTFM','PWNK','ROME','SANA','SOPB','SOPO','TERA','THUL','TSMB','TXBY','YKTK','KIEL2','NEU3','TIBT'

#STATIONS = 'THUL','YKTK'

for jj in range(len(STATIONS)+1):
    data_array = ""
    for ii in range(len(startindex)):
        #    link = 'http://www.nmdb.eu/nest/draw_graph.php?formchk=1&stations[]=KIEL' + \
        link = 'http://www.nmdb.eu/nest/draw_graph.php?formchk=1&stations[]=' + STATIONS[jj] + \
        '&output=ascii&force=1&tabchoice=revori&dtype=corr_for_efficiency&' + \
        'tresolution=5&date_choice=bydate&' + \
        'start_year=' + datelist[startindex[ii]].strftime('%Y') + '&start_month=' + datelist[startindex[ii]].strftime('%m') + '&start_day=' + datelist[startindex[ii]].strftime('%d') + '&start_hour=' + '00' + '&start_min=' + '00' +'&' + \
        'end_year=' + datelist[stopindex[ii]].strftime('%Y') + '&end_month=' + datelist[stopindex[ii]].strftime('%m') + '&end_day=' + datelist[stopindex[ii]].strftime('%d') + '&end_hour=' + '23' + '&end_min=' + '59'  #right now start_time is 2012-09-30 00:00 #right now end_time is 2013-09-30 23:59
        
        page = requests.get(link)
        tree = html.fromstring(page.content)
        
        if (tree.xpath('/html/body/font/b') == []):
            full = tree.xpath('//code')[0].text#[0:725]
            stations = tree.xpath('//code')[0].text[745:750]
            data = tree.xpath('//code')[0].text[778:]
            
            data_array += data
        else:
            continue #elif (tree.xpath('/html/body/font/b')[0].text == 'Sorry, no data available'):
        print('Iteration', str(ii+1), 'of', len(startindex), 'completed!')
    
    f = open('NMDB_' + STATIONS[jj] + '_data.txt', 'w')
    f.write('Timestamp;    ')
    f.write(stations)
    f.write(data_array)
    f.close()
    print('Station', str(jj+1), 'of', len(STATIONS), 'finished....')
#    data_array =  '\n'.join([data,string2,string3])
    