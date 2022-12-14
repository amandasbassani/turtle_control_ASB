#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

from turtlesim.msg import Pose

import sys

from math import pow, atan2, sqrt

class TurtleControl(Node):
    def __init__(self):
        super().__init__('turtle_control_ASB')

        self.cmdvel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel',10)

        self.pose_subs = self.create_subscription(Pose,'/turtle1/pose',self.pose_callback,10)

        timer_period = 0.5
        self.timer = self.create_timer(timer_period,self.move2goal)

        self.pose=Pose()
        self.flag=False


    def pose_callback(self,data):
        self.pose.x=data.x
        self.pose.y=data.y
        self.pose.theta=data.theta
        msg = 'X: {:.3f}, Y: {:.3f}, Theta: {:.3f}'.format(data.x,data.y,data.theta)
        self.get_logger().info(msg)


    def euclidien_distance(self, goal_pose):
        return sqrt(pow((goal_pose.x - self.pose.x),2) + pow((goal_pose.y - self.pose.y),2))
    

    def liner_vel(self,goal_pose,constant=2):
        return constant*self.euclidien_distance(goal_pose)
    

    def steering_angle(self,goal_pose):
        return atan2(goal_pose.y-self.pose.y,goal_pose.x-self.pose.x)
    
    
    def angular_vel(self,goal_pose,constant=2):
        return constant*(self.steering_angle(goal_pose)-self.pose.theta)


    def move2goal(self):

        goal_pose=Pose()
        goal_pose.x = float(sys.argv[1])
        goal_pose.y = float(sys.argv[2])
        goal_pose.theta = float(sys.argv[3])

        distance_tolerance = 0.1
        angular_tolerance = 0.01

        vel_msg=Twist()

        if abs(self.steering_angle(goal_pose)-self.pose.theta)>angular_tolerance:
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = self.angular_vel(goal_pose)
        else:
            vel_msg.angular.z = 0.0
            if self.euclidien_distance(goal_pose)>=distance_tolerance:
                vel_msg.linear.x = self.liner_vel(goal_pose)
            else:
                vel_msg.linear.x = 0.0
                self.flag = True

        if self.flag:
            vel_msg.angular.z = goal_pose.theta - self.pose.theta
            if abs(goal_pose.theta - self.pose.theta) <= angular_tolerance:
                quit()
        
        self.cmdvel_pub.publish(vel_msg)
    
def main(args=None):
    rclpy.init(args=args)
    node = TurtleControl()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
