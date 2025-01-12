from setuptools import setup

package_name = 'robot_arms_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name, 'shoulder', 'elbow'],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Shashank Goyal',
    maintainer_email='shashank3199@gmail.com',
    description='ROS2 package for controlling robot arms',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'shoulder_node = robot_arms_control.shoulder_node:main',
            'elbow_node = robot_arms_control.elbow_node:main',
        ],
    },
)