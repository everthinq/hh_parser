# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


#class HhParserPipeline(object):
#    def process_item(self, item, spider):
#        return item

from datetime import *

import sqlite3
import os

from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher


#class GismeteoParserPipeline(object):
#    def process_item(self, item, spider):
#        return item

class SQLiteStorePipeline(object):
    filename = '../../database/gismeteo.db'

    def __init__(self):
        if not os.path.isdir('../../database/'):
            os.mkdir('../../database/')

        self.conn = None
        dispatcher.connect(self.initialize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)

    def process_item(self, item, spider):
        try:
            date = datetime.now()
            date = str(date)
            date = date[:10]
            item['DATE'] = date

            self.conn.execute(''
            'INSERT INTO db VALUES(?,?, ?,?,?, ?,?,?,?,?,?, ?,?,?,?,?,?, ?,?,?,?,?,?, ?,?,?,?,?,?)',
            (
                item['URL'], item['DATE'],
                item['COUNTRY'], item['DISTRICT'], item['CITY'],
                item['NIGHT_TEMP'], item['NIGHT_FEELS'], item['NIGHT_WIND'], item['NIGHT_PRESSURE'], item['NIGHT_HUMIDITY'], item['NIGHT_geoCONDITIONS'],
                item['MORNING_TEMP'], item['MORNING_FEELS'], item['MORNING_WIND'], item['MORNING_PRESSURE'], item['MORNING_HUMIDITY'], item['MORNING_geoCONDITIONS'],
                item['DAY_TEMP'], item['DAY_FEELS'], item['DAY_WIND'], item['DAY_PRESSURE'], item['DAY_HUMIDITY'], item['DAY_geoCONDITIONS'],
                item['EVENING_TEMP'], item['EVENING_FEELS'], item['EVENING_WIND'], item['EVENING_PRESSURE'], item['EVENING_HUMIDITY'], item['EVENING_geoCONDITIONS']
            )
                            )
        except:
            print('Failed to insert item')
        return item

    def initialize(self):
        if os.path.exists(self.filename):
            self.conn = sqlite3.connect(self.filename)
        else:
            self.conn = self.create_table(self.filename)

    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None

    def create_table(self, filename):
        conn = sqlite3.connect(filename)
        conn.execute(''
                     'CREATE TABLE IF NOT EXISTS db'
                     '('
                        'url TEXT, date TEXT,'
                        'country TEXT, district TEXT, city TEXT,'
                        'night_temp TEXT, night_feels TEXT, night_wind TEXT, night_pressure TEXT, night_humidity TEXT, night_geoconditions TEXT,'
                        'morning_temp TEXT, morning_feels TEXT, morning_wind TEXT, morning_pressure TEXT, morning_humidity TEXT, morning_geoconditions TEXT,'
                        'day_temp TEXT, day_feels TEXT, day_wind TEXT, day_pressure TEXT, day_humidity TEXT, day_geoconditions TEXT,'
                        'evening_temp TEXT, evening_feels TEXT, evening_wind TEXT, evening_pressure TEXT, evening_humidity TEXT, evening_geoconditions TEXT'
                     ')'
                    )

        conn.commit()
        return conn