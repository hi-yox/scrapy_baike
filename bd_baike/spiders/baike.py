# -*- coding: utf-8 -*-
import scrapy
from bd_baike.items import BdBaikeItem
from bd_baike.items import ActorInfo
from bd_baike.items import VideoInfo
from bd_baike.items import MoreActorInfo

class BaikeSpider(scrapy.Spider):
    name = 'baike'
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/缝纫机乐队/20242910']


    def parse(self, response):
		
		item=BdBaikeItem()
		person=ActorInfo()
		video_info=VideoInfo()

		# 视频发行信息简介
		video_info["key"]=response.selector.xpath("//dt[@class='basicInfo-item name']/text()").extract()
		basicInfo_value=response.selector.xpath("//dd[@class='basicInfo-item value']")
		values=[]
		for x in basicInfo_value:
			real_x=[]
			## 先判断x内部有没有超链接
			for yy in x.xpath("./a/text()").extract():
				yy_strip=yy.strip()
				if len(yy_strip)>=1:
					real_x.append(yy_strip)
			for xx in x.xpath("./text()").extract():
				xx_strip=xx.strip()
				tmp=xx_strip
				if len(xx_strip)>1 :
					real_x.append(tmp)
			values.append(",".join(real_x))
		video_info["values"]=values
		# 主要演职员表
		more_actor_xpath=response.selector.xpath("//dl[@class='info']")
		more_actor_arr=[]
		for x in more_actor_xpath:
			more_actor=MoreActorInfo()
			a=x.xpath("./dt/a[1]")
			more_actor["name"]=a.xpath("./text()").extract_first()
			more_actor["p_url"]=a.xpath("./@href").extract_first()


			v_name_tmp=x.xpath("./dt/text()").extract_first() # 先提取饰演内容，如果没有则从超链接中获取，如果有则截取出来
			v_name_tmp=v_name_tmp.split("饰".decode("utf-8"))[-1]
			if len(v_name_tmp)>1 :
				more_actor["v_name"]=v_name_tmp.strip()
			else:
				a=x.xpath("./dt/a[2]")
				more_actor["v_name"]=a.xpath("./text()").extract_first()


			more_actor_arr.append(more_actor)

		# 视频基本简介

		base_info=response.selector.xpath("//div[@label-module='lemmaSummary']")
		base_info_arr=[]
		for x in base_info:
			base_info_arr.append(x.xpath("./*").extract())
			base_info_arr.append(x.xpath("./text()").extract())

		

		person["name"]=response.selector.xpath("//a[@class='actor-name ']/text()").extract()
		person["pic"]=response.selector.xpath("//a[@class='actor-avatar ']/img//@src").extract()
		person["intro"]=response.selector.xpath("//a[@class='actor-name ']//@href").extract()

		item["keywords"]=response.selector.xpath("//meta[@name='keywords']/@content").extract()
		item["description"]=response.selector.xpath("//meta[@name='description']/@content").extract()
		item["hot_desc"]=response.selector.xpath("//div[@class='lemmaWgt-lemmaSummary lemmaWgt-lemmaSummary-light']//text()").extract()
		item["post_image"]=response.selector.xpath("//style/text()").re(r'https?://\w+\.\w+\.\w+')
		item["main_actor_name"]=person
		item["video_info"]=video_info
		item["more_actor"]=more_actor_arr
		item["base_info"]=base_info_arr
		yield item

