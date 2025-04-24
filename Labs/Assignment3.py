import subprocess
import os

# Function for playing video
def play(input):
    cmd = [ "ffplay", input]
    subprocess.run(cmd)

# Function for probing video 
def get_info(input):
    cmd = [ "ffprobe", input]
    subprocess.run(cmd)

# Function to get size of file
def get_size(file_path):
    size_bytes = os.path.getsize(file_path)
    size_megabytes = size_bytes / (1024 * 1024)
    return size_megabytes

# Function for creating different crf videos
def change_crf(input_file, output_file, crf_rate):   
    cmd = [
        "ffmpeg",
        "-i", input_file,
        "-c:v", "libx264",
        "-crf", str(crf_rate), 
        output_file]
    subprocess.run(cmd)

# Function for video filters
def change_video_filter(input_file, output_file, video_filter ="format=gray"):   
    cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vf", video_filter,
        output_file]
    subprocess.run(cmd)

# Function for audio filter
def change_audio_filter(input_file, output_file, audio_filter ="volume=1.5"):   
    cmd = [
        "ffmpeg",
        "-i", input_file,
        "-af", audio_filter,
        output_file]
    subprocess.run(cmd)


def create_video_grid(input_file, output_file):
    cmd = [
        "ffmpeg",
        "-i", input_file,
        "-filter_complex",
        "[0:v]split=4[1][2][3][4];" # spliting into 4 streams
        "[1]scale=960:540[a];" # first without any changes
        "[2]scale=960:540,lutrgb=g=0:b=0[b];" # second is only red so 0 blue and green
        "[3]scale=960:540,lutrgb=r=0:b=0[c];" # third is green so 0 red and blue
        "[4]scale=960:540,lutrgb=r=0:g=0[d];" # forth is blue so 0 red and green
        "[a][b]hstack[top];" # connect horizontally
        "[c][d]hstack[bottom];" # connect horizontally
        "[top][bottom]vstack", # connect vertically
        output_file
    ]
    subprocess.run(cmd)

short_version = "Videos/Individual/short.mov"

# 1 CRF - Constant Rate Factor. 
# Use this rate control mode if you want to keep the best quality 
# and care less about the file size. This is the recommended rate 
# control mode for most uses. 

crf_10 = "Videos/Individual/short_crf_10.mov"
crf_30 = "Videos/Individual/short_crf_30.mov"
crf_50 = "Videos/Individual/short_crf_50.mov"

change_crf(short_version, crf_10, crf_rate=10)
change_crf(short_version, crf_30, crf_rate=30)
change_crf(short_version, crf_50, crf_rate=50)

print(f"\nSize of original {get_size(short_version):.2f} MB")
print(f"Size of CRF 10 {get_size(crf_10):.2f} MB")
print(f"Size of CRF 30 {get_size(crf_30):.2f} MB")
print(f"Size of CRF 50 {get_size(crf_50):.2f} MB\n")

# 2 Filters

# 5xVideo

# Resize video
video_filter_resize = "Videos/Individual/short_resize.mov"
change_video_filter(short_version, video_filter_resize, video_filter="scale=1280:720")

# Flip horizontally video
video_filter_fliph = "Videos/Individual/short_fliph.mov"
change_video_filter(short_version, video_filter_fliph, video_filter="hflip")

# Flip vertically video
video_filter_flipv = "Videos/Individual/short_flipv.mov"
change_video_filter(short_version, video_filter_flipv, video_filter="vflip")

# Add text
video_filter_add_text = "Videos/Individual/short_add_text.mov"
change_video_filter(short_version, video_filter_add_text, video_filter="drawtext=text='Hello':fontcolor=red:fontsize=400:x=10:y=10")

# Change frame rate
video_filter_fps = "Videos/Individual/short_fps.mov"
change_video_filter(short_version, video_filter_fps, video_filter="fps=10")

# 5xAudio

# Change volume
audio_filter_volume = "Videos/Individual/short_audio_volume.mov"
change_audio_filter(short_version, audio_filter_volume, audio_filter="volume=1.5")

# Add delay to audio
audio_filter_delay = "Videos/Individual/short_audio_delay.mov"
change_audio_filter(short_version, audio_filter_delay, audio_filter="adelay=1000")

# Change audio speed
audio_filter_speed = "Videos/Individual/short_audio_speed.mov"
change_audio_filter(short_version, audio_filter_speed, audio_filter="atempo=2")

# Reverse audio 
audio_filter_reverse = "Videos/Individual/short_audio_reverse.mov"
change_audio_filter(short_version, audio_filter_reverse, audio_filter="areverse")

# Add echo
audio_filter_echo = "Videos/Individual/short_audio_echo.mov"
change_audio_filter(short_version, audio_filter_echo, audio_filter="aecho=0.8:0.88:60:0.4")

# 3
video_complex = "Videos/Individual/short_complex.mov"
create_video_grid(short_version, video_complex)