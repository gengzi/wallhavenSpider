# -*- coding: utf-8 -*-
import scrapy
from wallhavenSpider.items import WallhavenspiderItem
#已经爬取了 3834 页
class ImageinfodownloadSpider(scrapy.Spider):
    """
     爬取图片信息
    """
    name = 'imageInfoDownload'
    allowed_domains = ['alpha.wallhaven.cc']

    url = 'https://alpha.wallhaven.cc/random?page='
    offset = 1

    reqUrl = url + str(offset)

    start_urls = [reqUrl]


    def parse(self, response):
        """
         解析response
        :param response:
        :return:
        """

        imageId_list = response.xpath("//figure/@data-wallpaper-id")

        for imageid in imageId_list:
            #创建一个新的 item
            item = WallhavenspiderItem()

            id = imageid.extract()

            item['imageId'] = id

            imageinfo = response.xpath("//figure[@data-wallpaper-id="+id+"]")

            for imginfo in imageinfo:
                # //figure[@data-wallpaper-id="378330"]/img/@src
                item['imageThumbnailUrl'] = imginfo.xpath("./img/@data-src").extract()[0]
                #/div/span/text()
                item['imageSize'] = imginfo.xpath("./div/span/text()").extract()[0]
                #//figure[@data-wallpaper-id="378330"]/div/a[@title="Tags"]/@href
                item['imageTagUrl'] = imginfo.xpath('./div/a[@title="Tags"]/@href').extract()[0]
                #https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-634130.jpg
                #截取图片的后缀
                imgSuffix = item['imageThumbnailUrl'].split('.')[-1]
                item['imageDownloadUrl'] = 'https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-'+id+'.'+imgSuffix

            #交给管道文件进行处理
            yield item

        # 分页请求
        if self.offset < 3:
            self.offset += 1
        # else:
        #     raise "结束工作"

        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)





