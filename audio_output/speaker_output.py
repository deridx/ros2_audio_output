import rclpy
from rclpy.node import Node
import yaml
import os
import time

from sensor_msgs.msg import Joy

# from audioplayer import AudioPlayer
import simpleaudio

class SpeakerOutput(Node):

	def __init__(self):
		super().__init__('speaker_output')
		with open("/home/logan/ros2_ws/src/audio_output/temp_config/soundpaths.yaml", "r") as config:
			self.sounds = yaml.safe_load(config)
		self.subscription = self.create_subscription(
			Joy,
			'joy',
			self.audio_callback,
			10)
		self.subscription

		self.previous_input = "none"

		self.soundpath1 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name1"])
		self.soundpath2 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name2"])
		self.soundpath3 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name3"])
		self.soundpath4 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name4"])

		self.sound1 = simpleaudio.WaveObject.from_wave_file(self.soundpath1)
		self.sound2 = simpleaudio.WaveObject.from_wave_file(self.soundpath2)
		self.sound3 = simpleaudio.WaveObject.from_wave_file(self.soundpath3)
		self.sound4 = simpleaudio.WaveObject.from_wave_file(self.soundpath4)

		self.playing1 = self.sound1.play()
		self.playing1.stop()
		self.playing2 = self.sound2.play()
		self.playing2.stop()
		self.playing3 = self.sound3.play()
		self.playing3.stop()
		self.playing4 = self.sound4.play()
		self.playing4.stop()

	def _play(self, sound):
		match sound:
			case 1: self.playing1 = self.sound1.play()
			case 2: self.playing2 = self.sound2.play()
			case 3: self.playing3 = self.sound3.play()
			case 4: self.playing4 = self.sound4.play()
	
	def _sound(self, to_play):
		# überprüfen, welcher Ton gerade spielt
		is_playing = 0
		if self.playing1.is_playing():
			is_playing = 1
		if self.playing2.is_playing():
			is_playing = 2
		if self.playing3.is_playing():
			is_playing = 3
		if self.playing4.is_playing():
			is_playing = 4

		if to_play == 0:
			self.get_logger().info('Not playing a sound')
		else:
			# Ton, der gerade spielt, abbrechen
			match is_playing:
				case 1: self.playing1.stop()
				case 2: self.playing2.stop()
				case 3: self.playing3.stop()
				case 4: self.playing4.stop()
			if to_play == is_playing:
				self.get_logger().info('Stopped playing a sound')
			else:
				# neuen Ton starten
				time.sleep(0.5)
				match to_play:
					case 1:
						self.get_logger().info('Playing sound 1')
						self._play(1)
					case 2:
						self.get_logger().info('Playing sound 2')
						self._play(2)
					case 3:
						self.get_logger().info('Playing sound 3')
						self._play(3)
					case 4:
						self.get_logger().info('Playing sound 4')
						self._play(4)

	def _get_action(self, c_input):
		# Herausfiltern von Mehrfachinputs
		if c_input == "none":
			to_play = 0
		elif c_input == self.previous_input:
			to_play = 0
		else:
			match c_input:
				case "up": to_play = 1
				case "right": to_play = 2
				case "down": to_play = 3
				case "left": to_play = 4
		self.previous_input = c_input
		return to_play
	
	def audio_callback(self, msg):
		c_input = ""
		
		#Indizes von joy.axes für Nintendo-Controller, je nach Controller abändern
		dpad_horizontal = msg.axes[4]		#1.0 == links, -1.0 == rechts
		dpad_vertical 	= msg.axes[5]		#1.0 == oben, -1.0 == unten

		if dpad_vertical == 1.0 and dpad_horizontal == 0.0:
			c_input = "up"
		elif dpad_horizontal == -1.0 and dpad_vertical == 0.0:
			c_input = "right"
		elif dpad_vertical == -1.0 and dpad_horizontal == 0.0:
			c_input = "down"
		elif dpad_horizontal == 1.0 and dpad_vertical == 0.0:
			c_input = "left"
		else:
			c_input = "none"

		to_play = self._get_action(c_input)
		
		self._sound(to_play)

def main(args=None):
	rclpy.init(args=args)

	speaker_output = SpeakerOutput()

	rclpy.spin(speaker_output)

if __name__ == '__main__':
	main()