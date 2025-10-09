import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool #TODO: eigenen Messagetyp erstelllen

class KeyboardInput(Node):

	def __init__(self):
		super().__init__('keyboard_input')
		self.msgtype = Bool()
		self.publisher_ = self.create_publisher(self.msgtype, 'pressed_key',1)
		timer_period = 1 #Sekunden
		self.timer = self.create_timer(timer_period, self.timer_callback)

	def timer_callback():
		msg = self.msgtype
		msg.data = True
		self.publisher_.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.data)

def main(self):
	rclpy.init(args=args)

	keyboard_input = KeyboardInput()
	rclpy.spin(keyboard_input)

if name == '__main__':
	main()