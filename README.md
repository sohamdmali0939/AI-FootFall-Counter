# 🧍‍♂️ Footfall Counter using YOLOv8 and OpenCV

### 🎯 Objective
The goal of this project is to automatically **count the number of people entering and exiting** a specific area (such as a shop, classroom, or event space) using **computer vision**.  
The system detects and tracks people in a video feed, drawing bounding boxes and updating counts in real-time.

---

### ⚙️ Tech Stack
- **Python 3.10+**
- **OpenCV** – for image processing and video frame handling  
- **YOLOv8 (Ultralytics)** – for real-time person detection  
- **NumPy** – for numerical computation  
- **cvzone (optional)** – for better visualization (can be added later)

---

### 🧩 Project Structure

📂 AI Assignment/
│
├── main.py # Main script for detection and counting
├── requirements.txt # Dependencies list
├── input_video.mp4 # Test video (replace with your own)
├── output_video.mp4 # Processed output video with results
├── venv/ # Virtual environment folder
└── README.md # Project documentation


---

### 📦 Installation

1. **Clone or copy** the project folder:
   ```bash
   cd "E:\AI Assignment"


Create and activate a virtual environment:

python -m venv venv
.\venv\Scripts\activate


Install required libraries:

pip install -r requirements.txt


Verify installation:

python -m ultralytics check

🎥 How to Run

Place your input video as:

input_video.mp4


(You can rename your test video to this name.)

Run the script:

python main.py


The program will:

Detect people in each frame using YOLOv8

Track their movement across a counting line

Increment Entry or Exit counts based on direction

Display results in real time

Save an annotated video as output_video.mp4

🧠 Working Logic

Detection:
YOLOv8 model detects all objects, and only detections with class ID = 0 (person) are processed.

Tracking:
Each person’s centroid is calculated and compared with previous frame positions to maintain continuity.

Counting Line:
A virtual line is drawn across the frame.

If a person moves downward (crosses the line) → counted as Entry

If a person moves upward (crosses the line) → counted as Exit

Result Display:
Entry and Exit counts are updated live on screen and saved on video.

📊 Output Example

When the script runs, the terminal and video window show something like:

✅ Processing complete!
Final Entry Count: 14
Final Exit Count: 9
🎥 Saved output video as 'output_video.mp4'


On the video:

Blue horizontal line = counting line

Green boxes = detected people

Red dots = person centroids

Top-left overlay = live Entry/Exit count

🧩 Sample Applications

Retail stores for customer analytics

Colleges for attendance monitoring

Events for crowd flow analysis

Public transport for station monitoring

🚀 Future Improvements

Integrate object tracking algorithms (e.g., DeepSORT) for smoother tracking

Deploy on a live webcam or CCTV feed

Store data to a database (SQLite/MySQL) for analytics

Build a Streamlit web dashboard for visualization

🧑‍💻 Author

Soham Mali
📧 sohamdmali2004@gmail.com
🎓 AI Assignment – Footfall Counter Project
🗓️ October 2025