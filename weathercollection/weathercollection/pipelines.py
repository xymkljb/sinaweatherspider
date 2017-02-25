# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WeathercollectionPipeline(object):

    def process_item(self, item, spider):
        with open('wea.txt', 'w+') as file:
            city = item['city'][0].encode('utf-8')
            file.write('city:'+str(city)+'\n\n')
            date = item['date']
            desc = item['daydesc']
            daydesc = desc[0::2]
            nightdesc = desc[1::2]
            daytemp = item['daytemp']
            wind = item['wind']
            pm = item['pm']
            air = item['air']
            weazip = zip(date, daydesc, nightdesc, daytemp, wind, pm, air)
            for i in range(len(weazip)):
                item = weazip[i]
                d = item[0]
                dd = item[1]
                nd = item[2]
                dt = item[3].split('/')
                w = item[4]
                p = item[5]
                a = item[6]
                dt = dt[0]
                nt = dt[1]
                txt = 'date:{0}\tday:{1}{2}\tnight:{3}{4}\twind:{5}\t\tpm:{6} {7}\n'.format(
                    d,
                    dd.encode('utf-8'),
                    dt.encode('utf-8'),
                    nd.encode('utf-8'),
                    nt.encode('utf-8'),
                    w.encode('utf-8'),
                    p,
                    a.encode('utf-8'))
                file.write(txt)
        return item
