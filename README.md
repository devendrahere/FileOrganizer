# 🗂️ SmartSort - File Organizer

SmartSort is a Python-based file organization tool that automatically sorts files in a given directory into categorized folders (Images, Documents, Videos, etc.).

## ✨ Features

- Categorizes files by type (Images, Documents, Audio, Video, Archives, Others)
- Automatically creates folders if not present
- Handles file permission and access errors
- Logs moved files to `log.txt`
- Command-line interface with colorful output using `colorama`

## 📁 Categories

- 📷 Images: `.jpg`, `.png`, `.jpeg`, `.gif`
- 📄 Documents: `.pdf`, `.docx`, `.txt`, `.pptx`
- 🎞️ Videos: `.mp4`, `.mkv`, `.mov`
- 🎵 Audio: `.mp3`, `.wav`
- 📦 Archives: `.zip`, `.rar`, `.tar`, `.gz`

## 🔧 Installation

```bash
git clone https://github.com/devendrahere/FileOrganizer.git
cd FileOrganizer
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt

python organiser/organiser.py
All moved files are logged in log.txt.
