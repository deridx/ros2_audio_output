import rclpy
from rclpy.node import Node
import yaml
import os

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
		self.i = 0
		self.subscription

		self.soundpath1 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name1"])
		self.soundpath2 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name2"])
		self.soundpath3 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name3"])
		self.soundpath4 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name4"])

		self.sound1 = None
		self.sound2 = None
		self.sound3 = simpleaudio.WaveObject.from_wave_file(self.soundpath3)
		self.sound4 = None

		self.playing3 = self.sound3.play()
		self.playing3.stop()

	def _play(self, path, sound):
		self.playing3 = self.sound3.play()
		# AudioPlayer(path).play(block=True)
	
	def _check_playstate(self):
		if self.playing3.is_playing():
			return "sound3"
		else:
			return "no_sound"
	
	def _sound(self, play_req):
		is_playing = self._check_playstate()

		if play_req == "no_sound":
			self.get_logger().info('Not playing a sound')

		if play_req == is_playing:
			self.get_logger().info('Not playing a sound')
		else:
			# Ton, der gerade spielt abbrechen
			match is_playing:
				case "sound1":
					self.playing1.stop()
				case "sound2":
					self.playing2.stop()
				case "sound3":
					self.playing3.stop()
				case "sound4":
					self.playing4.stop()
			# neuen Ton starten
			match play_req:
				case "sound1":
					self.get_logger().info('Playing sound 1')
					self._play(self.soundpath1, play_req)
				case "sound2":
					self.get_logger().info('Playing sound 2')
					self._play(self.soundpath2, play_req)
				case "sound3":
					self.get_logger().info('Playing sound 3')
					self._play(self.soundpath3, play_req)
				case "sound4":
					self.get_logger().info('Playing sound 4')
					self._play(self.soundpath4, play_req)
	
	def audio_callback(self, msg):
		play_req = ""
		
		#Indizes für Nintendo-Controller, je nach Controller abändern
		dpad_horizontal = msg.axes[4]		#1.0 == links, -1.0 == rechts
		dpad_vertical 	= msg.axes[5]		#1.0 == oben, -1.0 == unten

		if dpad_vertical == 1.0 and dpad_horizontal == 0.0:
			play_req = "sound1"
		elif dpad_horizontal == -1.0 and dpad_vertical == 0.0:
			play_req = "sound2"
		elif dpad_vertical == -1.0 and dpad_horizontal == 0.0:
			play_req = "sound3"
		elif dpad_horizontal == 1.0 and dpad_vertical == 0.0:
			play_req = "sound4"
		else:
			play_req = "no_sound"
		
		self._sound(play_req)

def main(args=None):
	rclpy.init(args=args)

	speaker_output = SpeakerOutput()

	rclpy.spin(speaker_output)

if __name__ == '__main__':
	main()