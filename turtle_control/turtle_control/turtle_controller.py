#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtleControllerNode(Node):

    def __init__(self):
        super().__init__('turtle_controller')

        self.cmd_vel_publisher_ = self.create_publisher(
            Twist,
            'turtle1/cmd_vel',
            10
        )

        self.pose_subscriber_ = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.pose_callback,
            10
        )

        self.get_logger().info('Turtle controller has been started.')
    
    def pose_callback(self, pose: Pose):
        cmd = Twist()

        if pose.x > 8.0 or pose.x < 3.0 or pose.y > 8.0 or pose.y < 3.0:
            cmd.linear.x = 1.2
            cmd.angular.z = 0.9
        else:      
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
        self.cmd_vel_publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()