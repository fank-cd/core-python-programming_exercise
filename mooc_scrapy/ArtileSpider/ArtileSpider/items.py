# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
import datetime
import re
from scrapy.loader.processors import MapCompose, TakeFirst,Join


def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y%m%d").date()
    except:
        create_date = datetime.datetime.now().date()
    return create_date


def get_nums(value):

    match_re = re.match(r".*?(\d+).*", value)
    if match_re:
        nums = match_re.groups(1)
    else:
        nums = 0

    return nums


def remove_comment_tags(value):
    # 去掉tag中多余的评论字段

    if "评论" in value:
        return ""
    else:
        return value


def return_value(value):
    return value


class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class JobBoleAritleItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert),
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()

    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value),
    )
    front_image_path = scrapy.Field()

    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums),
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums),
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums),
    )

    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(","),
    )
    content = scrapy.Field()
