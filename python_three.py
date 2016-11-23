import re
import requests
import time
# запускать желательно с консоли (cmd)
file = open('result.html', 'w')
file.write('<!DOCTYPE html><html><head><meta charset=UTF-8"></head><body><ul>')
country = 'us'
city = 'Boston'
category_id = '12'
state = 'MA'
key = '1743c52773e172746156c60174f2964'
days = 7
url = 'https://api.meetup.com/2/concierge?key=' + key + '&sign=true&photo-host=public&country=' + country + '&city=' + city + '&category_id=' + category_id + '&state=' + state
r = requests.get(url)
name = re.findall(r'"name":"([\w\ \(\)\:]+)","id":"[\w ]+","time":([\d]+)', r.text)
address = re.findall(r'"address_1":"([\w\ \.\&]+)"', r.text)
for i in range(days):
    for j in range(len(name)):
        if (int(name[j][1])<((i+1)*86400000+time.time()*1000)) and (int(name[j][1])>(i*86400000+time.time()*1000)):
            file.write('<div>' + str(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(float(name[j][1])/1000))) + ' Name the event: "' + str(name[j][0]) + '". Address - ' + str(address[j]) + '</div>')
file.write('</ul></body></html>')
print('Результат находится в файле result.html')
