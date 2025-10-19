import rclpy
from rclpy.node import Node
import yaml
import os

from sensor_msgs.msg import Joy

#from playsound import playsound
#from audioplayer import AudioPlayer
import simpleaudio

class SpeakerOutput(Node):

	def __init__(self):
		super().__init__('speaker_output')
		with open("/home/logan/ros2_ws/src/audio_output/temp_config/soundpaths.yaml", "r") as config:
			self.sounds = yaml.safe_load(config)
		self.subscription = self.create_subscription(
			Joy,
			'/joy',
			self.audio_callback,
			10)
		self.subscription

	def audio_callback(self, msg):
		soundpath1 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name1"])
		soundpath2 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name2"])
		soundpath3 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name3"])
		soundpath4 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name4"])

		#Indizes für Nintendo-Controller, je nach Controller abändern
		dpad_horizontal = msg.axes[4]		#1.0 == links, -1.0 == rechts
		dpad_vertical 	= msg.axes[5]		#1.0 == oben, -1.0 == unten
		
		if dpad_vertical == 1.0 and dpad_horizontal == 0.0:
			#playsound(soundpath1)
			#AudioPlayer(soundpath1).play(block=True)
			self.get_logger().info('Playing sound 1')
		elif dpad_horizontal == -1.0 and dpad_vertical == 0.0:
			#playsound(soundpath2)
			#AudioPlayer(soundpath2).play(block=True)
			self.get_logger().info('Playing sound 2')
		elif dpad_vertical == -1.0 and dpad_horizontal == 0.0:
			#playsound(soundpath3)
			#AudioPlayer(soundpath3).play(block=True)
			waveobject3 = simpleaudio.WaveObject.from_wave_file(soundpath3)
			sound3 = waveobject3.play()
			sound3.wait_done()
			self.get_logger().info('Playing sound 3')
		elif dpad_horizontal == 1.0 and dpad_vertical == 0.0:
			#playsound(soundpath4)
			#AudioPlayer(soundpath4).play(block=True)
			self.get_logger().info('Playing sound 4')
		else:
			self.get_logger().info('Not playing a sound')

def main(args=None):
	rclpy.init(args=args)

	speaker_output = SpeakerOutput()

	rclpy.spin(speaker_output)

if __name__ == '__main__':
	main()