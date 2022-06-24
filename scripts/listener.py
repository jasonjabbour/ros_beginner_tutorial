import rospy
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():

	# In ROS, nodes are uniquely named. If two nodes with the same
	# name are launched, the previous one is kicked off. The 
	# anonymous=True flag means that rospy will choose a unique 
	# name for our 'listener' node so that multiple listners can 
	# run simultaneously 

	# Each node must have a unique name. Anonymous generates a uniqueue name for a node
	rospy.init_node('listener', anonymous=True)

	# Declares that the node subscribes to the chatter Topic with message type String
	# call back is invoked with the message as the first argument
	rospy.Subscriber("chatter", String, callback)

	# spin() simply keep python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	listener()