#!/usr/bin/env python3

import rclpy
from robot_arms_control.shoulder import Shoulder

def main(args=None):
    rclpy.init(args=args)
    node = Shoulder()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()