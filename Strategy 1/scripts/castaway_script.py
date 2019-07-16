#!/usr/bin/env python

from __future__ import print_function

import math
import roslib; roslib.load_manifest('prueba2')
import rospy
import time
from geometry_msgs.msg import Twist
import os
import sys, select, termios, tty
from nav_msgs.msg import Odometry
import sys


class robot2():
	def __init__(self, name):
		self.name = name
		self.rospy = rospy
		self.rospy.init_node('Castaway', anonymous = True)
		self.initSubscribers()
		self.initPublishers()
		self.initVariables()
		self.main_path()

	def initPublishers(self):
		self.pub0 = self.rospy.Publisher('robot_0/cmd_vel', Twist, queue_size=1) 
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

	def initVariables(self):		
		self.x_bot1 = self.y_bot1 = self.x_bot2 = self.y_bot2 = self.orientationz = 0
		self.change = False
	    	speed = 1
	    	turn = 0
	    	x = 0
	    	y = 0
	    	z = 0
	    	th = 0
	    	status = 0

		return

	def odom_callback2(self, msg):
		self.x_bot2 = self.x_bot1
		self.y_bot2 = self.y_bot1
		self.orientationz = msg.pose.pose.orientation.z
		
		self.change = True
		return

	def castaway(self):

	    	xc = self.x_bot1
	    	yc = self.y_bot1

	    	theta=math.atan2(yc,xc)
	    	x=math.cos(theta)
	    	y=math.sin(theta)

	    	if xc and yc > 2 or xc and yc <-2:
	    		x=y=0
	    	print(xc,yc)
	    	twist = Twist()
	    	twist.linear.x = x*1; twist.linear.y = y*1; 
	    	  
	    	self.pub0.publish(twist)

	    	return 

	def main_path(self):

		while not self.rospy.is_shutdown():
			    self.castaway()
			    os.system('clear')
		sys.exit()

if __name__ == '__main__':
	try:
		sw = robot2('castaway')
	except rospy.ROSInterruptException:
		pass

	
