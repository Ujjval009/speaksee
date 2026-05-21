import numpy as np
import cv2
import os

# Create sample video file
output_video = 'data/s1/bbal6n.mpg'
os.makedirs(os.path.dirname(output_video), exist_ok=True)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter(output_video, fourcc, 25.0, (640, 480))

# Generate 75 random frames (3 seconds at 25 fps)
for i in range(75):
    frame = np.random.randint(0, 256, (480, 640, 3), dtype=np.uint8)
    out.write(frame)

out.release()
print(f"Created sample video: {output_video}")

# Create sample alignment file
output_align = 'data/alignments/s1/bbal6n.align'
os.makedirs(os.path.dirname(output_align), exist_ok=True)

with open(output_align, 'w') as f:
    f.write("0 2310 sil\n")
    f.write("2310 4620 bin\n")
    f.write("4620 6930 blue\n")
    f.write("6930 9240 at\n")
    f.write("9240 11000 sil\n")

print(f"Created sample alignment: {output_align}")
print("Sample data created! Now you can run the notebook.")
