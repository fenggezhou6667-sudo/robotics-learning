# Contributing

This repository is a personal ROS 2 learning workspace, but focused fixes and
improvements are welcome.

## Development workflow

1. Create a short-lived branch from `main`.
2. Keep one logical change per commit.
3. Use lowercase kebab-case for documentation and asset file names.
4. Update documentation when commands, paths, or package behavior change.
5. Build and test before opening a pull request.

## Build and test

```bash
source /opt/ros/humble/setup.bash
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
colcon test --packages-select my_robot_demo
colcon test-result --verbose
```

Do not commit generated `build/`, `install/`, or `log/` directories.
