#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
import numpy as np
import math
from geometry_msgs.msg import Twist
import os
import sys

class robot():
	def __init__(self, name):
		self.name = name
		self.rospy = rospy
		self.rospy.init_node('Shark', anonymous = True)
		self.initSubscribers()
		self.initPublishers()
		self.initVariables()
		self.main_path()

	def initPublishers(self):
		self.pub0 = self.rospy.Publisher('robot_1/cmd_vel', Twist, queue_size=1) 
		return				

	def initSubscribers(self):
		self.sub_odom = self.rospy.Subscriber('robot_0/base_pose_ground_truth', Odometry, self.odom_callback1)
		self.sub_odom = self.rospy.Subscriber('robot_1/base_pose_ground_truth', Odometry, self.odom_callback2)
		return

	def odom_callback1(self, msg):
		self.x_bot1 = msg.pose.pose.position.x
		self.y_bot1 = msg.pose.pose.position.y
		self.change = True
		return

	def odom_callback2(self, msg):
		self.x_bot2 = msg.pose.pose.position.x
		self.y_bot2 = msg.pose.pose.position.y
		self.orientationz = msg.pose.pose.orientation.z
		
		self.change = True
		return

	def initVariables(self):		
		self.x_bot1 = self.y_bot1 = self.x_bot2 = self.y_bot2 = self.orientationz = 0
		self.change = False
		self.rate = self.rospy.Rate(10)
		return

	def shark(self):

		xc = self.x_bot1
		yc = self.y_bot1

		theta_c=math.atan2(yc,xc)

		xs = self.x_bot2
		ys = self.y_bot2   

		theta_s = math.atan2(ys,xs)

		xloc=self.x_bot2-self.x_bot1
		yloc=self.y_bot2-self.y_bot1

		theta_loc=math.atan2(yloc,xloc)

		print "position_xc = " + str(xc) + "position_yc = " + str(yc)
		print "theta_c = " + str(theta_c) + "theta_s = " + str(theta_s)
		print "theta loc " + str(theta_loc)
		error_angle = theta_c - theta_s
		P = 10*error_angle

		
		twist = Twist()

		if P > 4:
			P=4
		if P < -4:
			P=-4
		
		twist.linear.y = P
		twist.angular.z = P

		
		if np.sign(theta_c)  == -1 and np.sign(theta_s) == 1 and theta_s > np.pi/2:
			twist.linear.y = 4
			twist.angular.z =4
				
		if np.sign(theta_c)  == 1 and np.sign(theta_s) == -1 and theta_s < -np.pi/2:
			twist.linear.y = -4
			twist.angular.z =-4
		print "error angle = " + str(P)
		
		print "error sum angles = " + str(np.absolute(theta_s)+np.absolute(theta_c))


		hyp = math.hypot(ys,xs)

		error_position = 1-hyp
		P = 10*error_position

		twist.linear.x = P

		if math.fabs(error_angle) < 0.1:
			twist.angular.z = 0


		self.pub0.publish(twist)
		print "error radio = " + str(P)
		print "error radio = " + str(error_position)
		print(self.orientationz*180/math.pi)
		print(hyp)

	def main_path(self):

		while not self.rospy.is_shutdown():
			    self.shark()
			    self.rate.sleep()
			    os.system('clear')
		sys.exit()
		

if __name__ == '__main__':
	try:
		sw = robot('shark')
	except rospy.ROSInterruptException:
		pass
