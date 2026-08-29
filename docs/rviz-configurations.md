# RViz configurations

The repository keeps two configurations because they have different origins and
have not yet been verified as interchangeable:

- `assets/rviz/custom-navigation.rviz` is the custom experiment configuration.
- `assets/rviz/turtlebot3-navigation.rviz` is the TurtleBot3 navigation
  configuration.

Both are retained to avoid losing display, topic, panel, or camera settings.
After validating both in the target ROS 2 Humble environment, compare their
Fixed Frame, Displays, Topics, Nav2 panels, and Views. If they behave
identically, keep the clearer TurtleBot3-named file and remove the duplicate in
a separate reviewed change.
