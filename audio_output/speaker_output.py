import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool

from playsound import playsound

class SpeakerOutput(Node):

	def __init__(self):
		super().__init__('speaker_output')
		self.subscription = self.create_subscription(
			Bool,
			'pressed_key',
			self.audio_callback,
			1)
		self.subscription

	def audio_callback(self, msg):
		if msg.data:
			playsound('/audio_files/test_sound.mp3')
			self.get_logger().info('Playing sound')
		else self.get_logger().info('No sound played')

def main(args=None):
	rclpy.init(args=args)

	speaker_output = SpeakerOutput()

	rclpy.spin(speaker_output)

if name == '__main__':
	main()