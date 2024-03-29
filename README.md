# The Castaway problem

## Bibliographic references
Andaluz, V.H, Roberti, F., Toibero, J.M., Carelli, R., Wagner, B.: Adaptive dynamic path following control of an unicycle like mobile robot. In: Intelligent Robotics and Applications, chapter 56, pp 563–574. Springer, Berlin (2011)

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
