#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class Elbow(Node):
    def __init__(self):
        super().__init__('elbow_node')

        # Declare parameters
        self.declare_parameter('elbow.x', 0.0)
        self.declare_parameter('elbow.y', 0.0)
        self.declare_parameter('elbow.z', 0.0)

        # Get parameters
        x = self.get_parameter('elbow.x').value
        y = self.get_parameter('elbow.y').value
        z = self.get_parameter('elbow.z').value

        # Log information
        self.get_logger().info(f'Elbow position: ({x}, {y}, {z})')
        self.get_logger().info(f'Namespaced under {self.get_namespace()}')
        self.get_logger().info('Elbow Node Initialized')
