rm -rf selfie_input/*
rm -rf selfie_mask/*
rm -rf selfie_result/*
python motion_detector_origin.py
wait
ffmpeg -y -f image2 -i selfie_result/image%d.png video_result.mp4