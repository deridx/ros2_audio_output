import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool #TODO: eigenen Messagetyp erstelllen

class KeyboardInput(Node):

	def __init__(self):
		super().__init__('keyboard_input')
		self.publisher_ = self.create_publisher(Bool, 'pressed_key',1)
		timer_period = 3 #Sekunden
		self.timer = self.create_timer(timer_period, self.timer_callback)

	def timer_callback(self):
		msg = Bool()
		msg.data = True
		self.publisher_.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
	rclpy.init(args=args)

	keyboard_input = KeyboardInput()
	rclpy.spin(keyboard_input)

if __name__ == '__main__':
	main()