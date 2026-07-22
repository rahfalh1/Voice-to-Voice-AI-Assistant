import whisper
import sounddevice as sd
from scipy.io.wavfile import write

model = whisper.load_model("base")

def record_audio(filename="recording.wav", duration=5, samplerate=44100):
    print("🎤 Speak now...")

    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(filename, samplerate, recording)

    print("✅ Recording finished.")

def speech_to_text():
    record_audio()

    result = model.transcribe("recording.wav")

    return result["text"]