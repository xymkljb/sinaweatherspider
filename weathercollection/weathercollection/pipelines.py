# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WeathercollectionPipeline(object):

    def process_item(self, item, spider):
        with open('wea.txt', 'a') as file:
            province = item['province'].encode('utf-8')
            file.write('province:'+str(province)+'\n')
            for i in range(len(item['data'])):
                file.write(
                    'city:' +
                    str(item['data'][i][0][0].strip().encode('utf-8')) + '\n')
                file.write('county\t\t%32s\t\t%32s\n' % (
                    item['date'][0].encode('utf-8'),
                    item['date'][1].encode('utf-8')))
                for j in range(len(item['data'][i][1])):
                    ct = item['data'][i][1][j]
                    wday = item['data'][i][2][0::2][j]
                    wnight = item['data'][i][2][1::2][j]
                    wind = item['data'][i][3][0::2]
                    windday = wind[0::2][j]
                    windnight = wind[1::2][j]
                    temp = item['data'][i][3][1::2]
                    tempday = temp[0::2][j]
                    tempnight = temp[1::2][j]
                    txt = '{0:6}\t\t{1:10} {2:10} {3:12}\t\t{4:10} {5:10} {6:12}\n'.format(
                        ct.encode('utf-8'),
                        wday.encode('utf-8'),
                        tempday.encode('utf-8'),
                        windday.encode('utf-8'),
                        wnight.encode('utf-8'),
                        tempnight.encode('utf-8'),
                        windnight.encode('utf-8'))
                    file.write(txt)
        return item
