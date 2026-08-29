# TurtleBot3 SLAM command reference

Run these commands from separate terminals after sourcing ROS 2 Humble.

## Start the simulation

```bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

## Start keyboard control

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

## Start SLAM Toolbox

```bash
ros2 launch slam_toolbox online_async_launch.py
```

## Save the map

From the repository root:

```bash
ros2 run nav2_map_server map_saver_cli \
  -f "$(pwd)/assets/maps/my_map"
```
