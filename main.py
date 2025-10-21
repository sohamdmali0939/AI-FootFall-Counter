import cv2
import numpy as np
from ultralytics import YOLO

# ======================================================
# 🎯 Step 1: Load YOLOv8 Model
# ======================================================
model = YOLO("yolov8n.pt")  # automatically downloads pretrained weights

# ======================================================
# 🎥 Step 2: Load Input Video
# ======================================================
input_path = "input_video.mp4"
cap = cv2.VideoCapture(input_path)

if not cap.isOpened():
    print("❌ Error: Could not open video file. Check the path or filename.")
    exit()

frame_width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# ======================================================
# 💾 Step 3: Setup Output Video Writer
# ======================================================
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output_video.mp4", fourcc, fps, (frame_width, frame_height))

# ======================================================
# 🧠 Step 4: Initialize Counting Variables
# ======================================================
line_y = frame_height // 2
entry_count = 0
exit_count = 0
trackers = {}  # previous centroids for tracking

def get_centroid(x1, y1, x2, y2):
    return int((x1 + x2) / 2), int((y1 + y2) / 2)

# ======================================================
# 🔁 Step 5: Frame-by-Frame Processing
# ======================================================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, stream=True)
    detections = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            if cls == 0:  # 'person' class in COCO
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                detections.append((x1, y1, x2, y2))

    new_trackers = {}

    for i, (x1, y1, x2, y2) in enumerate(detections):
        cx, cy = get_centroid(x1, y1, x2, y2)
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

        same_id = None
        for obj_id, (pcx, pcy) in trackers.items():
            if abs(cx - pcx) < 50 and abs(cy - pcy) < 50:
                same_id = obj_id
                break

        if same_id is None:
            same_id = len(trackers) + len(new_trackers) + 1

        new_trackers[same_id] = (cx, cy)

        # 🚶 Check if person crossed the line
        if same_id in trackers:
            prev_y = trackers[same_id][1]
            if prev_y < line_y and cy >= line_y:
                entry_count += 1
            elif prev_y > line_y and cy <= line_y:
                exit_count += 1

        # 📦 Draw bounding box + ID
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"ID {same_id}", (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    trackers = new_trackers

    # ======================================================
    # 🧾 Step 6: Draw UI Elements (line + counts)
    # ======================================================
    cv2.line(frame, (0, line_y), (frame_width, line_y), (255, 0, 0), 2)
    cv2.putText(frame, f"Entry: {entry_count}  Exit: {exit_count}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Show window
    cv2.imshow("Footfall Counter", frame)

    # Write the processed frame to output video
    out.write(frame)

    # Press ESC to exit early
    if cv2.waitKey(1) & 0xFF == 27:
        break

# ======================================================
# 🏁 Step 7: Cleanup
# ======================================================
cap.release()
out.release()
cv2.destroyAllWindows()

print("\n✅ Processing complete!")
print(f"Final Entry Count: {entry_count}")
print(f"Final Exit Count:  {exit_count}")
print("🎥 Saved output video as 'output_video.mp4'")
