# 📝 OCR Application

![OCR Banner](https://img.shields.io/badge/OCR-Application-blue?style=for-the-badge&logo=python)

A fast and efficient Optical Character Recognition (OCR) service built with FastAPI and EasyOCR that detects and extracts text from images in both Vietnamese and English.

## ✨ Features

- ⚡️ Fast text detection and recognition
- 🌐 Support for Vietnamese and English
- 💾 Smart caching system to improve performance
- 🖥️ Simple REST API interface
- 🔄 Efficient image processing

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- GPU support (recommended for production)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ocr_app.git
   cd ocr_app
   ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### 🚀 Usage
```
uvicorn main:app --host 0.0.0.0 --port 8081
```