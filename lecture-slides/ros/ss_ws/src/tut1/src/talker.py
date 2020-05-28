#!/usr/bin/env python


import rospy
from std_msgs.msg import String     # Standad ROS string messages


def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10)     # Creating a publisher `pub` on `chatter` topic with maximum queue size of 10
	rospy.init_node('talker', anonymous=True)       # Initializing the current node as `talker`
	rate = rospy.Rate(10)   # Publishing rate at 10 hz
	
	while not rospy.is_shutdown():      # Check for Ctrl+C
		hello_str = "hello world %s" % rospy.get_time()
		print(hello_str)
		pub.publish(hello_str) 
		rate.sleep()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass