# realtime-opencv-motion-detection
This is realtime opencv motion detection.
USAGE
# python motion_detector.py
# python motion_detector.py --video video.mp4
After video processing python will create frames in folder selfie_result. To create a video from this frame use:
# ffmpeg -y -f image2 -i selfie_result/image%d.png video_result.mp4
