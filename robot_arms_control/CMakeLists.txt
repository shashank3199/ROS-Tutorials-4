cmake_minimum_required(VERSION 3.8)
project(robot_arms_control)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)

# Include directories
include_directories(include)

# Create C++ executable
add_executable(hand_node src/hand_node.cpp src/hand.cpp)
ament_target_dependencies(hand_node rclcpp)

# Install C++ executables
install(TARGETS
  hand_node
  DESTINATION lib/${PROJECT_NAME}
)

# Install include directories
install(
  DIRECTORY include/
  DESTINATION include/${PROJECT_NAME}
)

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

# Install Python scripts
install(PROGRAMS
  robot_arms_control/shoulder_node.py
  robot_arms_control/elbow_node.py
  DESTINATION lib/${PROJECT_NAME}
)

# Testing
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()