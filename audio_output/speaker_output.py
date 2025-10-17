import rclpy
from rclpy.node import Node
import yaml
import os

from sensor_msgs.msg import Joy

from playsound import playsound

class SpeakerOutput(Node):

	def __init__(self):
		super().__init__('speaker_output')
		with open("/home/logan/ros2_ws/src/audio_output/temp_config/soundpaths.yaml", "r") as config:
			self.sounds = yaml.safe_load(config)
		self.subscription = self.create_subscription(
			Joy,
			'pressed_key',				#TODO: topic-Name ändern
			self.audio_callback,
			1)
		self.subscription

	def audio_callback(self, msg):
		sound1 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name1"])
		sound2 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name2"])
		sound3 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name3"])
		sound4 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name4"])

		dpad_up 	= msg.buttons[0]		#TODO: tatsächliche keys herausfinden
		dpad_right 	= msg.buttons[1]
		dpad_down 	= msg.buttons[2]
		dpad_left 	= msg.buttons[3]
		
		if dpad_up == 1 and dpad_right == 0 and dpad_down == 0 and dpad_left == 0:
			playsound(sound1)
			self.get_logger().info('Playing sound 1')
		elif dpad_right == 1 and dpad_up == 0 and dpad_down == 0 and dpad_left == 0:
			playsound(sound2)
			self.get_logger().info('Playing sound 2')
		elif dpad_down == 1 and dpad_up == 0 and dpad_right == 0 and dpad_left == 0:
			playsound(sound3)
			self.get_logger().info('Playing sound 3')
		elif dpad_left == 1 and dpad_up == 0 and dpad_right == 0 and dpad_down == 0:
			playsound(sound4)
			self.get_logger().info('Playing sound 4')
		else:
			self.get_logger().info('Not playing a sound')
		


		#if msg.data:
		#	playsound(sound3)
		#	self.get_logger().info('Playing sound 3')
		#else:
		#	self.get_logger().info('not playing a sound')

def main(args=None):
	rclpy.init(args=args)

	speaker_output = SpeakerOutput()

	rclpy.spin(speaker_output)

if __name__ == '__main__':
	main()