# ✋ Hand Gesture Volume Control with OpenCV

Control your Mac's volume using just your fingers!
This Python project uses your webcam to track your **thumb and index finger**, and adjusts the volume based on how far apart they are. Super fun and surprisingly useful 😎🔊

---

## 🧠 How It Works

- Uses a webcam and OpenCV to capture your hand.
- Tracks hand landmarks using a pre-built module (`HandTrackingModule.py`).
- Calculates the distance between your thumb and index finger.
- Changes system volume accordingly.
- Also shows a visual volume bar and some vibrant circles/lines for extra flair ✨

---

## 🙌 Credits

This project uses code from the amazing
HandTrackingModule
Licensed under the MIT License.
A tiny line was edited to fit my project better!

---

## Note: 

This project works only on macOS because it uses AppleScript (osascript) for volume control. 
Made it with the help of https://www.youtube.com/watch?v=9iEPzbG-xLE&list=PLMoSUbG1Q_r8jFS04rot-3NzidnV54Z2q 

## 🛠️ Requirements

Make sure you have Python 3 installed, then install the dependencies:

```bash
pip install opencv-python mediapipe numpy
