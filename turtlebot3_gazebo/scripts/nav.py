#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

def movebase_client():
    rospy.init_node('movebase_client')
    goal = PoseStamped()
    goal.header.frame_id = "map" 
    goal.header.stamp = rospy.Time.now()

    move_base_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():
        zone = input("Please ender zone: ")
        if (zone == "zone 1"):
            goal.pose.position.x = -3.30
            goal.pose.position.y = 2.33
            goal.pose.orientation.w = 1.0
        elif (zone == "zone 2"):
            goal.pose.position.x = -3.30
            goal.pose.position.y = -1.32
            goal.pose.orientation.w = 1.0
        elif (zone == "home"):
            goal.pose.position.x = -0.11
            goal.pose.position.y = -0.03
            goal.pose.orientation.w = 1.0
        move_base_pub.publish(goal)
        rate.sleep()

if __name__ == '__main__':
    try:
        movebase_client()
    except rospy.ROSInterruptException:
        pass
