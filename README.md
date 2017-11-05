# 百度百科电影资源爬取

## 1、构造基本数据Item
## 2、随便取一部电影资源的url作为开始爬取url
## 3、通过获取第一个爬取资源的基本数据（里面可能包含其他电影数据，构建Request继续爬取），如果不需要特别复杂的数据，基本上能够爬取所有百科电影资源
## 4、由于电影中包含很多人名，利用人和人之间的关联也能爬取所有的百科明星
## 5、其他数据的爬取原理也大致相同

## 基本数据

```json
[
  {
    "base_info": [
      [
      《缝纫机乐队》是由他城影业、儒意影业、青春光线、万达影业、乐合影业出品，由执导，董成鹏、乔杉、古力娜扎、李鸿其、韩童生、曲隽希等主演的喜剧电影。该片讲述了胡亮的家乡小镇集安，几个背景各异的小人物为了追寻共同的音乐梦想，组建了一支与众不同的摇滚乐队的故事。影片于2017年9月29日在中国内地上映"
      ],
    ],
    "description": [
      "《缝纫机乐队》是由他城影业、儒意影业、青春光线、万达影业、乐合影业出品，由董成鹏执导，董成鹏、乔杉、古力娜扎、李鸿其、韩童生、曲隽希等主演的喜剧电影。该片讲述了胡亮的家乡小镇集安，几个背景各异的小人物为了追寻共同的音乐梦想，组建了一支与众不同的摇滚乐队的故事。影片于2..."
    ],
    "main_actor_name": {
      "pic": [
        "https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/whfpf%3D82%2C102%2C50/sign=a9a1e230a3d3fd1f365cf17a56731d2d/2fdda3cc7cd98d102ac37d2f2a3fb80e7bec909c.jpg",
        "https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/whfpf%3D82%2C102%2C50/sign=40fdcf5f432309f7e73afe52143334c1/cefc1e178a82b901452719f8768da9773812ef77.jpg",
        "https://gss1.bdstatic.com/-vo3dSag_xI4khGkpoWK1HF6hhy/baike/whfpf%3D82%2C102%2C50/sign=d49e135665061d957d1364781dc932e3/7a899e510fb30f243f38866dc395d143ad4b0339.jpg",
        "https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/whfpf%3D82%2C102%2C50/sign=ca4ef814c195d143da23b76315cdba30/32fa828ba61ea8d375f660139e0a304e241f58d4.jpg"
      ],
      "intro": [
        "http://baike.baidu.com/item/董成鹏/5700623",
        "http://baike.baidu.com/item/乔杉/4102789",
        "http://baike.baidu.com/item/古力娜扎/5724495",
        "http://baike.baidu.com/item/李鸿其/18112482"
      ],
      "name": [
        "董成鹏",
        "乔杉",
        "古力娜扎",
        "李鸿其"
      ]
    },
    "video_info": {
      "values": [
        "缝纫机乐队",
        "City of Rock",
        "2017年",
        "他城影业、儒意影业、青春光线、万达影业、乐合影业",
        "中国大陆",
        "北京,集安,、吉林",
        "董成鹏",
        "董成鹏,苏彪",
        "陈祉希",
        "喜剧、剧情",
        "董成鹏，乔杉，古力娜扎，李鸿其，韩童生，曲隽希",
        "140分钟",
        "2017年9月29日",
        "普通话",
        "彩色"
      ],
      "key": [
        "中文名",
        "外文名",
        "出品时间",
        "出品公司",
        "制片地区",
        "拍摄地点",
        "导    演",
        "编    剧",
        "制片人",
        "类    型",
        "主    演",
        "片    长",
        "上映时间",
        "对白语言",
        "色    彩"
      ]
    },
    "more_actor": [
      {
        "v_name": "程宫",
        "name": "董成鹏",
        "p_url": "/item/%E8%91%A3%E6%88%90%E9%B9%8F/5700623"
      },
      {
        "v_name": "胡亮",
        "name": "乔杉",
        "p_url": "/item/%E4%B9%94%E6%9D%89/4102789"
      },
      {
        "v_name": "丁建国",
        "name": "古力娜扎",
        "p_url": "/item/%E5%8F%A4%E5%8A%9B%E5%A8%9C%E6%89%8E/5724495"
      },
      {
        "v_name": "炸药",
        "name": "李鸿其",
        "p_url": "/item/%E6%9D%8E%E9%B8%BF%E5%85%B6/18112482"
      },
      {
        "v_name": "杨双树",
        "name": "韩童生",
        "p_url": "/item/%E9%9F%A9%E7%AB%A5%E7%94%9F/2012748"
      },
      {
        "v_name": "希希",
        "name": "曲隽希",
        "p_url": "/item/%E6%9B%B2%E9%9A%BD%E5%B8%8C/9227874"
      },
      {
        "v_name": "彤彤/丽丽",
        "name": "周冬雨",
        "p_url": "/item/%E5%91%A8%E5%86%AC%E9%9B%A8/5051740"
      },
      {
        "v_name": "孙大力",
        "name": "于谦",
        "p_url": "/item/%E4%BA%8E%E8%B0%A6/1533903"
      },
      {
        "v_name": "希希妈",
        "name": "代乐乐",
        "p_url": "/item/%E4%BB%A3%E4%B9%90%E4%B9%90/3097698"
      },
      {
        "v_name": "煎饼摊老板娘",
        "name": "袁姗姗",
        "p_url": "/item/%E8%A2%81%E5%A7%97%E5%A7%97/936741"
      },
      {
        "v_name": "茜茜",
        "name": "宋茜",
        "p_url": "/item/%E5%AE%8B%E8%8C%9C/2355394"
      },
      {
        "v_name": "乔大山",
        "name": "岳云鹏",
        "p_url": "/item/%E5%B2%B3%E4%BA%91%E9%B9%8F/2190336"
      },
      {
        "v_name": "张发财",
        "name": "于洋",
        "p_url": "/item/%E4%BA%8E%E6%B4%8B/6260468"
      },
      {
        "v_name": "胡亮",
        "name": "曹桐睿",
        "p_url": "/item/%E6%9B%B9%E6%A1%90%E7%9D%BF/20411834"
      },
      {
        "v_name": "叶世荣",
        "name": "叶世荣",
        "p_url": "/item/%E5%8F%B6%E4%B8%96%E8%8D%A3/144376"
      },
      {
        "v_name": "黄贯中",
        "name": "黄贯中",
        "p_url": "/item/%E9%BB%84%E8%B4%AF%E4%B8%AD/141768"
      },
      {
        "v_name": "宋小宝",
        "name": "宋小宝",
        "p_url": "/item/%E5%AE%8B%E5%B0%8F%E5%AE%9D/1274312"
      },
      {
        "v_name": "刘小光",
        "name": "刘小光",
        "p_url": "/item/%E5%88%98%E5%B0%8F%E5%85%89/30269"
      },
      {
        "v_name": "宋晓峰",
        "name": "宋晓峰",
        "p_url": "/item/%E5%AE%8B%E6%99%93%E5%B3%B0/73999"
      },
      {
        "v_name": "文松",
        "name": "文松",
        "p_url": "/item/%E6%96%87%E6%9D%BE/12592997"
      },
      {
        "v_name": "赵英俊",
        "name": "赵英俊",
        "p_url": "/item/%E8%B5%B5%E8%8B%B1%E4%BF%8A/1036473"
      }
    ],
    "post_image": [
      "https://gss3.bdstatic.com",
      "https://bkssl.bdimg.com",
      "https://bkssl.bdimg.com",
      "https://bkssl.bdimg.com"
    ],
    "keywords": [
      "缝纫机乐队 缝纫机乐队剧情简介 缝纫机乐队演职员表 缝纫机乐队角色介绍 缝纫机乐队音乐原声 缝纫机乐队幕后花絮 缝纫机乐队幕后制作 缝纫机乐队制作发行 缝纫机乐队影片评价 大鹏的《缝纫机乐队》很努力，但只有努力还不够"
    ],
    "hot_desc": [
      "\n《缝纫机乐队》是由他城影业、儒意影业、青春光线、万达影业、乐合影业出品，由董成鹏执导，董成鹏、乔杉、古力娜扎、李鸿其、韩童生、曲隽希等主演的喜剧电影。该片讲述了胡亮的家乡小镇集安，几个背景各异的小人物为了追寻共同的音乐梦想，组建了一支与众不同的摇滚乐队的故事。影片于2017年9月29日在中国内地上映。\n\n",
      ">>>",
      "\n"
    ]
  }
]
```