﻿from math import *

from PublicReference.base import *

class 刹那永恒主动技能(主动技能):
    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return round((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率,2)
    def 等效CD(self, 武器类型):
        if 武器类型 == '魔杖':
            return round(self.CD / self.恢复 * 1.0, 1)
        if 武器类型 == '法杖':
            return round(self.CD / self.恢复 * 1.1, 1)

class 刹那永恒技能0(刹那永恒主动技能):
    名称 = '冰魄剑'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 566
    成长 = 64.56
    攻击次数 = 2
    基础2 = 679.2
    成长2 = 77.47
    攻击次数2 = 1
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 7

class 刹那永恒技能1(被动技能):
    名称 = '冰武精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.01 * self.等级, 5)

class 刹那永恒技能2(刹那永恒主动技能):
    名称 = '寒冰连枪'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 1583
    成长 = 180.63
    CD = 3.0
    TP成长 = 0.10
    TP上限 = 7

class 刹那永恒技能3(刹那永恒主动技能):
    名称 = '冰魄旋枪'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3652
    成长 = 410.47
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 7

class 刹那永恒技能4(刹那永恒主动技能):
    名称 = '冰霜之径'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0

    def 属强加成(self):
        if self.等级 == 0:
            return 0
        else:
            return (30 + self.等级 * 4)

    def 加成倍率(self, 武器类型):
            return 1.0


class 刹那永恒技能5(被动技能):
    名称 = '冰之领悟'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return (1.02 + self.等级 * 0.01)
        else:
            return (1.12 + (self.等级 - 10) * 0.02)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return (1.02 + self.等级 * 0.01)
        else:
            return (1.12 + (self.等级 - 10) * 0.02)


class 刹那永恒技能6(刹那永恒主动技能):
    名称 = '冰魄之弓'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 5524
    成长 = 625.77
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7


class 刹那永恒技能7(刹那永恒主动技能):
    名称 = '破冰飞刃'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 5200.8
    成长 = 589.92
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 7

class 刹那永恒技能8(被动技能):
    名称 = '水晶剑'
    所在等级 = 30
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['冰魄剑']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return (1.25 + (self.等级-1) * 0.0125)


class 刹那永恒技能9(刹那永恒主动技能):
    名称 = '旋冰穿刺'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 7354
    成长 = 830
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 7


class 刹那永恒技能10(刹那永恒主动技能):
    名称 = '冰魄锤击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 8341
    成长 = 942
    CD = 18.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.27
        self.成长 *= 1.27

class 刹那永恒技能11(刹那永恒主动技能):
    名称 = '极冰绽放'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 1358
    成长 = 153.8
    攻击次数 = 4
    基础2 = 7250
    成长2 = 818.6
    攻击次数2 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.11
        self.成长 *= 1.11
        self.基础2 *= 1.23
        self.成长2 *= 1.23
        self.CD *= 0.90


class 刹那永恒技能12(刹那永恒主动技能):
    名称 = '冰雪风暴'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 789.3
    成长 = 89.26
    攻击次数 = 14
    基础2 = 7716
    成长2 = 871.29
    攻击次数2 = 1
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.攻击次数 = 16
        self.基础2 *= 1.15
        self.成长2 *= 1.15

class 刹那永恒技能13(被动技能):
    名称 = '冰封奥义'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)

class 刹那永恒技能14(刹那永恒主动技能):
    名称 = '千旋冰轮破'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 44922.72
    成长 = 13578.29
    CD = 145.0

class 刹那永恒技能15(刹那永恒主动技能):
    名称 = '冰凌破'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 18151
    成长 = 2046.1
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.22
        self.成长 *= 1.22

class 刹那永恒技能16(刹那永恒主动技能):
    名称 = '千里冰封'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 25834
    成长 = 2917
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.18667
        self.成长 *= 1.18667

