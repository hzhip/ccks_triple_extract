# -*- coding: utf-8 -*-
# author: Jclian91
# place: Pudong Shanghai
# time: 2020-03-14 20:53
import os, re, json, traceback
from pprint import pprint

from triple_extract.triple_extractor import TripleExtract


text = "真人版的《花木兰》由新西兰导演妮基·卡罗执导，由刘亦菲、甄子丹、郑佩佩、巩俐、李连杰等加盟，几乎是全亚洲阵容。"
# text = "《冒险小王子》作者周艺文先生，教育、文学领域的专家学者以及来自全国各地的出版业从业者参加了此次沙龙，并围绕儿童文学创作这一话题做了精彩的分享与交流。"
# text = "宋应星是江西奉新人，公元1587年生，经历过明朝腐败至灭亡的最后时期。"
# text = "韩愈，字退之，河阳（今河南孟县）人。"
# text = "公开资料显示，李强，男，汉族，出生于1971年12月，北京市人，北京市委党校在职研究生学历，教育学学士学位，1996年11月入党，1993年7月参加工作。"
# text = "杨牧，本名王靖献，早期笔名叶珊，1940年生于台湾花莲，著名诗人、作家。"
# text = "杨广是隋文帝杨坚的第二个儿子。"
# text = "此次权益变动后，何金明与妻子宋琦、其子何浩不再拥有对上市公司的控制权。"
# text = "线上直播发布会中，谭维维首次演绎了新歌《章存仙》，这首歌由钱雷作曲、尹约作词，尹约也在直播现场透过手机镜头跟网友互动聊天。"
# text = "“土木之变”后，造就了明代杰出的民族英雄于谦。"
# text = "真纳大学坐落在巴基斯坦首都伊斯兰堡市，是一所创建于1967年7月的公立研究型大学。"
# text = "另外，哈尔滨历史博物馆也是全国面积最小的国有博物馆，该场馆面积只有50平方米，可称之“微缩博物馆”。"

triple_extract = TripleExtract(text)

entities = triple_extract.get_entity()
print("实体： ", end='')
pprint(entities)

spo_list = triple_extract.extractor()
print("三元组： ", end='')
pprint(spo_list)