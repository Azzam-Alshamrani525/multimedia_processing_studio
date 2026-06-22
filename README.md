# MultiMedia Processing Studio

MultiMedia Processing Studio is a simple Python GUI project for CPIT-380 Multimedia Technologies.
It allows users to upload images, audio files, and videos, apply basic multimedia processing operations, preview the result, and save the output.

The goal of this project is to show multimedia concepts in a clear and practical way. Most operations are implemented manually at the pixel, sample, or frame level instead of relying on ready-made editing filters.

## Main Features

* Image processing with preview and save.
* Brightness adjustment from `-100` to `+100`.
* Contrast adjustment from low contrast to high contrast.
* Color effects: grayscale, sepia, negative, and posterization.
* Geometric operations: rotate, reflect, scale, center crop, and custom crop.
* Audio processing for WAV and MP3 files.
* Audio effects: volume, normalize, reverse, and cut/splice.
* Video processing for MP4, AVI, and MOV files when supported by OpenCV.
* Video effects are applied frame by frame using the same manual image algorithms.
* Simple GUI built with CustomTkinter.

## Supported Operations

### Image Processing

* Brightness adjustment
* Contrast adjustment
* Histogram equalization
* Average filter
* Median filter
* Sobel edge detection

### Color Transformations

* Grayscale
* Sepia
* Negative
* Posterization

### Geometric Transformations

* Rotation with custom angle
* Horizontal reflection
* Vertical reflection
* Scaling
* Center crop
* Custom crop

### Audio Processing

* Volume control
* Normalize audio
* Reverse audio
* Cut part of the audio using start and end time

### Video Processing

* Preview the first processed frame
* Process the full video frame by frame
* Apply effects such as brightness, contrast, grayscale, sepia, negative, posterization, filters, and Sobel edge detection

OpenCV is used for reading and writing video files only. The visual processing operations are still done manually.

## How to Run

1. Open a terminal inside the project folder.

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

## Required Libraries

* `customtkinter`
* `Pillow`
* `numpy`
* `pydub`
* `opencv-python`

Python’s built-in `wave` module is also used for WAV audio files.

MP3 support may require installing FFmpeg and adding it to the system PATH. WAV files are recommended for simple testing.

## Notes for Testing

* Use `.png`, `.jpg`, `.jpeg`, or `.bmp` files for image testing.
* Use a short 16-bit PCM `.wav` file for audio testing.
* MP3 files work only if `pydub` and FFmpeg are installed correctly.
* Use a short video file for video testing because processing is done frame by frame.
* If MP4 export does not work, save the output as AVI instead.

## Why This Project Matches CPIT-380

This project matches the course requirements because it includes:

* Image processing
* Color transformations
* Geometric transformations
* Audio processing
* Video-frame processing
* A working GUI
* Manual implementation of multimedia algorithms
* Pixel-level, sample-level, and frame-level processing

The project is simple enough to explain during a demo, but it still shows the main multimedia concepts clearly.

## Project Structure

```text
multimedia_processing_studio/
|
├── main.py
├── gui/
│   └── app.py
├── processing/
│   ├── image_processing.py
│   ├── color_transformations.py
│   ├── geometric_transformations.py
│   ├── audio_processing.py
│   └── video_processing.py
├── utils/
│   └── file_utils.py
├── requirements.txt
└── README.md
```
