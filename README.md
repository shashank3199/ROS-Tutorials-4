# ROS2 Tutorial - Nodes and Launch Files

[![ROS2 Version](https://img.shields.io/badge/ROS2-Humble-blue)](https://docs.ros.org/en/humble/)
[![Developer](https://img.shields.io/badge/Developer-shashank3199-green)](https://github.com/shashank3199)

This repository demonstrates a modular robot arms control system built with ROS2, showcasing mixed language implementation (C++ and Python) and advanced launch file configuration. The system enables independent control of two robotic arms (left and right), with each arm composed of three main components: hand, elbow, and shoulder.

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Package Descriptions](#package-descriptions)
  - [Robot Arms Control Package](#robot-arms-control-package)
  - [Robot Arms Bringup Package](#robot-arms-bringup-package)
- [Building the Packages](#building-the-packages)
- [Running the System](#running-the-system)
- [Package Dependencies](#package-dependencies)

## Overview

The system consists of two main packages:

1. `robot_arms_control`: Contains the core node implementations for controlling robot arm components
2. `robot_arms_bringup`: Provides launch files and configuration for system orchestration

Each robot arm has three nodes:

- Hand node (C++) - Controls finger lengths and positions
- Elbow node (Python) - Manages elbow position in 3D space
- Shoulder node (Python) - Controls shoulder position in 3D space

## Repository Structure

```plaintext
📦 ROS2-Robot-Arms
 ┣ 📂 robot_arms_control/           # Core control package
 ┃ ┣ 📂 include/                    # C++ header files
 ┃ ┣ 📂 src/                        # C++ source files
 ┃ ┣ 📂 robot_arms_control/         # Python modules
 ┃ ┣ 📄 setup.py                    # Python setup script
 ┃ ┣ 📄 CMakeLists.txt              # Build configuration
 ┃ ┗ 📄 package.xml                 # Package manifest
 ┣ 📂 robot_arms_bringup/           # Launch and config package
 ┃ ┣ 📂 config/                     # Configuration files
 ┃ ┣ 📂 launch/                     # Launch files
 ┃ ┣ 📄 CMakeLists.txt              # Build configuration
 ┃ ┗ 📄 package.xml                 # Package manifest
 ┗ 📜 README.md                     # Repository documentation
```

## Package Descriptions

### Robot Arms Control Package

Core package implementing the control nodes for robot arms.

**Key Files:**

- `include/hand/hand.hpp`: Hand node class declaration
- `src/hand.cpp`: Hand node implementation
- `src/hand_node.cpp`: Hand node main function
- `robot_arms_control/shoulder.py`: Shoulder node implementation
- `robot_arms_control/elbow.py`: Elbow node implementation

**Features:**

- C++ implementation for hand control with parameter handling
- Python implementations for shoulder and elbow control
- Real-time parameter updates
- Namespace support for multiple arms

### Robot Arms Bringup Package

Launch and configuration package for system orchestration.

**Key Files:**

- `launch/robot_bringup.launch.py`: Main launch file
- `launch/left_arm.launch.py`: Left arm launch configuration
- `launch/right_arm.launch.py`: Right arm launch configuration
- `config/bringup.yaml`: System-wide configuration
- `config/left_hand.yaml`: Left hand specific configuration
- `config/right_hand.yaml`: Right hand specific configuration

**Features:**

- Modular launch file system
- Namespace-based arm separation
- Centralized parameter management
- Dynamic configuration loading

## Building the Packages

1. Create a new ROS2 workspace:

    ```bash
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src
    ```

2. Clone this repository:

    ```bash
    git clone https://github.com/shashank3199/ROS-Tutorials-4.git
    ```

3. Install dependencies:

    ```bash
    cd ~/ros2_ws
    rosdep install --from-paths src --ignore-src -r -y
    ```

4. Build the packages:

    ```bash
    colcon build --packages-select robot_arms_control robot_arms_bringup
    ```

5. Source the workspace:

    ```bash
    source install/setup.bash
    ```

## Running the System

### Running Individual Nodes

You can run individual nodes with specific parameters:

```bash
# Run hand node with custom parameters
ros2 run robot_arms_control hand_node --ros-args -p "finger_lengths:=[5.0, 7.5, 7.85, 7.5, 6.5]" -r __ns:=/left_arm

# Run shoulder node
ros2 run robot_arms_control shoulder_node --ros-args -p "shoulder.x:=0.5" -p "shoulder.y:=0.3" -p "shoulder.z:=0.7" -r __ns:=/left_arm
```

### Using Launch Files

Launch the entire system or specific arms:

```bash
# Launch everything
ros2 launch robot_arms_bringup robot_bringup.launch.py

# Launch just the left arm
ros2 launch robot_arms_bringup left_arm.launch.py namespace:=/robot_1

# Launch just the right arm
ros2 launch robot_arms_bringup right_arm.launch.py namespace:=/robot_1
```

### Expected Output

When running successfully, you should see log messages like:

```plaintext
[INFO] [/robot_1/left_arm/hand_node]: Finger lengths: [5.0, 7.5, 7.85, 7.5, 6.5]
[INFO] [/robot_1/left_arm/hand_node]: Namespaced under /robot_1/left_arm
[INFO] [/robot_1/left_arm/hand_node]: Hand Node Initialized
```

## Package Dependencies

Common dependencies for both packages:

- ROS2 Humble
- rclcpp (C++ nodes)
- rclpy (Python nodes)
- ament_cmake
- ament_cmake_python
- launch
- launch_ros
- ament_index_python

Each package's specific dependencies can be found in their respective `package.xml` files.
