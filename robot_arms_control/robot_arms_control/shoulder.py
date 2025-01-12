#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class Shoulder(Node):
    def __init__(self):
        super().__init__('shoulder_node')

        # Declare parameters
        self.declare_parameter('shoulder.x', 0.0)
        self.declare_parameter('shoulder.y', 0.0)
        self.declare_parameter('shoulder.z', 0.0)

        # Get parameters
        x = self.get_parameter('shoulder.x').value
        y = self.get_parameter('shoulder.y').value
        z = self.get_parameter('shoulder.z').value

        # Log information
        self.get_logger().info(f'Shoulder position: ({x}, {y}, {z})')
        self.get_logger().info(f'Namespaced under {self.get_namespace()}')
        self.get_logger().info('Shoulder Node Initialized')
