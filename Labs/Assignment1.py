# 1 Size of audo

sample_rate= 44100 # kHZ
bit_depth = 16 # bytes
byte_size = 8 # size of byte in bits
channels = 6 # Dolby Digital 5.1 (5 normal + subwoofer)
duration_audio = 2*60*60 # 2 hours = 2*60 minutes = 2*60*60 seconds

## a
size_audio = sample_rate * (bit_depth/byte_size) * channels * duration_audio
print("\n1.a Size of audio:", size_audio, "bytes =" , size_audio/10**9, "GB")

## b
bit_rate_audio = sample_rate * channels * bit_depth
print("1.b Bit rate of audio:", bit_rate_audio, "bits/sec =", bit_rate_audio/10**6 ,"Mbps\n")

# 2 Size of video

resolution = 1920 * 1080 # HD (1920x1080)
color_depth = 3 # RGB (3 bytes)
frame_rate = 30 # fps
duration_video = 2*60*60 # 2 hours = 2*60 minutes = 2*60*60 seconds

## a
size_video = resolution * color_depth * frame_rate * duration_video
print("2.a Size of video", size_video, "bytes =", size_video/10**12, "TB")

## b
bit_rate_video = resolution * color_depth * frame_rate
print("2.b Bit rate of video", bit_rate_video, "bytes per second =", bit_rate_video/10**9, "GB/s")

## c
print("2.c Lower resolution, lower frame rate, change color format (YUV-16 bpp, Monochrome-1 bpp)\n")

# 3 https://support.google.com/youtube/answer/1722171?hl=en

# # Seven settings and their meanings:

# #     Container – MP4 is preferred.

# #     Audio Codec – AAC-LC (stereo, 48 kHz preferred)

# #     Video Codec – H.264 for compatibility, High Profile, Level 4.2

# #     Frame Rate – Match original (24, 25, 30, 48, 50,  60 fps)

# #     Bitrate – Depends on resolution

# #     Resolution – Recommended aspect ratio is 16:9

# #     Color Space – Use standard color range

# 4

# # Codec (a) – Compresses/decompresses audio/video data
# # Container (b) – Holds multiple streams (video, audio, subtitles)
# # Classification:

# #     Codecs:
# #     DivX, XviD, H.264, H.265, MP3, FLAC, AAC, WAV, OGG, AIFF, M4A, VP9, AV1, MPEG-4

# #     Containers:
# #     MKV, MP4, DVD, TS, AVI

# 5 

# # A codec (coder-decoder) is software or hardware used to compress and decompress media.
# # Can you mix codecs?

# #     Yes, but both encoder and decoder must support the format.

# #     You can’t always decode with a different codec unless they’re compatible.

# # DivX vs. XviD:

# #     Both are MPEG-4 Part 2 based.

# #     XviD is open source, DivX is proprietary.

# #     Some compatibility exists, but you can’t decode DivX with XviD if there are unique features used by DivX.

# 6
# # Lossless:

# #     No quality loss (e.g., FLAC, WAV)

# #     Larger file size

# #     Used when preserving original is important

# # Lossy:

# #     Some data discarded (e.g., MP3, H.264, AAC)

# #     Smaller file size

# #     Good for streaming or storage

# # Task 1 Audio: Dolby Digital (AC-3) is lossy 
# 6
# # av01.0.04M.08 (397) / opus (251)
# # Video: AV1
# # AudioL opus
