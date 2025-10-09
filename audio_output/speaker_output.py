import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool

import pygame
#from playsound import playsound

class SpeakerOutput(Node):

	def __init__(self):
		super().__init__('speaker_output')
		pygame.mixer.init()
		self.subscription = self.create_subscription(
			Bool,
			'pressed_key',
			self.audio_callback,
			1)
		self.subscription

	def audio_callback(self, msg):
		if msg.data:
			#playsound("/src/audio_output/audio_output/test_sound_3.mp3")
			pygame.mixer.music.load('test_sound_2.mp3')
			pygame.mixer.music.play()
			self.get_logger().info('Playing sound')
		else:
		 self.get_logger().info('No sound played')

def main(args=None):
	rclpy.init(args=args)

	speaker_output = SpeakerOutput()

	rclpy.spin(speaker_output)

if __name__ == '__main__':
	main()