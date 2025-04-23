import subprocess

# Creating short version video for task
def create_short_video(input, output):
    cmd = [ "ffmpeg",
            "-ss", "00:00:40",
            "-i", input,
            "-t", "10",
            "-c", "copy", output]
    subprocess.run(cmd)

# Function for playing video
def play(input):
    cmd = [ "ffplay", input]
    subprocess.run(cmd)

# Function for probing video 
def get_info(input):
    cmd = [ "ffprobe", input]
    subprocess.run(cmd)

# Function for transcoding
def transcoding(input, output):
    cmd = [ "ffmpeg",
            "-i", input,
            "-c:v", "mpeg4", # mpeg4
            "-c:a", "libmp3lame", # mp3
            output]
    subprocess.run(cmd)

# Function for transmuxing
def transmuxing(input, output):
    cmd = [ "ffmpeg",
            "-i", input,
            "-c", "copy",
            output]
    subprocess.run(cmd)

# Function for transrating
def transrating(input, output):
    cmd = [ "ffmpeg",
            "-i", input,
            "-b:v", "1000k", # 1000kbps
            "-b:a", "128k", # 128kbps
            output]
    subprocess.run(cmd)

# Function for transsizing
def transsizing(input, output):
    cmd = [ "ffmpeg",
            "-i", input,
            "-vf", "scale=1280:720",
            output]
    subprocess.run(cmd)

# Function for isolating audio and saving to MP3
def isolating_audio(input, output):
    cmd = [ "ffmpeg",
            "-i", input,
            "-q:a", "0", # highest quality
            "-map", "a", # map only aduio stream
            output]
    subprocess.run(cmd)

# Function for removing audio from video
def removing_audio(input, output):
    cmd = [ "ffmpeg",
            "-i", input,
            "-an", # remove audio
            output]
    subprocess.run(cmd)

# Function for creating video from images
def create_video_from_images(photo_dir, output_file):
    
    cmd = [
        "ffmpeg",
        "-framerate", "1",
        "-i", f"{photo_dir}/frame_%03d.jpg",        
        "-c:v", "libx264",    # H.264 codec
        output_file]
    subprocess.run(cmd)

# Function for extracting photos from video
def extract_images_every_n_seconds(video_path, output_dir, interval):
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-vf", f"fps=1/{interval}",
        f"{output_dir}/frame_%03d.jpg"
    ] 
    subprocess.run(cmd)

input_file_short = "Videos/Trans/short.mp4"
input_file_best_quality = "Videos/Original/big_buck_bunny_1080p_h264.mov"
short_version = "Videos/Individual/short.mov"
create_short_video(input_file_best_quality, short_version)

# 1

# a Transcripting from v: h264 and a: aac

transcoding_version = "Videos/Individual/short_transcoding.mov"
transcoding(short_version, transcoding_version)

# b Transmuxing from mov to mp4

transmuxing_version = "Videos/Individual/short_transmuxing.mp4"
transmuxing(short_version, transmuxing_version)

# c Transrating

transrating_version = "Videos/Individual/short_transrating.mov"
transrating(short_version, transrating_version)

# d Transsizing 

transsizing_version = "Videos/Individual/short_transsizing.mov"
transsizing(short_version, transsizing_version)

# 2
audio_version = "Videos/Individual/short_audio.mp3"
isolating_audio(short_version, audio_version)

# 3
video_without_audio = "Videos/Individual/short_no_audio.mov"
removing_audio(short_version, video_without_audio)

# 4
output_folder = "Photos"
extract_images_every_n_seconds(short_version, output_folder, interval=1)

video_from_images = "short_video_from_images.mkv"
create_video_from_images(output_folder, video_from_images)