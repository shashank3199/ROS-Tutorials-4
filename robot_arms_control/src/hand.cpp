#include "hand/hand.hpp"

namespace robot_arms_control
{

    Hand::Hand(const rclcpp::NodeOptions &options) : Node("hand_node", options)
    {
        declare_parameters();

        // Set up parameter callback
        callback_handle_ = add_on_set_parameters_callback(std::bind(&Hand::parameters_callback, this, std::placeholders::_1));

        RCLCPP_INFO(get_logger(),
                    "Finger lengths: [%f, %f, %f, %f, %f]",
                    finger_lengths_[0],
                    finger_lengths_[1],
                    finger_lengths_[2],
                    finger_lengths_[3],
                    finger_lengths_[4]);
        RCLCPP_INFO(get_logger(), "Namespaced under %s", get_namespace());
        RCLCPP_INFO(get_logger(), "Hand Node Initialized");
    }

    void Hand::declare_parameters()
    {
        // Declare parameters with default values
        std::vector<double> default_lengths = {0.0, 0.0, 0.0, 0.0, 0.0};
        declare_parameter(param_name, default_lengths);

        // Get parameters
        finger_lengths_ = get_parameter(param_name).as_double_array();
    }

    rcl_interfaces::msg::SetParametersResult Hand::parameters_callback(
        const std::vector<rclcpp::Parameter> &parameters)
    {
        rcl_interfaces::msg::SetParametersResult result;
        result.successful = true;

        for (const auto &param : parameters)
        {
            if (param.get_name() == param_name)
            {
                finger_lengths_ = param.as_double_array();
                RCLCPP_INFO(get_logger(), "Updated finger lengths");
            }
        }

        return result;
    }

} // namespace robot_arms_control