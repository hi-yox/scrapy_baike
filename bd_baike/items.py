# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item,Field



class MoreActorInfo(Item):
	name=Field() # 演员
	p_url=Field()
	v_name=Field() # 饰演角色
	v_desc=Field() # 描述
	v_test=Field()

class ActorInfo(Item):
	name=Field()	# 人物姓名
	pic=Field()  # 人物图片
	intro=Field()  # 百科简介

class VideoInfo(Item):
	key=Field()
	values=Field()
	

class BdBaikeItem(Item):
	keywords=Field()
	description=Field()
	hot_desc=Field()
	post_image=Field()
	main_actor_name=Field()
	video_info=Field()
	more_actor=Field()
	base_info=Field() # 基本信息









