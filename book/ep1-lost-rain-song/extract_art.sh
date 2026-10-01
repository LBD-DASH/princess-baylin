#!/usr/bin/env bash
# Re-extract the book art from the Episode 1 video (frames taken in narration pauses, no captions).
set -euo pipefail
VIDEO="${1:-/workspace/princess-baylin/video/lost-rain-song-en.mp4}"
cd "$(dirname "$0")" && mkdir -p art
for t in s0_21.25 s1_43.75 s1_64.75 s1_80.25 s2_128.75 s3_157.75 s3_185.75 s4_201.25 s4_242.25 s5_266.75 s5_274.25 s5_291.75 s6_308.25 s6_331.75 s7_353.75 s7_371.25 s8_396.25 s8_432.75 s9_441.25 s9_477.75 s10_502.75 s11_525.75 s12_563.25 s12_585.75 s12_593.75; do
  sec="${t#*_}"
  ffmpeg -nostdin -v error -y -ss "$sec" -i "$VIDEO" -frames:v 1 -q:v 1 "art/$t.png"
  python3 -c "from PIL import Image; Image.open('art/$t.png').convert('RGB').save('art/$t.jpg', quality=92, subsampling=0)" && rm "art/$t.png"
done
