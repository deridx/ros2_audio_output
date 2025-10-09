from setuptools import find_packages, setup

package_name = 'audio_output'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='logan',
    maintainer_email='lowei4805@gmail.com',
    description='Output of one audio file from several distinct options',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'keyboard_listener = audio_output.keyboard_input:main',
            'speaker = audio_output.speaker_output:main'
        ],
    },
)
