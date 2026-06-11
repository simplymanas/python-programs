"""
Audio Loop Generator
--------------------

Purpose:
    Creates a new MP3 file by looping an input MP3 until a desired
    duration (in minutes) is reached.

Prerequisites:
    1. Python 3.10+
    2. FFmpeg installed and available in PATH

Install FFmpeg (macOS):
    brew install ffmpeg

Verify FFmpeg:
    ffmpeg -version
    ffprobe -version

Install Python Dependencies:
    pip install pydub tqdm

Usage:
    1. Place your source MP3 file in the same folder as this script.
    2. Update the configuration section:

        INPUT_MP3 = "input.mp3"
        DESIRED_MINUTES = 30

    3. Run the script:

        python audio-loop.py

Output:
    A new MP3 file will be created with a timestamped filename:

        LoopedAudio_30min_YYYYMMDD_HHMMSS.mp3

Example:
    Input File:
        input.mp3 (4 minutes)

    Desired Duration:
        30 minutes

    Result:
        The MP3 is repeated automatically and trimmed
        to exactly 30 minutes.

Features:
    ✓ Automatic loop calculation
    ✓ Progress indicator
    ✓ Exact duration trimming
    ✓ Timestamped output filename
    ✓ MP3 export

Author:
    Manas Dash
"""
from pydub import AudioSegment
import math
from datetime import datetime

# Configuration
INPUT_MP3 = "The_Lotus_River.mp3"
DESIRED_MINUTES = 11  # Change as needed


print("Loading MP3...")

audio = AudioSegment.from_mp3(INPUT_MP3)

desired_ms = DESIRED_MINUTES * 60 * 1000
loops = math.ceil(desired_ms / len(audio))

print(f"Input Duration : {len(audio)/1000:.2f} sec")
print(f"Target Duration: {DESIRED_MINUTES} min")
print(f"Loops Required : {loops}")

# Build output incrementally with progress
output_audio = AudioSegment.empty()

for i in range(loops):
    output_audio += audio

    percent = ((i + 1) / loops) * 100

    print(
        f"\rBuilding Audio: {percent:6.2f}% "
        f"({i + 1}/{loops} loops)",
        end="",
        flush=True,
    )

print("\nTrimming to exact duration...")

output_audio = output_audio[:desired_ms]

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"LoopedAudio_{DESIRED_MINUTES}min_{timestamp}.mp3"

print("Exporting MP3...")

output_audio.export(
    output_file,
    format="mp3",
    bitrate="192k",
)

print("\nCompleted Successfully")
print(f"Output File : {output_file}")
print(f"Duration    : {DESIRED_MINUTES} minutes")
