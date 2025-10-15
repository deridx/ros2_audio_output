import rclpy
from rclpy.node import Node
import yaml
import os

from std_msgs.msg import Bool

from playsound import playsound


class SpeakerOutput(Node):

	def __init__(self):
		super().__init__('speaker_output')
		with open("/home/logan/ros2_ws/src/audio_output/temp_config/soundpaths.yaml", "r") as config:
			self.sounds = yaml.safe_load(config)
		self.subscription = self.create_subscription(
			Bool,
			'pressed_key',
			self.audio_callback,
			1)
		self.subscription

	def audio_callback(self, msg):
		sound1 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name1"])
		sound2 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name2"])
		
		if msg.data:
			playsound(sound1)
			self.get_logger().info('Playing sound 1')
		else:
			playsound(sound2)
			self.get_logger().info('Playing sound 2')

def main(args=None):
	rclpy.init(args=args)

	speaker_output = SpeakerOutput()

	rclpy.spin(speaker_output)

if __name__ == '__main__':
	main()