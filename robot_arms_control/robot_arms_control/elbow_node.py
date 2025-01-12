#!/usr/bin/env python3

import rclpy
from robot_arms_control.elbow import Elbow

def main(args=None):
    rclpy.init(args=args)
    node = Elbow()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()