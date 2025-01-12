#ifndef ROBOT_ARMS_CONTROL_HAND_HPP_
#define ROBOT_ARMS_CONTROL_HAND_HPP_

#include <rclcpp/rclcpp.hpp>
#include <vector>

namespace robot_arms_control
{

    class Hand : public rclcpp::Node
    {
    public:
        explicit Hand(const rclcpp::NodeOptions &options = rclcpp::NodeOptions());
        virtual ~Hand() = default;

    private:
        // Parameters
        std::vector<double> finger_lengths_;

        // Parameter declaration
        void declare_parameters();

        // Parameter callback
        rcl_interfaces::msg::SetParametersResult parameters_callback(const std::vector<rclcpp::Parameter> &parameters);

        // Callback handle
        OnSetParametersCallbackHandle::SharedPtr callback_handle_;

        // Parameter name
        std::string param_name = std::string("finger_lengths");
    };

} // namespace robot_arms_control

#endif // ROBOT_ARMS_CONTROL_HAND_HPP_