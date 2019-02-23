cmake_minimum_required(VERSION 2.8.3)
project(odom_tf)

find_package(catkin REQUIRED COMPONENTS
  nav_msgs
  roscpp
  tf
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

 add_executable(odom_tf src/odom_tf.cpp)
 add_dependencies(odom_tf nav_msgs_generate_messages_cpp)
 target_link_libraries(odom_tf ${catkin_LIBRARIES})	

