"""Log pose updates received from turtlesim."""

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class TurtlePose(Node):
    """Subscribe to and report the current turtle pose."""

    def __init__(self):
        """Create the pose subscription."""
        super().__init__('turtle_pose')
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10,
        )

    def pose_callback(self, msg):
        """Log a formatted pose message."""
        self.get_logger().info(
            f'x={msg.x:.2f}, y={msg.y:.2f}, theta={msg.theta:.2f}'
        )


def main(args=None):
    """Run the turtle_pose node."""
    rclpy.init(args=args)
    node = TurtlePose()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
