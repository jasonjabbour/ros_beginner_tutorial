#make sure Master is running by using cmd: $ roscore

import rospy #for writing node
from std_msgs.msg import String #message type

def talker():
	#publish chatter Topic using message type String
	#queue size limits amount of queued messages if any subscriber is not receiving them fast enough
	pub = rospy.Publisher('chatter', String, queue_size=10)
	#name your node talker. needed to communicate with ROS master. 
	#anonymous ensures node has unique name by adding random numbers to the end of the name
	rospy.init_node('talker', anonymous=True)
	#expect to go through the loop 10 times per second (as long as processing time does not exceed 1/10th of a second)
	rate = rospy.Rate(10) #10 hz
	#check if program is shut down
	while not rospy.is_shutdown():
		hello_str = "hello world %s" % rospy.get_time()
		#print to screen, write to Node's log file, and get written to rosout
		rospy.loginfo(hello_str)
		#publish string to our chatter Topic
		pub.publish(hello_str)
		#sleep as long as declared above
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass

	