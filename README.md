# The Castaway problem

## Install ROS Kinetic

Using Ubuntu 14.04 install ROS Kinetic:

First, make sure your Debian package index is up-to-date:

```bash
sudo apt-get update
```

Desktop-Full Install: (Recommended) : ROS, rqt, rviz, robot-generic libraries, 2D/3D simulators, navigation and 2D/3D perception

```bash
sudo apt-get install ros-kinetic-desktop-full
```

Before you can use ROS, you will need to initialize rosdep. rosdep enables you to easily install system dependencies for source you want to compile and is required to run some core components in ROS.
```bash
sudo rosdep init
rosdep update
```
## Install stage_controllers
It's convenient if the ROS environment variables are automatically added to your bash session every time a new shell is launched:
Download the codes from [https://code.google.com/archive/p/mobotica/downloads](https://code.google.com/archive/p/mobotica/downloads) and extract the stage_controllers file and make sure that it is in the [ROS path](http://wiki.ros.org/ROS/EnvironmentVariables#ROS_PACKAGE_PATH)

```bash
rosmake stage_controllers
```
Check if the package can be found by rospack
```bash
rospack find stage_controllers
```
Is necessary install catkin and create package with your preferred name
```bash
cd ~/catckin_ws/src
catkin_create_pkg name_pack std_msgs rospy roscpp geometry_msgs tf
```
move folder scripts and launch to new folder created, and make programm
```bash
catkin_make
```
Launch all node
```bash
rosmake source_code
```

## Run program
First run roscore
```bash
roscore
```
For the initialization of 2D environment 
```bash
rosrun stage_ros stageros ra1.cfg
```
Launch all node
```bash
roslaunch source_program thecastaway_launcher.launch
```
If you want to see all nodes use
```bash
rtq_graph
rosnode list
```
@InProceedings{10.1007/978-3-642-25486-4_56,
author="Andaluz, Victor H.
and Roberti, Flavio
and Toibero, Juan Marcos
and Carelli, Ricardo
and Wagner, Bernardo",
editor="Jeschke, Sabina
and Liu, Honghai
and Schilberg, Daniel",
title="Adaptive Dynamic Path Following Control of an Unicycle-Like Mobile Robot",
booktitle="Intelligent Robotics and Applications",
year="2011",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="563--574",
abstract="This work presents a new adaptive dynamic control to solve the path following problem for the unicycle-like mobile robot. First, it is proposed a dynamic modeling of a unicycle-like mobile robot where it is considered that its mass center is not located at the center the wheels' axle. Then, the design of the control algorithm is presented. This controller design is based on two cascaded subsystems: a kinematic controller with command saturation, and an adaptive dynamic controller that compensates the dynamics of the robot. Stability and robustness are proved by using Lyapunov's method. Experimental results show a good performance of the proposed controller as proved by the theoretical design.",
isbn="978-3-642-25486-4"
}
