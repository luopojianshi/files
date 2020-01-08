## 教育网站项目分析

## 校长端
```
域名: https://www.initwords.com/teacherlogin.jsp
账号: hzxhdcy001
密码: hzxhdcy001
需求：
    1、个人面板
    2、我的信息模块
    3、学习管理模块
    4、系统设置模块
```


##### 登录页
```
1、首页
2、帮助
3、关于我们
4、登录窗口
5、版权相关
```
##### 个人面板
```
1、欢迎登录
2、临近课程（分页长列表）
```
##### 学员面板
```
1、请选择（空白）
2、内容展示（空白）
```
##### 我的信息
```
1、个人信息
2、修改密码
```
##### 学习管理
```
1、班级列表（分页长列表，具有新增、保存、取消、删除功能）
2、学生名册
	请选择班级（选择班级展示学生名册）
	学生名册（分页长列表，具有注册课程、测试记录、查找学员、添加/删除学员、兑换突击币、金币总量按钮）
3、学习统计
	统计说明
	请选择班级（班级、训练量、词汇量、学习时间、训练&词汇、其他）
	柱状图（训练量、词汇量、学习时间、）、柱状图+折线图（训练&词汇）
	单词学习时间统计（柱状图）
4、单词比赛（分页列表，具有创建比赛、比赛控制、单词导入、删除比赛功能）
```

```
补充：
	注册课程：较复杂表单，判断耗时较长，0.5~1天
	测试记录：分页短列表
	添加/删除学员：简单表单
	比赛控制：参数设置、启动比赛、限时计量赛、限量枪时赛、结束比赛，没看懂这个比赛的游戏规则），判断耗时较长，0.5~1天
	单词导入：简单表单
```

##### 系统设置

```
退出
```
