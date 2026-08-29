"""Launch turtlesim together with the learning publisher and subscriber."""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """Create the complete turtlesim learning demo."""
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim',
        ),
        Node(
            package='my_robot_demo',
            executable='move_turtle',
            name='move_turtle',
        ),
        Node(
            package='my_robot_demo',
            executable='turtle_pose',
            name='turtle_pose',
        ),
    ])