class 刹那永恒技能17(被动技能):
    名称 = '冰之技艺'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['冰魄之弓','破冰飞刃','冰雪风暴','千旋冰轮破','冰凌破','千里冰封','极冰领域','永罪冰狱']
    关联技能2 = ['冰魄剑','寒冰连枪','冰魄旋枪','旋冰穿刺','冰魄锤击','极冰绽放','碎冰破']
    
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.16 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.24 + 0.03 * self.等级, 5)


class 刹那永恒技能18(刹那永恒主动技能):
    名称 = '碎冰破'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 45452
    成长 = 5132.0
    CD = 40.0

class 刹那永恒技能19(刹那永恒主动技能):
    名称 = '极冰领域'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 36582
    成长 = 4130.0
    CD = 40.0

class 刹那永恒技能20(刹那永恒主动技能):
    名称 = '永罪冰狱'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 75014
    成长 = 22647.0
    CD = 180.0

class 刹那永恒技能21(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 刹那永恒技能22(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 刹那永恒技能23(被动技能):
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

刹那永恒技能列表 = []
i = 0
while i >= 0:
    try:
        exec('刹那永恒技能列表.append(刹那永恒技能'+str(i)+'())')
        i += 1
    except:
        i = -1

刹那永恒技能序号 = dict()
for i in range(len(刹那永恒技能列表)):
    刹那永恒技能序号[刹那永恒技能列表[i].名称] = i

刹那永恒一觉序号 = 0
刹那永恒二觉序号 = 0
刹那永恒三觉序号 = 0
for i in 刹那永恒技能列表:
    if i.所在等级 == 50:
        刹那永恒一觉序号 = 刹那永恒技能序号[i.名称]
    if i.所在等级 == 85:
        刹那永恒二觉序号 = 刹那永恒技能序号[i.名称]
    if i.所在等级 == 100:
        刹那永恒三觉序号 = 刹那永恒技能序号[i.名称]

刹那永恒护石选项 = ['无']
for i in 刹那永恒技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        刹那永恒护石选项.append(i.名称)

刹那永恒符文选项 = ['无']
for i in 刹那永恒技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        刹那永恒符文选项.append(i.名称)


class 刹那永恒角色属性(角色属性):

    职业名称 = '刹那永恒'

    武器选项 = ['魔杖','法杖']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['魔法百分比']
    
    #默认
    伤害类型 = '魔法百力比'
    防具类型 = '皮甲'
    防具精通属性 = ['智力']

    主BUFF = 1.800
   
    #基础属性(含唤醒)
    基础力量 = 774.0
    基础智力 = 976.0
    
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
        self.技能栏= deepcopy(刹那永恒技能列表)
        self.技能序号= deepcopy(刹那永恒技能序号)


    def 伤害指数计算(self):
        self.冰属性强化 += self.技能栏[self.技能序号['冰霜之径']].属强加成()

        基准倍率 = 1.5 * self.主BUFF * (1 - 443243 / (443243 + 20000))

        面板 = (self.面板智力()/250+1) * (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻)

        self.火属性强化 = int(self.火属性强化 * (1+self.百分比属强))
        self.冰属性强化 = int(self.冰属性强化 * (1+self.百分比属强))
        self.光属性强化 = int(self.光属性强化 * (1+self.百分比属强))
        self.暗属性强化 = int(self.暗属性强化 * (1+self.百分比属强))
        if self.攻击属性 == 0:
            属性倍率=1.05+0.0045*max(self.火属性强化,self.冰属性强化,self.光属性强化,self.暗属性强化)
        elif self.攻击属性 == 1:
            属性倍率=1.05+0.0045*self.火属性强化
        elif self.攻击属性 == 2:
            属性倍率=1.05+0.0045*self.冰属性强化
        elif self.攻击属性 == 3:
            属性倍率=1.05+0.0045*self.光属性强化
        elif self.攻击属性 == 4:
            属性倍率=1.05+0.0045*self.暗属性强化
        增伤倍率=1+self.伤害增加
        增伤倍率*=1+self.暴击伤害
        增伤倍率*=1+self.最终伤害
        增伤倍率*=self.技能攻击力
        增伤倍率*=1+self.持续伤害*(1-0.1*self.持续伤害计算比例)
        增伤倍率*=1+self.附加伤害+self.属性附加*属性倍率
        self.伤害指数=面板*属性倍率*增伤倍率*基准倍率/100
           
    def 冰属性强化加成(self):
        冰属性强化值 = 0
        for i in self.技能栏:
            if i.名称 != '冰霜之径':
              冰属性强化值 += 0
            else:
              冰属性强化值 += i.属强加成()
        return (冰属性强化值)

    def 装备属性计算(self):
        self.装备基础()

        for i in self.装备栏:
            装备列表[装备序号[i]].城镇属性(self)
            装备列表[装备序号[i]].进图属性(self)

        for i in self.套装栏:
            套装列表[套装序号[i]].城镇属性(self)
            套装列表[套装序号[i]].进图属性(self)

        for i in self.装备栏:
            if 装备列表[装备序号[i]].名称 == '奔流不息之伽蓝':
                if self.技能栏[self.技能序号['冰之技艺']].等级 != 0:
                    self.技能栏[self.技能序号['极冰绽放']].基础 *= (1 + 10 / 7 * (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24)) / (
                                (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24) + 1)
                    self.技能栏[self.技能序号['极冰绽放']].成长 *= (1 + 10 / 7 * (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24)) / (
                                (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24) + 1)
                    self.技能栏[self.技能序号['极冰绽放']].基础2 *= (1 + 10 / 7 * (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24)) / (
                                (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24) + 1)
                    self.技能栏[self.技能序号['极冰绽放']].成长2 *= (1 + 10 / 7 * (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24)) / (
                                (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24) + 1)
            if 装备列表[装备序号[i]].名称 == '奔流不息之山川':
                if self.技能栏[self.技能序号['冰之技艺']].等级 != 0:
                    self.技能栏[self.技能序号['冰魄锤击']].基础 *= (1 + 10 / 7 * (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24)) / (
                                (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24) + 1)
                    self.技能栏[self.技能序号['冰魄锤击']].成长 *= (1 + 10 / 7 * (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24)) / (
                                (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24) + 1)
                    self.技能栏[self.技能序号['旋冰穿刺']].基础 *= (1 + 10 / 7 * (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24)) / (
                                (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24) + 1)
                    self.技能栏[self.技能序号['旋冰穿刺']].成长 *= (1 + 10 / 7 * (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24)) / (
                                (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24) + 1)
            if 装备列表[装备序号[i]].名称 == '奔流不息之银河':
                if self.技能栏[self.技能序号['冰之技艺']].等级 != 0:
                    self.技能栏[self.技能序号['冰魄旋枪']].基础 *= (1 + 10 / 7 * (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24)) / (
                                (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24) + 1)
                    self.技能栏[self.技能序号['冰魄旋枪']].成长 *= (1 + 10 / 7 * (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24)) / (
                                (self.技能栏[self.技能序号['冰之技艺']].等级 * 0.03 + 0.24) + 1)


class 刹那永恒(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 刹那永恒角色属性()
        self.角色属性A = 刹那永恒角色属性()
        self.角色属性B = 刹那永恒角色属性()
        self.一觉序号 = 刹那永恒一觉序号
        self.二觉序号 = 刹那永恒二觉序号
        self.三觉序号 = 刹那永恒三觉序号
        self.护石选项 = deepcopy(刹那永恒护石选项)
        self.符文选项 = deepcopy(刹那永恒符文选项)

    def 站街计算(self,装备名称,套装名称):
        C = deepcopy(self.角色属性A)
        C.技能栏 = deepcopy(self.角色属性A.技能栏)
        C.穿戴装备(装备名称,套装名称)
        for i in C.装备栏:
            装备列表[装备序号[i]].城镇属性(C)
        for i in C.套装栏:
            套装列表[套装序号[i]].城镇属性(C)
        C.装备基础()

        C.冰属性强化 += C.冰属性强化加成()
        
        return C
