# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#引入settings.py 的配置项
import scrapy
import json
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os

class WallhavenspiderPipeline(ImagesPipeline):
    #获取在 settings 文件中的配置项
    IMAGE_SOURCE = get_project_settings().get('IMAGES_STORE')


    def get_media_requests(self, item, info):
        image_url = item['imageDownloadUrl']
        yield scrapy.Request(image_url)


    def item_completed(self, result, item, info):
        image_path = [x["path"] for ok, x in result if ok]
        os.rename(self.IMAGE_SOURCE + "\\" + image_path[0], self.IMAGE_SOURCE + "\\" + item["imageId"] + ".jpg")
        item['imageDownloadUrl'] = image_path
        return item


