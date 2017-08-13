# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class HhParserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    URL     = Field()
    DATE    = Field()

    COUNTRY     = Field()
    DISTRICT    = Field()
    CITY        = Field()

    NIGHT_TEMP          = Field()
    NIGHT_FEELS         = Field()
    NIGHT_WIND          = Field()
    NIGHT_PRESSURE      = Field()
    NIGHT_HUMIDITY      = Field()
    NIGHT_geoCONDITIONS = Field()

    MORNING_TEMP          = Field()
    MORNING_FEELS         = Field()
    MORNING_WIND          = Field()
    MORNING_PRESSURE      = Field()
    MORNING_HUMIDITY      = Field()
    MORNING_geoCONDITIONS = Field()

    DAY_TEMP          = Field()
    DAY_FEELS         = Field()
    DAY_WIND          = Field()
    DAY_PRESSURE      = Field()
    DAY_HUMIDITY      = Field()
    DAY_geoCONDITIONS = Field()

    EVENING_TEMP          = Field()
    EVENING_FEELS         = Field()
    EVENING_WIND          = Field()
    EVENING_PRESSURE      = Field()
    EVENING_HUMIDITY      = Field()
    EVENING_geoCONDITIONS = Field()
