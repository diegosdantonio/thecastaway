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
		self.sub_odom = self.rospy.Subscriber('robot_0/odom', Odometry, self.odom_callback1)
		self.sub_odom = self.rospy.Subscriber('robot_1/odom', Odometry, self.odom_callback2)
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
		return

	def shark(self):

		xc = self.x_bot1
		yc = self.y_bot1

		theta_c=math.atan2(yc,xc)

		xs = self.x_bot2+1
		ys = self.y_bot2   

		theta_s = math.atan2(ys,xs)

		print "position_xc = " + str(xc) + "position_yc = " + str(yc)
		print "theta_c = " + str(theta_c) + "theta_s = " + str(theta_s)

		error_angle = theta_c - theta_s
		P = 4*error_angle

		print "error angle = " + str(P)

		twist = Twist()

		if theta_c < theta_s or yc > 0:
			if P >= 4 :
				twist.linear.y = 4 
			else:
				twist.linear.y = P
			twist.angular.z = P
			turn = 'Derecha'
		else:
			if P >= 4 :
				twist.linear.y = 4
			else:
				twist.linear.y = P
			twist.angular.z = P
			turn = 'Izquierda'
		print(turn)

		hyp = math.hypot(ys,xs)

		error_position = 1-hyp
		P = 5*error_position

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
			    os.system('clear')
		sys.exit()
		

if __name__ == '__main__':
	try:
		sw = robot('shark')
	except rospy.ROSInterruptException:
		pass
