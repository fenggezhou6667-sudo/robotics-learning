"""Publish configurable velocity commands to turtlesim."""

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class MoveTurtle(Node):
    """Publish linear and angular velocity commands at a fixed interval."""

    def __init__(self):
        """Create the publisher, parameters, and timer."""
        super().__init__('move_turtle')

        self.declare_parameter('linear_velocity', 2.0)
        self.declare_parameter('angular_velocity', 1.0)
        self.declare_parameter('publish_period', 0.5)

        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10,
        )
        publish_period = (
            self.get_parameter('publish_period')
            .get_parameter_value()
            .double_value
        )
        self.timer = self.create_timer(publish_period, self.move)

    def move(self):
        """Publish the configured velocity command."""
        msg = Twist()
        msg.linear.x = (
            self.get_parameter('linear_velocity')
            .get_parameter_value()
            .double_value
        )
        msg.angular.z = (
            self.get_parameter('angular_velocity')
            .get_parameter_value()
            .double_value
        )
        self.publisher.publish(msg)
        self.get_logger().debug('Published velocity command')


def main(args=None):
    """Run the move_turtle node."""
    rclpy.init(args=args)
    node = MoveTurtle()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
