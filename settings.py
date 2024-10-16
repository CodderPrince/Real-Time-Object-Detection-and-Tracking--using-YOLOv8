from pathlib import Path
import sys
import os

# Get the absolute path of the current file
FILE = Path(__file__).resolve()
# Get the root directory based on the location of the settings.py file
ROOT = FILE.parent

# Add the root path to the sys.path list if it is not already there
if ROOT not in sys.path:
    sys.path.append(str(ROOT))

# Debugging information
print(f"Current working directory: {Path.cwd()}")
print(f"Root directory: {ROOT}")

# Sources
IMAGE = 'Image'
VIDEO = 'Video'
WEBCAM = 'Webcam'
YOUTUBE = 'YouTube'

SOURCES_LIST = [IMAGE, VIDEO, WEBCAM, YOUTUBE]

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'home4.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'detect4.png'

# Videos config
VIDEO_DIR = ROOT / 'videos'
VIDEOS_DICT = {
    'video_1': VIDEO_DIR / 'video_1.mp4',
    'video_2': VIDEO_DIR / 'video_2.mp4',
    'video_3': VIDEO_DIR / 'video_3.mp4',
    'video_4': VIDEO_DIR / 'video_4.mp4',
}

# Check if video files exist
for video_key, video_path in VIDEOS_DICT.items():
    if not os.path.exists(video_path):
        print(f"Warning: Video file not found: {video_path}")

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'yolov8n.pt'
# In case of your custom model comment out the line above and
# Place your custom model pt file name at the line below 
# DETECTION_MODEL = MODEL_DIR / 'my_detection_model.pt'

SEGMENTATION_MODEL = MODEL_DIR / 'yolov8n-seg.pt'

# Webcam
WEBCAM_PATH = 0
