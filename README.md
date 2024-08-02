# Hand Gesture Driving using Hand Motion Detection

## Overview

This project implements a hand gesture-based control system for driving using hand motion detection. The system uses computer vision techniques to detect hand gestures and translates them into driving commands. This project can be useful for developing innovative control systems for vehicles, especially for people with physical disabilities.

## Result
![ezgif com-gif-maker](https://github.com/user-attachments/assets/82342ee5-a0a4-461b-9463-e5dbf3834705)


## Features

- Hand gesture detection using computer vision
- Real-time hand motion tracking
- Translation of hand gestures into driving commands

## Usage

The script will start the webcam and begin detecting hand gestures. The recognized gestures will be displayed on the screen, and corresponding driving commands will be printed.

## Project Structure

- `hand_gesture_driving.py`: Main script for hand gesture detection and driving command translation.
- `requirements.txt`: List of required Python packages.

## Example

Here is a basic usage example:

1. Ensure your webcam is connected and working.
2. Run the `hand_gesture_driving.py` script.
3. Move your hand in front of the camera. The script will detect your hand gestures and output the corresponding driving commands (e.g., "Move Forward", "Turn Left", "Turn Right", "Stop").

## Dependencies

- OpenCV: For computer vision and hand gesture detection.
- Mediapipe: For hand landmark detection.
- NumPy: For numerical operations.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or issues, please open an issue or submit a pull request.

## Acknowledgements

- OpenCV and Mediapipe libraries for facilitating computer vision and hand detection.
- The open-source community for continuous improvements and support.
