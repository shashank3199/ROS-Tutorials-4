from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    GroupAction
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.logging import get_logger
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    logger = get_logger('robot_bringup.launch')

    # Get the package share directory
    pkg_dir = get_package_share_directory('robot_arms_bringup')

    # Declare the namespace argument
    namespace_arg = DeclareLaunchArgument(
        'namespace',
        default_value='',
        description='Top level namespace'
    )

    namespace = LaunchConfiguration('namespace')

    # Include the left arm launch file
    left_arm_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(pkg_dir, 'launch', 'left_arm.launch.py')
        ]),
        launch_arguments={'namespace': namespace}.items()
    )

    # Include the right arm launch file
    right_arm_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(pkg_dir, 'launch', 'right_arm.launch.py')
        ]),
        launch_arguments={'namespace': namespace}.items()
    )

    # Create a group action to launch everything
    bringup_group = GroupAction([
        left_arm_launch,
        right_arm_launch
    ])

    return LaunchDescription([
        namespace_arg,
        bringup_group
    ])