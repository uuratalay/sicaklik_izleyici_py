import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class IzleyiciNode(Node):

    def __init__(self):
        super().__init__('izleyici_node')
        self.declare_parameter('esik', 30.0)
        self.subscription = self.create_subscription(
            Float32, 'sicaklik', self.listener_callback, 10)

    def listener_callback(self, msg):
        esik = self.get_parameter('esik').get_parameter_value().double_value
        self.get_logger().info(f'Alinan sicaklik: {msg.data:.2f}')
        if msg.data > esik:
            self.get_logger().warn(
                f'Sicaklik esik degerini asti! ({msg.data:.2f} > {esik:.2f})')


def main(args=None):
    rclpy.init(args=args)
    node = IzleyiciNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
