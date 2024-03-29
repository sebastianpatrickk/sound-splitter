from pydub import AudioSegment
from pydub.silence import split_on_silence

# Load the .wav file
audio = AudioSegment.from_wav("input.wav")

# Detect the silence and split the audio file at these points
chunks = split_on_silence(audio, min_silence_len=100, silence_thresh=-50)

# For each split audio
for i, chunk in enumerate(chunks):
    # Export it as a new .wav file
    chunk.export(f"note{i+1}.wav", format="wav")