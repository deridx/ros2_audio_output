import rclpy
from rclpy.node import Node

#TODO: Messagetyp importieren

class KeyboardInput(Node):

	def __init__(self):
		super().__init__('keyboard_input')
		self.msgtype = ... #TODO: Messagetyp einfügen
		self.publisher_ = self.create_publisher(self.msgtype, 'pressed_key',1)
		timer_period = 0.1
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0

	def timer_callback():
		msg = self.msgtype
		msg.data = 0
		self.publisher_.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.data)
		self.i += 1

def main(self):
	rclpy.init(args=args)

	keyboard_input = KeyboardInput()
	rclpy.spin(keyboard_input)

if name == '__main__':
	main()