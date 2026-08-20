# Robotics Learning Journey

用于记录机器人实验室项目学习过程，包括 ROS2、Gazebo 仿真、SLAM 建图、Nav2 自主导航以及机器人应用开发。

---

# ROS2 Learning Journey

## Environment

- Ubuntu 22.04
- ROS2 Humble
- Python 3.10
- Gazebo
- TurtleBot3 Burger

---

# Stage 1: ROS2 Basics

Completed:

- Node
- Topic
- Service
- Action
- Parameter

Learned basic ROS2 communication mechanisms and system architecture.

---

# Stage 2: ROS2 Engineering

Completed:

- Create ROS2 package
- colcon build
- Launch file
- Workspace management

Package:

my_robot_demo

---

# Stage 3: rclpy Programming

Implemented ROS2 Python nodes.

## move_turtle.py

A ROS2 publisher node controlling robot velocity.

Topic:

/turtle1/cmd_vel

Functions:

- Publish velocity commands
- Control robot movement


## turtle_pose.py

A ROS2 subscriber node receiving robot pose information.

Topic:

/turtle1/pose

Functions:

- Subscribe robot state
- Process position information


---

# Stage 4: Gazebo Simulation

Completed:

- TurtleBot3 simulation environment setup
- ROS2 and Gazebo communication
- Robot model loading
- Sensor data verification

Platform:

TurtleBot3 Burger

Verified:

- Differential drive control
- Laser scan data
- TF coordinate transformation

---

# Stage 5: SLAM Mapping

Completed:

- SLAM Toolbox configuration
- Environment exploration
- 2D occupancy grid map generation
- Map saving

Generated map files:

maps/
├── my_map.yaml
└── my_map.pgm

The generated map can be reused for autonomous navigation.

---

# Stage 6: Nav2 Autonomous Navigation

Completed:

- Load saved map using map_server
- Configure Navigation2 stack
- AMCL localization
- TF transformation verification

Main components:

map_server
amcl
planner_server
controller_server
global_costmap
local_costmap

Verified:

- Map loading
- Robot localization
- Navigation framework startup


---

# Debugging Notes

During the Nav2 deployment process, several issues were solved:

## 1. Missing map frame

Problem:

Invalid frame ID "map"

Solution:

- Check map_server lifecycle state
- Verify /map topic publishing


## 2. AMCL localization failure

Problem:

AMCL cannot publish a pose

Solution:

- Set initial pose in RViz
- Check TF relationship


## 3. RViz configuration compatibility

Problem:

- Different Nav2 versions caused RViz plugin loading errors

Solution:

- Use compatible TurtleBot3 Navigation2 RViz configuration


---

# Repository Structure

robotics-learning
├── README.md
│
├── maps
│   ├── my_map.yaml
│   └── my_map.pgm
│
├── notes
│   └── ros2_navigation.md
│
├── rviz
│   └── README.md
│
└── screenshots
    ├── slam_result.png
    └── navigation_result.png

---

# Future Plan

## Autonomous Navigation

- Complete custom Gazebo world
- Implement Nav2 goal navigation
- Develop multi-point navigation node using rclpy
- Learn ROS2 Action interface


## Robot Perception

- Camera perception
- LiDAR processing
- Object detection
- Sensor fusion


## Advanced Robotics

- Robot control
- Autonomous systems
- Embodied intelligence
- Multi-modal perception
