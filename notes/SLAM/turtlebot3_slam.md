# TurtleBot3 SLAM学习记录

## 1. 环境

- ROS2 Humble
- Gazebo
- TurtleBot3 Burger
- slam_toolbox

---

## 2. SLAM流程

启动机器人：

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
启动键盘控制：
ros2 run teleop_twist_keyboard teleop_twist_keyboard
启动SLAM：
ros2 launch slam_toolbox online_async_launch.py
 
重要Topic
查看：
ros2 topic list
主要：
/scan
/odom
/tf
/map


遇到的问题
问题1
激光雷达显示异常。
原因：
TF时间不同步。
检查：
ros2 topic hz /scan
问题2
保存地图失败。
原因：
map_server生命周期节点未激活。
解决：
确认：
ros2 topic echo /map --once
然后：
ros2 run nav2_map_server map_saver_cli -f ~/my_map


学习总结
理解：
SLAM不是直接生成地图，而是通过：激光数据
里程计
TF关系

不断优化机器人位姿和地图。

保存：

Ctrl+O

回车

Ctrl+X

---

# 四、创建 Navigation2 笔记

```bash
nano notes/Navigation2/turtlebot3_nav2.md
写：
# TurtleBot3 Navigation2学习记录


## SLAM和导航区别

SLAM:

同时定位和建图。

输出：

map


Navigation2:

已有地图后：

定位 + 路径规划。


---

## 导航流程

地图：

map_server

定位：

AMCL

规划：

planner_server

控制：

controller_server


---

## TF关系

正确结构：

map
 |
odom
 |
base_footprint
 |
base_link


检查：

```bash
ros2 run tf2_tools view_frames
AMCL定位
查看：
ros2 topic echo /amcl_pose --once
输出：
frame_id: map
说明定位成功。
RViz问题总结
官方tb3_navigation2.rviz:
包含完整插件配置。
自己创建RViz:
需要手动添加:
Map
RobotModel
TF
LaserScan
并且需要正确Topic和Fixed Frame。

---

# 五、保存地图文件

你的地图：

my_map.yaml
my_map.pgm

复制：

```bash
cp ~/my_map.yaml maps/

cp ~/my_map.pgm maps/
检查：
ls maps
应该：
my_map.yaml
my_map.pgm

