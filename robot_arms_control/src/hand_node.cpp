#include <memory>
#include "hand/hand.hpp"

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<robot_arms_control::Hand>());
    rclcpp::shutdown();
    return 0;
}