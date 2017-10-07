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
    filename = '../database/hh.db'

    def __init__(self):
        if not os.path.isdir('../database/'):
            os.mkdir('../database/')

        self.conn = None
        dispatcher.connect(self.initialize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)

    def process_item(self, item, spider):
        try:
            #date = datetime.now()
            #date = str(date)
            #date = date[:10]
            #item['DATE'] = date

            self.conn.execute('INSERT INTO db VALUES(?,?,?,?)',
            (
                item['COUNTRY'], item['INDUSTRY'], item['COMPANY'], item['COMPANY_URL']
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
        conn.execute('CREATE TABLE IF NOT EXISTS db'
                     '('
                        'country TEXT, industry TEXT, company TEXT, company_url TEXT'
                     ')'
                    )

        conn.commit()
        return conn