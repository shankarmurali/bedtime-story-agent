"""Narrate a plain-text story to an MP3 in a single voice.

Usage: python3 narrate.py story.txt out.mp3 [voice]

Run setup.sh first. Paragraphs are separated by blank lines. A short
paragraph (under 60 characters) is treated as a title and gets a longer pause.
"""
import os
import subprocess
import sys

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    src, out = sys.argv[1], sys.argv[2]
    voice = sys.argv[3] if len(sys.argv) > 3 else "bm_george"
    lang = "en-gb" if voice[0] == "b" else "en-us"

    kokoro = Kokoro(os.path.join(HERE, "kokoro.onnx"), os.path.join(HERE, "voices.bin"))
    with open(src, encoding="utf-8") as f:
        paragraphs = [p.strip() for p in f.read().split("\n\n") if p.strip()]
    if not paragraphs:
        sys.exit("story file is empty")

    parts, rate = [], 24000
    for i, text in enumerate(paragraphs, 1):
        samples, rate = kokoro.create(text, voice=voice, speed=0.92, lang=lang)
        parts.append(samples)
        pause = 1.4 if len(text) < 60 else 0.7
        parts.append(np.zeros(int(rate * pause), dtype=samples.dtype))
        print(f"{i}/{len(paragraphs)}", flush=True)

    wav = os.path.splitext(out)[0] + ".wav"
    sf.write(wav, np.concatenate(parts), rate)
    subprocess.run(
        ["ffmpeg", "-loglevel", "error", "-y", "-i", wav, "-b:a", "96k", out], check=True
    )
    os.remove(wav)
    minutes = sum(len(p) for p in parts) / rate / 60
    print(f"wrote {out} ({minutes:.1f} min)")


if __name__ == "__main__":
    main()
