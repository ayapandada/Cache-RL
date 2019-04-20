import gym
from gym.envs.classic_control import rendering #图像引擎

import numpy as np

class GridEnv(gym.Env):
    def __init__(self,world_w=4,world_h=2,pixel_size=20,default_type=0):
        self.length=world_h*world_w
        self.state = [i for i in range(self.length)]
        #self.statecom=self.state.reshape(world_w,world_h)
        #print(self.statecom)
        self.action=['n','w','e','s','nw','ne','sw','se']
        self.changestate_action = {'n':-world_w, 'e':1, 's':world_w, 'w':-1,'nw':-(world_w+1),'ne':-(world_w-1),'sw':world_w-1,'se':world_w+1}
        self.destination=[6] #先假设位置10是目的地
        #self.user2des=[8] #假设另一个用户的目的地址移动轨迹（或者是缓存放置位置）(多位置的奖励应该怎么写呢)'''
        
        self.user2Cache=[0,5,8] 
        self.CacheFavorite=[1,2,3] #缓存内容感兴趣程度等级5-0
        #self.scope=1  #假设覆盖范围之后再考虑

        self.viewer = rendering.Viewer(800, 400)   # 600x400 是画板的长和框
        self.gamma = 0.8         #折扣因子


    def dynamic_step(self):

        next_state = s
        #\只是一行太长了进行换行...
        if ((s < world_w  and (a == 'n' or a=='nw' or a=='ne')) or (s % world_w == 0 and (a == 'w' or a=='nw' or a=='sw'))\
        or (s > length - world_w - 1 and (a == 's'or a=='sw' or a=='se')) or ((s+1) % world_w == 0 and (a == 'e'or a=='ne' or a=='se'))): 
        #保证没有走出定义的格子世界,并且状态是从0开始到length-1
                pass
        else:
            next_state =  s + changestate_action[a]
        if s in self.destination:  #需要之后根据具体情况给出is_end的终止条件(这里假设达到了目的地就结束)
            is_end=true
        else:
            is_end=false 
        reward=getreward(s)
        return next_state, reward, is_end

    
    def getReward(self):
        s=self.sate
        r=[]
        if s in self.distance: 		#在特定位置给出reward
            return 10 				#需要对到达目的地给一个更大的奖励来避免停留在cache点
        else:		#根据与Cache点的曼哈顿距离给出奖励
            for i in self.user2Cache:
                difference=abs(s-i) 		#需要取绝对值
                updown=difference/world_w 		#需要取整
                leftright=difference%world_w 		#左右距离 
                distance=updown+leftright
                r.append(distance)
        for x in r:
            rew+=x
        return rew

    def getAction(self):
        return self.actions

#**********************************************这是一条很长的分割线******************************************************
    #metadata{'rendermode','anis','human'}
    #编写图像引擎部分进行显示
    def render(self, mode='human', close=False): 
         # 可视化地图
        lines = []
        line1 = rendering.Line((0, 0), (0, 200))
        lines.append(line1)
        line2 = rendering.Line((120, 0), (120, 200))
        lines.append(line2)
        line3 = rendering.Line((0, 200), (600, 200))
        lines.append(line3)
        line4 = rendering.Line((0, 100), (600, 100))
        lines.append(line4)
        line5 = rendering.Line((240, 0), (240, 200))
        lines.append(line5)
        line6 = rendering.Line((360, 0), (360, 200))
        lines.append(line6)
        line7 = rendering.Line((480, 0), (480, 200))
        lines.append(line7)
        line8 = rendering.Line((600, 0), (600, 200))
        lines.append(line8)
        line9 = rendering.Line((0, 0), (120, 0))
        lines.append(line9)
        line10 = rendering.Line((240, 0), (360, 0))
        lines.append(line10)
        line11 = rendering.Line((480, 0), (600, 0))
        lines.append(line11)

    # 创建terminal
        terminals = []
        termin = rendering.make_circle(40)
        circletrans = rendering.Transform(translation=(300, 50))
        terminals.add_attr(circletrans)
        terminals.set_color(1, 0.9, 0)
        terminals.append(termin)


    # 创建building
        buildings = []
        building1 = rendering.make_circle(40)
        building1_transiform = rendering.Transform(translation=(60, 50))
        building1.add_attr(building1_transiform)
        building1.set_color(0, 0, 0)
        buildings.append(building1)

        building2 = rendering.make_circle(40)
        building2_transiform = rendering.Transform(translation=(540, 50))
        building2.add_attr(building2_transiform)
        building2.set_color(0, 0, 0)
        buildings.append(building2)

    #创建
        transiform = rendering.Transform(translation=(50, 50))
        for line_ in lines:
            line_.set_color(0, 0, 0)
            line_.add_attr(transiform)
            self.viewer.add_geom(line_)
        for building_ in buildings:
            building_.add_attr(transiform)
            self.viewer.add_geom(building_)
        for terminal_ in terminals:
            terminal_.add_attr(transiform)
            self.viewer.add_geom(terminal_)

        return self.viewer.render(return_rgb_array=mode == 'rgb_array')


if __name__ == '__main__':
    t = GridEnv()
    while True:
        t.render()