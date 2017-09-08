# realtime-opencv-motion-detection
This is realtime opencv motion detection and segmentation. It capture first frame and analize other frames. To use it - simply run run.sh (or you can use it in console) - 
# python motion_detector.py (with camera)
# python motion_detector.py --video video.mp4 (with video)
To stop processing click Esc.
In folder selfie_input will original captured frames from camera/video, in selfie_mask - mask for segmentation frames, and in selfie_result - result segmentation frames.
After video processing python will create frames in folder selfie_result. To create a video from this frame use:
# ffmpeg -y -f image2 -i selfie_result/image%d.png video_result.mp4
![alt text](https://github.com/ShadowsLegioneer/realtime-opencv-motion-detection/blob/master/gif_result.gif "Logo Title Text 1")
