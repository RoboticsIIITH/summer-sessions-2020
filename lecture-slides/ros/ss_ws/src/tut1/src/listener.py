#!/usr/bin/env python


import rospy
from std_msgs.msg import String


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)      # ROS function to print on terminal with timestamps
	

def listener():
	rospy.init_node('listener', anonymous=True)     # anonymous=True would ensure unique name for this listener, in case of multiple listeners

	rospy.Subscriber("chatter", String, callback)

	rospy.spin()        # spin() simply keeps python from exiting until this node is stopped
	

if __name__ == '__main__':
	listener()
