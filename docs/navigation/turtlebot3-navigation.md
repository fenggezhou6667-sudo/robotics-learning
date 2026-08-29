# TurtleBot3 SLAM and Navigation

## Environment

- Ubuntu 22.04
- ROS2 Humble
- TurtleBot3 Burger
- Gazebo
- Nav2


## SLAM

使用 slam_toolbox 建图。

流程：

1. Launch simulation
2. Start slam_toolbox
3. Control robot exploration
4. Save map


## Map

Generated map:

- my_map.pgm
- my_map.yaml


## Navigation

Use Nav2:

ros2 launch turtlebot3_navigation2 navigation2.launch.py \
map:=my_map.yaml \
use_sim_time:=True


## Problems Solved

### 1. map frame missing

Reason:

map_server was not activated.

Solution:

Check lifecycle:

ros2 lifecycle get /map_server


### 2. AMCL cannot publish pose

Reason:

Initial pose was not set.

Solution:

Use RViz 2D Pose Estimate.


### 3. RobotModel missing

Reason:

RViz configuration mismatch.

Solution:

Use official TurtleBot3 RViz configuration.
