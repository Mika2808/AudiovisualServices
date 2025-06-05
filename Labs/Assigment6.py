#------------------------------ 1 ---------------------------------
print("====== 1. Streaming Video Protocols by Stack ======\n")

print("Eliminated (Not used in video streaming):")
print("  - Telnet, TCPMUX, RLP, XNS, FTP, SMTP, HTML5\n")

print("Used in Streaming (Grouped by Stack):")
print("Application Layer:")
print("  - RTSP: Controls media sessions (play/pause/seek)")
print("  - RTMP: Real-Time Messaging Protocol (used for ingestion)")
print("  - HLS: HTTP Live Streaming by Apple (m3u8 playlist)")
print("  - DASH: Adaptive Streaming over HTTP (open standard)")
print("  - SIP: For setting up multimedia calls (used with RTP)")
print("  - WebSocket: Full-duplex communication over TCP")

print("\nTransport Layer:")
print("  - TCP: Reliable, used in HLS, RTMP")
print("  - UDP: Fast, used in RTP")
print("  - SCTP: Used in WebRTC")

print("\nSecurity Layer:")
print("  - TLS: Secures TCP traffic")
print("  - DTLS: Secures UDP traffic")
print("  - SRTP: Secure RTP with encryption\n")

#------------------------------ 2 ---------------------------------
print("====== 2. What is DRM? ======\n")
print("DRM (Digital Rights Management) restricts copying, sharing, or modifying digital media.")
print("It helps content creators protect copyright in streaming and downloads.\n")

print("Common DRM Systems:")
print("  - Widevine (Google): Used in Chrome, Android, YouTube, Netflix")
print("  - PlayReady (Microsoft): Windows, Xbox, Edge")
print("  - FairPlay (Apple): Safari, iOS, Apple TV")
print("  - Adobe Access (Adobe): Flash-based platforms")
print("  - Marlin (Open): Used by Sony, Intertrust\n")

#------------------------------ 3 ---------------------------------
print("====== 3. RTP Streaming with FFMPEG and VLC ======\n")

print("▶ A. FFMPEG to VLC via SDP file:")
print("1. Save the following as stream.sdp:")
print("v=0 o=- 0 0 IN IP4 127.0.0.1 s=RTP Stream c=IN IP4 127.0.0.1 t=0 0 m=video 5004 RTP/AVP 96 a=rtpmap:96 H264/90000")

print("2. Send RTP stream from FFMPEG:")
print("   ffmpeg -re -i input.mp4 -vcodec libx264 -f rtp rtp://127.0.0.1:5004")

print("3. Open 'stream.sdp' in VLC (Media > Open File)\n")

print("◀ B. VLC to FFplay:")
print("1. In VLC: Media > Stream > Choose file > RTP > Address: 127.0.0.1 Port: 5004")
print("2. In terminal: ffplay rtp://127.0.0.1:5004\n")

print("=== RTP Protocol Summary ===")
print(" - RTP (Real-time Transport Protocol) transmits audio/video data")
print(" - Works over UDP; includes timestamps & sequence numbers")
print(" - Often used with RTSP or SIP to stream actual media")
print(" - SRTP is the secure version (encrypted RTP)\n")