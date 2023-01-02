import rclpy
from rclpy.node import Node
from std_msgs import String

class M_pub(Node):
  def __init__(self):
    super().__init__('message_publisher')
    self.message_publisher =self.create_publisher(String, 'm_pub', 10)
    self.timer = self.create_timer(1, self.m_publisher)
    self.count=0

  def m_publisher(self, msg):
    msg.data='hello'+ self.count
    self.message_publisher.publish(msg)
    self.count +=1

def main(args=None):
  rclpy.init(args=args)
  node=M_pub()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    node.get_logger().info('Keyboard interrupt!!!!')
  finally:
      node.destroy_node()
      rclpy.shutdown()


if __name__=='__main':
  main()
