from core import Transcriber

transcriber = Transcriber()

result = transcriber.transcribe(
    "temp/denoised/sample_enhanced_denoised.wav"
)

print("\n")
print("=" * 80)

print("Language :", result["language"])
print("Confidence :", result["probability"])

print("=" * 80)

for segment in result["segments"]:

    print(f"\nSegment {segment['id']}")

    print(
        f"[{segment['start']}s --> {segment['end']}s]"
    )

    print(
        f"Duration : {segment['duration']} seconds"
    )

    print(segment["text"])

print("\n")

print(
    "Total Segments :",
    len(result["segments"])
)

print("=" * 80)