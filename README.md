

Body Pose Game Control

This project uses OpenCV to capture your body movements via a webcam, processes the movements, and translates them into keyboard inputs for controlling a game. Specifically, it detects body motion and sends keypresses (W, A, S, D) based on the direction of the movement.

Features

Webcam Capture: Captures video frames using your webcam.
Movement Detection: Detects large contours (movements) in the video.
Keyboard Control: Translates movements into keyboard presses (W, A, S, D) to control your character in a game.
How It Works

Background Subtraction: The program uses background subtraction to isolate moving objects (i.e., your body) in the camera frame.
Contour Detection: It identifies the largest contour (presumably your body) and tracks its bounding box.
Movement Detection: When significant horizontal or vertical movement is detected, corresponding keyboard keys (W, A, S, D) are pressed to simulate in-game movement.
Move up → W keypress
Move down → S keypress
Move left → A keypress
Move right → D keypress
Prerequisites

Python 3.x
OpenCV
Pynput

git clone https://github.com/armansj/gamebody.git
cd game_body
pip install opencv-python pynput

python body_pose_control.py

[Watch the demo on Instagram](https://www.instagram.com/reel/C-Dt7BSAOZ6/?utm_source=ig_web_button_share_sheet&igsh=MzRlODBiNWFlZA==)

