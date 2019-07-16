#!/usr/bin/env python

from __future__ import print_function

import math
import numpy as np
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
		self.sub_odom = self.rospy.Subscriber('robot_0/base_pose_ground_truth', Odometry, self.odom_callback1)
		self.sub_odom = self.rospy.Subscriber('robot_0/base_pose_ground_truth', Twist, self.odom_callback1)
		self.sub_odom = self.rospy.Subscriber('robot_1/base_pose_ground_truth', Odometry, self.odom_callback2)
		return

	def odom_callback1(self, msg):
		self.x_bot1 = msg.pose.pose.position.x
		self.y_bot1 = msg.pose.pose.position.y
		self.change = True
		return

	def initVariables(self):		
		self.x_bot1 = self.y_bot1 = self.x_bot2 = self.y_bot2 = self.orientationz = 0
		self.change = False
		self.flag=1
	    	speed = 1
	    	turn = 0
	    	x = 0
	    	y = 0
	    	z = 0
	    	th = 0
	    	status = 0
		self.gen_path_circle()
		self.rate = self.rospy.Rate(10)
		self.i=0

		return

	def odom_callback2(self, msg):
		self.x_bot2 = msg.pose.pose.position.x
		self.y_bot2 = msg.pose.pose.position.y
		
		self.change = True
		return
	def gen_path_circle(self):
		theta=np.linspace(0, 359*np.pi/180, num=360)
		self.r=0.2
		self.xd = self.r*np.cos(theta)
		self.yd = self.r*np.sin(theta)
		return

	def castaway(self):

		xc = self.x_bot1
		yc = self.y_bot1

		theta_c=math.atan2(yc,xc)

		xs = self.x_bot2
		ys = self.y_bot2   

		theta_s = math.atan2(ys,xs)

		xloc=self.x_bot2-self.x_bot1
		yloc=self.y_bot2-self.y_bot1

		theta_loc=math.atan2(yloc,xloc)

		print ("position_xc = " , str(xc) , "position_yc = " , str(yc))
		print ("theta_c = " , str(theta_c) , "theta_s = " , str(theta_s))
		print ("theta loc " , str(theta_loc))

		twist = Twist()

		hyp = math.hypot(yc,xc)
		
		if xc<1.5 and xc >-1.5 and yc<1.5 and yc>-1.5:
			error_position_x =-self.r*xs-xc
			error_position_y =-self.r*ys-yc
			P1= 5*error_position_x
			P2 = 5*error_position_y

			vcm=0.2

			if P1 > vcm: P1=vcm
			if P1 < -vcm:P1=-vcm
			if P2 > vcm: P2=vcm
			if P2 < -vcm:P2=-vcm

			twist.linear.x = P1
			twist.linear.y = P2
		else:
			error_position_x =0
			error_position_y =0
			twist.linear.x = 0
			twist.linear.y = 0






		self.pub0.publish(twist)
		print ("error radio = " , str(error_position_x))
		print(self.orientationz*180/math.pi)
		print(hyp)


		#twist = Twist()
		error_theta=(np.absolute(theta_s) + np.absolute(theta_c))
		if error_theta > np.pi-np.pi*0.1 and error_theta < np.pi+np.pi*0.1:
			self.r+=0.01



	    	return 

	def main_path(self):

		while not self.rospy.is_shutdown():
			    self.castaway()
			    self.rate.sleep()
			    os.system('clear')

		sys.exit()

if __name__ == '__main__':
	try:
		sw = robot2('castaway')
	except rospy.ROSInterruptException:
		pass

	
