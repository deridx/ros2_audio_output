import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy

# from pynput import keyboard

class KeyboardInput(Node):

	def __init__(self):
		super().__init__('keyboard_input')
		self.publisher_ = self.create_publisher(Joy, 'pressed_key', 1)
		timer_period = 3 #Sekunden
		self.timer = self.create_timer(timer_period, self.timer_callback)

	def timer_callback(self):
		msg = Joy()
		
		# with keyboard.Events() as events:
		# 	event = events.get(0.4)
		# 	if event is not None:
		# 		msg.buttons[0] = 1
		
		msg.axes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0]
				
		self.publisher_.publish(msg)
		self.get_logger().info(f'Publishing: "{msg}"')

def main(args=None):
	rclpy.init(args=args)

	keyboard_input = KeyboardInput()
	rclpy.spin(keyboard_input)

if __name__ == '__main__':
	main()