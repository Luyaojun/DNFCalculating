##辟邪玉属性部分

class 辟邪玉():
    名称 = ''
    最小值 = -5
    最大值 = 5
    间隔 = 0.1
    当前值 = 0
    def 进图属性(self, 属性):
        pass

class 辟邪玉0(辟邪玉):
    名称 = '无'
    最小值 = 0
    最大值 = 0

class 辟邪玉1(辟邪玉):
    名称 = '附加伤害增加增幅(待定)'
    def 进图属性(self, 属性):
        if 属性.附加伤害 >= 2:
            属性.附加伤害 += self.当前值 / 50
        else:
            属性.附加伤害 *= 1 + self.当前值 / 100

class 辟邪玉2(辟邪玉):
    名称 = '属性附加伤害增加增幅(待定)'
    def 进图属性(self, 属性):
        if 属性.属性附加 >= 2:
            属性.属性附加 += self.当前值 / 50
        else:
            属性.属性附加 *= 1 + self.当前值 / 100

class 辟邪玉3(辟邪玉):
    名称 = '技能伤害增加增幅'
    最小值 = -3
    最大值 = 3
    def 进图属性(self, 属性):
        属性.技能攻击力 = 1 + (属性.技能攻击力 - 1) * (1 + self.当前值 / 100)

class 辟邪玉4(辟邪玉):
    名称 = '暴击伤害增加增幅'
    def 进图属性(self, 属性):
        if 属性.暴击伤害 >= 2:
            属性.暴击伤害 += self.当前值 / 50
        else:
            属性.暴击伤害 *= 1 + self.当前值 / 100

class 辟邪玉5(辟邪玉):
    名称 = '伤害增加增幅'
    def 进图属性(self, 属性):
        if 属性.伤害增加 >= 2:
            属性.伤害增加 += self.当前值 / 50
        else:
            属性.伤害增加 *= 1 + self.当前值 / 100

class 辟邪玉6(辟邪玉):
    名称 = '最终伤害增加增幅'
    def 进图属性(self, 属性):
        if 属性.最终伤害 >= 2:
            属性.最终伤害 += self.当前值 / 50
        else:
            属性.最终伤害 *= 1 + self.当前值 / 100

class 辟邪玉7(辟邪玉):
    名称 = '力量智力增加增幅'
    def 进图属性(self, 属性):
        if 属性.百分比力智 >= 2:
            属性.百分比力智 += self.当前值 / 50
        else:
            属性.百分比力智 *= 1 + self.当前值 / 100

class 辟邪玉8(辟邪玉):
    名称 = '物理魔法攻击力增加增幅'
    def 进图属性(self, 属性):
        if 属性.百分比三攻 >= 2:
            属性.百分比三攻 += self.当前值 / 50
        else:
            属性.百分比三攻 *= 1 + self.当前值 / 100

class 辟邪玉9(辟邪玉):
    名称 = '所有属性强化增加'
    def 进图属性(self, 属性):
        属性.百分比属强 += self.当前值 / 100 #待测试

class 辟邪玉10(辟邪玉):
    名称 = '10~15技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 10, 15, self.当前值)
        pass

class 辟邪玉11(辟邪玉):
    名称 = '20~25技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 20, 25, self.当前值)
        pass

class 辟邪玉12(辟邪玉):
    名称 = '30~35技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 30, 35, self.当前值)
        pass
 
class 辟邪玉13(辟邪玉):
    名称 = '40~45技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 40, 45, self.当前值)
        pass
 
class 辟邪玉14(辟邪玉):
    名称 = '55~60技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 55, 60, self.当前值)
        pass
 
class 辟邪玉15(辟邪玉):
    名称 = '65~70技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 65, 70, self.当前值)
        pass
 
class 辟邪玉16(辟邪玉):
    名称 = '75~80技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 75, 80, self.当前值)
        pass
 
class 辟邪玉17(辟邪玉):
    名称 = '1次觉醒技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 50, 50, self.当前值)
        pass
 
class 辟邪玉18(辟邪玉):
    名称 = '2次觉醒技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1
    def 进图属性(self, 属性):
        属性.技能等级加成('所有', 85, 85, self.当前值)
        pass
 

辟邪玉列表 = []
i = 0
while i >= 0:
    try:
        exec('辟邪玉列表.append(辟邪玉'+str(i)+'())')
        i += 1
    except:
        i = -1

辟邪玉序号 = dict()
for i in range(len(辟邪玉列表)):
    辟邪玉序号[辟邪玉列表[i].名称] = i
