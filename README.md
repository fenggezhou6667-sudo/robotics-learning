# Robotics Learning Journey

A reproducible ROS 2 Humble learning workspace for turtlesim, TurtleBot3
simulation, SLAM mapping, RViz, and Nav2 navigation.

The repository combines small ROS 2 Python examples with experiment notes and
configuration assets. Detailed procedures live in `docs/`; this README is the
project entry point.

## Environment

- Ubuntu 22.04
- ROS 2 Humble
- Python 3.10
- Gazebo
- TurtleBot3 Burger

## Learning progress

- [x] ROS 2 nodes, topics, services, actions, and parameters
- [x] Ament Python packages and `colcon` workspace management
- [x] Publishers and subscribers with `rclpy`
- [x] TurtleBot3 Gazebo simulation
- [x] SLAM Toolbox mapping
- [x] Map saving and reuse
- [x] Nav2 startup and AMCL localization
- [ ] Custom Gazebo world
- [ ] Nav2 goal and multi-point navigation nodes
- [ ] Camera and LiDAR perception
- [ ] Object detection and sensor fusion

## Repository structure

```text
robotics-learning/
├── assets/
│   ├── maps/
│   └── rviz/
├── docs/
│   ├── navigation/
│   ├── slam/
│   └── troubleshooting/
└── src/
    └── my_robot_demo/
        ├── launch/
        ├── my_robot_demo/
        ├── resource/
        └── test/
```

## Quick start

Clone the repository and install declared ROS dependencies:

```bash
git clone https://github.com/fenggezhou6667-sudo/robotics-learning.git
cd robotics-learning

source /opt/ros/humble/setup.bash
rosdep install --from-paths src --ignore-src -r -y
```

Build and source the workspace:

```bash
colcon build --symlink-install
source install/setup.bash
```

Launch turtlesim together with the publisher and pose subscriber:

```bash
ros2 launch my_robot_demo demo.launch.py
```

The movement node is configurable through ROS parameters:

```bash
ros2 run my_robot_demo move_turtle --ros-args \
  -p linear_velocity:=1.0 \
  -p angular_velocity:=0.5 \
  -p publish_period:=0.5
```

Run the package tests:

```bash
colcon test --packages-select my_robot_demo
colcon test-result --verbose
```

## TurtleBot3 assets

Saved maps are in `assets/maps/`. RViz configurations are in
`assets/rviz/`:

- `custom-navigation.rviz`: the custom experiment configuration.
- `turtlebot3-navigation.rviz`: the TurtleBot3 navigation configuration.

Example Nav2 launch command from the repository root:

```bash
export TURTLEBOT3_MODEL=burger

ros2 launch turtlebot3_navigation2 navigation2.launch.py \
  map:="$(pwd)/assets/maps/my_map.yaml" \
  use_sim_time:=True
```

## Documentation

- [ROS 2 basics](docs/ros2-basics.md)
- [TurtleBot3 SLAM](docs/slam/turtlebot3-slam.md)
- [SLAM command reference](docs/slam/commands.md)
- [TurtleBot3 navigation](docs/navigation/turtlebot3-navigation.md)
- [Nav2 troubleshooting](docs/troubleshooting/nav2.md)
- [RViz configurations](docs/rviz-configurations.md)

## Next steps

Future work is tracked in the learning checklist above. Larger tasks can be
moved into GitHub Issues as the project grows.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE).
