#########ros2常见缩写
cmd	command
vel	velocity
odom	odometry
imu	Inertial Measurement Unit
lidar	Light Detection And Ranging
slam	Simultaneous Localization And Mapping
nav	navigation

命令 ros2 + 接口 +list 查询


 
一  #节点（node）
自行发布第一个节点
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 1.0}}"

二  #话题（topic)长时间持续发送，连续变化的数据流

三  #服务（service）一次性
ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.0, y: 5.0, theta: 0, name: turtle2}"

四  #action（结构，类型），适用于任务
包含三部分
Goal（目标）
Feedback（反馈）
Result（结果）
 
五  #parameter（参数）param
get获取  set调整 +接口名称



六  #launch（一个自动启动多个ROS节点的脚本）
成功创建自己的launch文件：小乌龟脚本

工作空间
目录：
ros2_ws

├── src
│
├── build
│
├── install
│
└── log
其中：
src：
放源码。
build：
编译过程。
install：
编译后的程序。
log：
日志。
    
七   创建第一个luanch文件的过程中出现的问题：
#colcon包功能忘记下载
#创建文件时误将文件创建在ws根目录下
#修改setup文件时未导入os导致编译失败

整体结构：Node
  |
  | 被Launch启动
  |
Topic / Service / Action通信
  |
Parameter配置





第八阶段：ROS2 Python节点——Subscriber（订阅）
写一个“自动追踪目标点的小乌龟”
