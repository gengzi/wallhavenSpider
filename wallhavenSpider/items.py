# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WallhavenspiderItem(scrapy.Item):
    # define the fields for your item here like:
	# 图片的id
    imageId = scrapy.Field()
    # 图片的缩略图路径
    imageThumbnailUrl = scrapy.Field()
    # 图片的分辨率
    imageSize = scrapy.Field()
    # 图片的下载路径
    imageDownloadUrl = scrapy.Field()
    # 图片的tag的路径
    imageTagUrl = scrapy.Field()
    # 图片保存的路径
    #imagePath = scrapy.Field()
	
	

