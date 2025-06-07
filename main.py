from io import BytesIO
import easyocr
import numpy as np
import imagehash
from fastapi import FastAPI, File, UploadFile
from loguru import logger
from PIL import Image
from contextlib import asynccontextmanager

# Load the ML model
reader = easyocr.Reader(
    ["vi", "en"],
    gpu=True,
    detect_network="craft",
    model_storage_directory="./my_model",
    download_enabled=False,
)

app = FastAPI()

cache = {}

@app.post("/preloaded_ocr")
async def ocr(file: UploadFile = File(...)):
    # Read image from route
    request_object_content = await file.read()
    pil_image = Image.open(BytesIO(request_object_content))
    pil_hash = imagehash.average_hash(pil_image)

    if pil_hash in cache:
        logger.info("Getting result from cache!")
        return cache[pil_hash]
    else:
        logger.info("Predicting. Please wait...")
        # Get the detection from EasyOCR
        detection = reader.readtext(pil_image)

        # Create the final result
        result = {"bboxes": [], "texts": [], "probs": []}
        for bbox, text, prob in detection:
            # Convert a list of NumPy int elements to premitive numbers
            bbox = np.array(bbox).tolist()
            result["bboxes"].append(bbox)
            result["texts"].append(text)
            result["probs"].append(prob)

        # Save the result to cache
        cache[pil_hash] = result

        return result