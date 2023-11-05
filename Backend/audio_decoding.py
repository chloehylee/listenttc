from pydub import AudioSegment
from pydub.playback import play

# Replace with your raw audio data in bytes
raw_audio_bytes = b'\x00\x01\x02\x03...'  # Replace with your raw audio bytes

# Create an AudioSegment from the raw audio bytes
audio_data = AudioSegment.from_raw(raw_audio_bytes, sample_width=2, frame_rate=44100, channels=2)

# Output file path for the decoded MP3 file
output_file = "decoded_audio.mp3"

# Export the audio data as an MP3 file
audio_data.export(output_file, format="mp3")

print(f"Audio data decoded and saved as {output_file}")

# Play the decoded audio (optional)
play(audio_data)





