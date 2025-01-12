from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.logging import get_logger
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    logger = get_logger('left_arm.launch')

    # Get the package share directory
    pkg_dir = get_package_share_directory('robot_arms_bringup')
    config_file = os.path.join(pkg_dir, 'config', 'bringup.yaml')

    # Declare the namespace argument
    namespace_arg = DeclareLaunchArgument(
        'namespace',
        default_value='',
        description='Namespace for the nodes'
    )

    namespace = LaunchConfiguration('namespace')

    # Create node launches
    logger.info('Launching left hand node')
    hand_node = Node(
        package='robot_arms_control',
        executable='hand_node',
        namespace=[namespace, '/left_arm'],
        parameters=[config_file],
        output='screen'
    )

    logger.info('Launching left elbow node')
    elbow_node = Node(
        package='robot_arms_control',
        executable='elbow_node.py',
        namespace=[namespace, '/left_arm'],
        parameters=[config_file],
        output='screen'
    )

    logger.info('Launching left shoulder node')
    shoulder_node = Node(
        package='robot_arms_control',
        executable='shoulder_node.py',
        namespace=[namespace, '/left_arm'],
        parameters=[config_file],
        output='screen'
    )

    return LaunchDescription([
        namespace_arg,
        hand_node,
        elbow_node,
        shoulder_node
    ])