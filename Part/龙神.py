from PublicReference.base import *

class 龙神技能0(被动技能):
    名称 = '基础精通'
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['龙人剑术']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.472 + 0.0889 * self.等级, 5)

class 龙神技能1(主动技能):
    名称 = '龙人剑术'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    基础 = 1159.00
    成长 = 0
    CD = 3.0
    TP成长 = 0.10
    TP上限 = 5

class 龙神技能2(主动技能):
    名称 = '火焰吐息'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2116.1333
    成长 = 238.8667
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 7

class 龙神技能3(主动技能):
    名称 = '龙翼突袭'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2645.1905
    成长 = 298.8095
    CD = 4.0
    TP成长 = 0.10
    TP上限 = 7

class 龙神技能4(主动技能):
    名称 = '龙语召唤：阿斯特拉'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    基础 = 2279.5263
    成长 = 432.4737
    CD = 7.0
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 20:
            return round(1.05 + 0.005 * self.等级, 5)
        else:
            return round(0.75 + 0.02 * self.等级, 5)

    def 独立攻击力倍率进图(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 20:
            return round(1.05 + 0.005 * self.等级, 5)
        else:
            return round(0.75 + 0.02 * self.等级, 5)

class 龙神技能5(主动技能):
    名称 = '爆破龙角'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 4585.2750
    成长 = 517.7250
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7

class 龙神技能6(主动技能):
    名称 = '龙拳'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4128.7027
    成长 = 466.2973
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7

class 龙神技能7(主动技能):
    名称 = '龙拳(空中释放)'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4400.9730
    成长 = 497.0270
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7


class 龙神技能8(主动技能):
    名称 = '龙之撕咬'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4873.6216
    成长 = 550.3784
    CD = 10
    TP成长 = 0.10
    TP上限 = 7

class 龙神技能9(主动技能):
    名称 = '龙翼穿刺(2hit+踢击)'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 6022.0857
    成长 = 679.9143
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 7

class 龙神技能10(主动技能):
    名称 = '龙翼穿刺(撕咬)'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 6387.8286
    成长 = 721.1714
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 7

class 龙神技能11(主动技能):
    名称 = '飞龙斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 8885.7714
    成长 = 1003.2286
    CD = 13.5
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.2532

class 龙神技能12(被动技能):
    名称 = '大胃王'
    所在等级 = 35
    等级上限 = 25
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.0 + 0.01 * self.等级, 5)
        else:
            return round(0.9 + 0.02 * self.等级, 5)

class 龙神技能13(主动技能):
    名称 = '龙刃无双'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 13035.1563
    成长 = 1470.8438
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.28

class 龙神技能14(主动技能):
    名称 = '魔龙之息'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 17907.0667
    成长 = 2021.9333
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.22

class 龙神技能15(被动技能):
    名称 = '魔龙之力'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)

class 龙神技能16(主动技能):
    名称 = '魔龙之力(火球)'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    基础 = 785.8421
    成长 = 149.1579
    CD = 3.0
    TP上限 = 0

    def 火球等级(self):
        super().火球等级()
        self.技能栏[self.技能序号['魔龙之力(火球)']].等级 = self.技能栏[self.技能序号['魔龙之力']].等级

    def 火球(self, 武器类型):
        return (self.基础 + self.成长 * self.等级) * self.倍率

class 龙神技能17(主动技能):
    名称 = '雷光嘶吼'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 42854.742
    成长 = 14123.86
    CD = 145

class 龙神技能18(主动技能):
    名称 = '龙皇制裁'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 18569.4091
    成长 = 2096.5909
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.23

class 龙神技能19(主动技能):
    名称 = '魔龙天翔(脱手)'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 26653.6471
    成长 = 3009.3529
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.18

class 龙神技能20(主动技能):
    名称 = '魔龙天翔(空中释放)'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 32651.4706
    成长 = 3686.5294
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.23

class 龙神技能21(被动技能):
    名称 = '龙神血脉'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.21 + 0.02 * self.等级, 5)

class 龙神技能22(主动技能):
    名称 = '魔龙星落'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 49844.8667
    成长 = 5628.1333
    CD = 40.0

class 龙神技能23(主动技能):
    名称 = '征战无双'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 55975.1667
    成长 = 6319.8333
    CD = 50.0

class 龙神技能24(主动技能):
    名称 = '龙神裁决：终末之光'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 114938
    成长 = 34700.0000
    CD = 180

class 龙神技能25(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 龙神技能26(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 龙神技能27(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

龙神技能列表 = []
i = 0
while i >= 0:
    try:
        exec('龙神技能列表.append(龙神技能'+str(i)+'())')
        i += 1
    except:
        i = -1

龙神技能序号 = dict()
for i in range(len(龙神技能列表)):
    龙神技能序号[龙神技能列表[i].名称] = i

龙神一觉序号 = 0
龙神二觉序号 = 0
龙神三觉序号 = 0
for i in 龙神技能列表:
    if i.所在等级 == 50:
        龙神一觉序号 = 龙神技能序号[i.名称]
    if i.所在等级 == 85:
        龙神二觉序号 = 龙神技能序号[i.名称]
    if i.所在等级 == 100:
        龙神三觉序号 = 龙神技能序号[i.名称]

龙神护石选项 = ['无']
for i in 龙神技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        龙神护石选项.append(i.名称)

龙神符文选项 = ['无']
for i in 龙神技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        龙神符文选项.append(i.名称)

class 龙神角色属性(角色属性):

    职业名称 = '龙神'

    武器选项 = ['太刀','钝器','巨剑','短剑']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['物理固伤']
    
    #默认
    伤害类型 = '物理固伤'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 1.850
   
    #基础属性(含唤醒)
    基础力量 = 923.0
    基础智力 = 827.0
    
    #适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    #人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
  
    def __init__(self):
        self.技能栏= deepcopy(龙神技能列表)
        self.技能序号= deepcopy(龙神技能序号)

class 龙神(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 龙神角色属性()
        self.角色属性A = 龙神角色属性()
        self.角色属性B = 龙神角色属性()
        self.一觉序号 = 龙神一觉序号
        self.二觉序号 = 龙神二觉序号
        self.三觉序号 = 龙神三觉序号
        self.护石选项 = deepcopy(龙神护石选项)
        self.符文选项 = deepcopy(龙神符文选项)
