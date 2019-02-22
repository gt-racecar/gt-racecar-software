#!/usr/bin/env python
import rospy

from nav_msgs.msg import Odometry
import tf

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.twist.twist.linear.x)

    br = tf.TransformBroadcaster()
    br.sendTransform((data.twist.twist.linear.x, data.twist.twist.linear.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, data.twist.twist.angular.z),
                     rospy.Time.now(),
                     "base_link",
                     "odom")
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/pf/pose/odom", Odometry, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
