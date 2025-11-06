import rclpy
from rclpy.node import Node
import yaml
import os
import ctypes
from multiprocessing import Process, Value

from sensor_msgs.msg import Joy

from playsound import playsound			#unterstützt .wav und .mp3

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
		self.is_playing = Value(ctypes.c_wchar_p, "no_sound")
		self.i = 0
		self.subscription

		self.soundpath1 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name1"])
		self.soundpath2 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name2"])
		self.soundpath3 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name3"])
		self.soundpath4 = os.path.join(self.sounds["soundfolder"], self.sounds["filenames"]["name4"])

		self.sound1 = None
		self.sound2 = None
		self.sound3 = None
		self.sound4 = None

	def _play(self, path, sound):
		self.is_playing.value = sound
		playsound(path)
		self.is_playing.value = "no_sound"
	
	def _sound(self, play_req):
		if play_req == "no_sound":
			self.get_logger().info('Not playing a sound')

		if play_req == self.is_playing.value:
			self.get_logger().info('Not playing a sound')
		else:
			# Ton, der gerade spielt abbrechen
			match self.is_playing.value:
				case "sound1":
					self.sound1.interrupt()
				case "sound2":
					self.sound2.interrupt()
				case "sound3":
					self.sound3.interrupt()
				case "sound4":
					self.sound4.interrupt()
			# neuen Ton starten
			match play_req:
				case "sound1":
					self.sound1 = Process(target=self._play, kwargs={"path": self.soundpath1, "sound": play_req})
					self.sound1.start()
					self.get_logger().info('Playing sound 1')
				case "sound2":
					self.sound2 = Process(target=self._play, kwargs={"path": self.soundpath2, "sound": play_req})
					self.sound2.start()
					self.get_logger().info('Playing sound 2')
				case "sound3":
					self.sound3 = Process(target=self._play, kwargs={"path": self.soundpath3, "sound": play_req})
					self.sound3.start()
					self.get_logger().info('Playing sound 3')
				case "sound4":
					self.sound4 = Process(target=self._play, kwargs={"path": self.soundpath4, "sound": play_req})
					self.sound4.start()
					self.get_logger().info('Playing sound 4')
	
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