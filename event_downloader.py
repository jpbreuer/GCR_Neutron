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
d2 = date(2014, 4, 2)

delta = d2 - d1

datelist = []
for i in range(delta.days + 1):
    datelist.append(d1 + td(days=i))

data_array = ""

for ii in range(len(datelist)):
#    link = 'http://www.nmdb.eu/nest/draw_graph.php?formchk=1&stations[]=KIEL' + \
    link = 'http://www.nmdb.eu/nest/draw_graph.php?formchk=1&allstations=1' + \
    '&output=ascii&force=1&tabchoice=revori&dtype=corr_for_efficiency&' + \
    'tresolution=5&date_choice=bydate&' + \
    'start_year=' + datelist[ii].strftime('%Y') + '&start_month=' + datelist[ii].strftime('%m') + '&start_day=' + datelist[ii].strftime('%d') + '&start_hour=' + '00' + '&start_min=' + '00' +'&' + \
    'end_year=' + datelist[ii+1].strftime('%Y') + '&end_month=' + datelist[ii+1].strftime('%m') + '&end_day=' + datelist[ii+1].strftime('%d') + '&end_hour=' + '23' + '&end_min=' + '59'  #right now start_time is 2012-09-30 00:00 #right now end_time is 2013-09-30 23:59

    #'start_year=' + start_times[ii][0:4] + '&start_month=' + start_times[ii][4:6] + '&start_day=' + start_times[ii][6:8] + '&start_hour=' + '00' + '&start_min=' + '00' +'&' + \
    #'end_year=' + end_times[ii][0:4] + '&end_month=' + end_times[ii][4:6] + '&end_day=' + end_times[ii][6:8] + '&end_hour=' + '23' + '&end_min=' + '59'  #right now start_time is 2012-09-30 00:00 #right now end_time is 2013-09-30 23:59

    page = requests.get(link)
    tree = html.fromstring(page.content)

    header = tree.xpath('//code')[0].text[0:725]
    stations = tree.xpath('//code')[0].text[725:957]
    data = tree.xpath('//code')[0].text[957:]
    
    data_array += data
    print('Iteration', str(ii), 'of', len(datelist), 'completed!')

#    data_array =  '\n'.join([data,string2,string3])
    
f = open('NMDB_station_data.txt', 'w')
f.write(stations)
f.write(data_array)
f.close()
    


#url = ''
#values = {formchk=1
#stations[]=KIEL
#output=ascii
#force=1
#tabchoice=revori
#dtype=corr_for_efficiency
#tresolution=5
#date_choice=bydate
#start_year=2012
#start_month=09
#start_day=30
#start_hour=00
#start_min=00
#end_year=2013
#end_month=09
#end_day=30
#end_hour=23
#end_min=59
#}
#
#data = urllib.parse.urlencode(values)
#data = data.encode('ascii') #data should be bytes
#req = urllib.request.Request(rurl,data)
#with urllib.request.urlopen(req) as response:
#    the_page = response.read()