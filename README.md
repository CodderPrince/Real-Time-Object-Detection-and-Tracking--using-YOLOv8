# <span style="color:green"> Real-time Object Detection and Tracking with YOLOv8 & Streamlit </span>

This repository is an extensive open-source project showcasing the seamless integration of **object detection and tracking** using **YOLOv8** (object detection algorithm), along with **Streamlit** (a popular Python web application framework for creating interactive web apps). The project offers a user-friendly and customizable interface designed to detect and track objects in real-time video streams from sources such as RTSP, UDP, and YouTube URLs, as well as static videos and images.


## <span style="color:green"> Explore Implementation Details on Medium (3 parts blog series) </span>

## <span style="color:green"> WebApp Demo on Streamlit Server</span>



**Note**: In the demo, Due to non-availability of GPUs, you may encounter slow video inferencing.


## <span style="color:green"> Tracking With Object Detection Demo</span>


## Demo Pics

## Requirements

- Python 3.6+
- YOLOv8
- Streamlit

## Usage

- **Run the app with the following command:** `streamlit run app.py`
- **The app should open in a new browser window.**

### Machine Learning Model Configuration

- **Select task:** Choose between "Detection" and "Segmentation".
- **Select model confidence:** Use the slider to adjust the confidence threshold (1-100) for the model.

Once the model configuration is done, select a source for the input.

### Detection on images

- **The default image with its objects-detected image is displayed on the main page.**
- **Select a source:** Choose "Image" from the radio button selection.
- **Upload an image:** Click on the "Browse files" button to upload an image from your local machine.
- **Click the "Detect Objects" button:** This will run the object detection algorithm on the uploaded image with the selected confidence threshold.
- **Resulting image:** The resulting image with objects detected will be displayed on the page. Click the "Download Image" button to download the image.("If save image to download" is selected)

## Detection in Videos

- **Create a folder named "videos" in the same directory as your app.**
- **Place your video files in the "videos" folder.**
- **Edit `settings.py`:**
    - **Modify the `VIDEO_DIR` variable:** This variable should point to the newly created "videos" folder.
    - **Edit the `VIDEO_1_PATH`, `VIDEO_2_PATH`, etc. variables:** Use the exact names of your video files (e.g., "video_1.mp4", "video_2.mp4").
    - **Update the `VIDEOS_DICT` dictionary:** Ensure the names used in the dictionary match the names of your video files.
- **Select the source as "Video".**
- **Choose a video from the dropdown menu:** The videos you placed in the "videos" folder will appear here.
- **Click the "Detect Video Objects" button:** The selected task (detection/segmentation) will start on the chosen video.

### Detection on YouTube Video URL

- **Select the source as "YouTube".**
- **Paste the YouTube video URL into the text box.**
- **Click the "Detect Video Objects" button:** The detection/segmentation task will start on the provided YouTube video URL.

## Acknowledgements

This app uses [YOLOv8](<https://github.com/ultralytics/ultralytics>) for object detection algorithms and [Streamlit](<https://github.com/streamlit/streamlit>) library for the user interface.

### Disclaimer

This project is intended as a learning exercise and demonstration of integrating various technologies, including:

- Streamlit
- YoloV8
- Object-Detection on Images And Live Video Streams
- Python-OpenCV

Please note that this application is not designed or tested for production use. It serves as an educational resource and a showcase of technology integration rather than a production-ready web application.

Contributors and users are welcome to explore, learn from, and build upon this project for educational purposes.

### Hit star ⭐ if you like this repositories!!!
