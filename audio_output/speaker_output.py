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
			'/joy',				#TODO: topic-Name ändern
			self.audio_callback,
			10)
		self.subscription

	def audio_callback(self, msg):
		sound1 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name1"])
		sound2 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name2"])
		sound3 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name3"])
		sound4 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name4"])

		#Indizes für Nintendo-Controller, je nach Controller abändern
		dpad_horizontal = msg.axes[4]		#1.0 == links, -1.0 == rechts
		dpad_vertical 	= msg.axes[5]		#1.0 == oben, -1.0 == unten
		
		if dpad_vertical == 1.0 and dpad_horizontal == 0.0:
			playsound(sound1)
			self.get_logger().info('Playing sound 1')
		elif dpad_horizontal == -1.0 and dpad_vertical == 0.0:
			playsound(sound2)
			self.get_logger().info('Playing sound 2')
		elif dpad_vertical == -1.0 and dpad_horizontal == 0.0:
			playsound(sound3)
			self.get_logger().info('Playing sound 3')
		elif dpad_horizontal == 1.0 and dpad_vertical == 0.0:
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