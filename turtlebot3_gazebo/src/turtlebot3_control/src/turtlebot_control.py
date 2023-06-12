#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def controller():
    pub_topic_name = "/cmd_vel"
    pub = rospy.Publisher(pub_topic_name, Twist, queue_size=10)
    rospy.init_node('controller')
    msg = Twist()

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        msg.linear.x = 2.0
        msg.angular.z = 1.8
        pub.publish(msg)
        rate.sleep()

    # for index in range(5): 
    #     msg.linear.x = 0.2
    #     msg.angular.z = 0.0
    #     pub.publish(msg)
    #     rospy.sleep(3)

    #     msg.linear.x = 0.0
    #     msg.angular.z = 0.5
    #     pub.publish(msg)
    #     rospy.sleep(3.5)

    # msg.linear.x = 0.0
    # msg.angular.z = 0.0
    # pub.publish(msg)


if __name__=='__main__':
    controller()