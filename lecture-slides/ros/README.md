## Slides of the lecture  
1. [ROS_Summer_School.pdf](ROS_Summer_School.pdf)

## ROS example workspace

1. This catkin workspace `ss_ws` contains two packages which were covered in the lecture slides:    
	1. `tut1:` Simple publisher and subscriber transferring `Hello world` string messages.  
	2. `learning_tf:`Tf broadcaster and listener code, along with the launch file.  

2. In order to run the tutorials you need to install [ROS](http://wiki.ros.org/ROS/Installation) according to your ubuntu distribution and build the workspace by running:  
	1. You need to install ros dependencies used in the tutorial, by (replace `kinetic` by `melodic` for `Ubuntu 18.04`):  
		1. `sudo apt-get install ros-kinetic-ros-tutorials`  
		2. `sudo apt-get install ros-kinetic-ros-tutorials ros-kinetic-geometry-tutorials ros-kinetic-rviz ros-kinetic-rosbash ros-kinetic-rqt-tf-tree`  
	2. `source /opt/ros/kinetic/setup.bash`		# Source ROS workspace  
	3. `cd ss_ws`  
	4. `catkin_make`		# This would create `devel` and `build` folder in `ss_ws`  
	5. `source devel/setup.bash`		# Source current workspace path   


3. `tut1`:  
	1. It contains two nodes in the folder `ss_ws/src/tut1/src/`: `listener.py` and `talker.py`  
	2. In order to run the nodes, do:    
		1. `roscore`  
		2. `./listner.py`  
		3. `./talker.py`  

4. `learning_tf`:  
	1. It contains two nodes in the folder `ss_ws/src/learning_tf/src/`: `turtle_tf_listener.py` and `turtle_tf_broadcaster.py`.  
	2. In order to run the nodes, do:  
		1. `roslaunch learning_tf start_demo.launch`  

5. References for the tutorials:  
	1. [Tf tutorials](http://wiki.ros.org/tf/Tutorials/Introduction%20to%20tf) 
	2. [ROS tutorials](http://wiki.ros.org/ROS/Tutorials/UnderstandingNodes)