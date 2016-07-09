# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:37:05 2016

@author: jpbreuer
"""

#20120930 to 20140401
#5 minute resolution

from lxml import html
import requests

start_times = '201209300000','201309310000'
end_times = '201309302359','201404012359'


#station is KIEL, loop over all stations
for ii in range(len(start_times))
    link = 'http://www.nmdb.eu/nest/draw_graph.php?formchk=1&stations[]=KIEL' + \
    '&output=ascii&force=1&tabchoice=revori&dtype=corr_for_efficiency&' + \
    'tresolution=5&date_choice=bydate&' + \
    'start_year=' + start_times[ii][0:4] + '&start_month=' + start_times[ii][4:6] + '&start_day=' + start_times[ii][6:8] + '&start_hour=' + start_times[ii][8:10] + '&start_min=' + start_times[ii][10:12] +'&' + \
    'end_year=' + end_times[ii][0:4] + '&end_month=' + end_times[ii][4:6] + '&end_day=' + end_times[ii][6:8] + '&end_hour=' + end_times[ii][8:10] + '&end_min=' + end_times[ii][10:12]  #right now start_time is 2012-09-30 00:00 #right now end_time is 2013-09-30 23:59

    page = requests.get(link)
    tree = html.fromstring(page.content)

    data = tree.xpath('//code')[0].text
    


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