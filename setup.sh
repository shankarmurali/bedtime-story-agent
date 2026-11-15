#!/usr/bin/env bash
# Installs the pinned speech packages and downloads the pinned voice model.
# Stops if a downloaded file does not match its recorded checksum.
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

MODEL_URL="https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.int8.onnx"
VOICES_URL="https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin"
MODEL_SHA="6e742170d309016e5891a994e1ce1559c702a2ccd0075e67ef7157974f6406cb"
VOICES_SHA="bca610b8308e8d99f32e6fe4197e7ec01679264efed0cac9140fe9c29f1fbf7d"

# Some managed Python installs need --break-system-packages; plain pip is tried first.
pip install -q "kokoro-onnx==0.6.1" "soundfile==0.14.0" 2>/dev/null \
  || pip install -q --break-system-packages "kokoro-onnx==0.6.1" "soundfile==0.14.0"

[ -f kokoro.onnx ] || curl -sSL --max-time 300 -o kokoro.onnx "$MODEL_URL"
[ -f voices.bin ]  || curl -sSL --max-time 300 -o voices.bin "$VOICES_URL"

echo "$MODEL_SHA  kokoro.onnx" | sha256sum -c -
echo "$VOICES_SHA  voices.bin" | sha256sum -c -

command -v ffmpeg >/dev/null || { echo "ffmpeg is required for MP3 output"; exit 1; }
echo "setup ok"
