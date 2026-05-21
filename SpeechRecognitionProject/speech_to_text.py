import whisper

# Load whisper model
model = whisper.load_model("base")

# Convert speech to text
result = model.transcribe("sample 2.mp4")

# Print output
print("Recognized Text:")
print(result["text"])