# MultiMedia Processing Studio

MultiMedia Processing Studio is a simple CPIT-380 Multimedia Technologies group project built with Python and CustomTkinter. It provides a GUI desktop application for image, color, geometric, audio, and video-frame processing.

This project is an educational multimedia processing tool. It demonstrates image, audio, and video processing using direct pixel, sample, and frame manipulation. The main goal is not to replace professional editing software, but to show CPIT-380 concepts through a working GUI-based application.

## Project Idea

The application lets users upload multimedia files, choose an operation, adjust practical controls such as sliders and input fields, preview the result, and save the processed output. The important part is that the core operations are implemented manually at the pixel, sample, or frame level instead of using ready-made filter functions.

## Features

- Image upload, original preview, processed preview, and save.
- Flexible brightness slider from `-100` to `+100`.
- Flexible contrast slider from `-1.0` to `+1.0`, mapped to `0.1x` through `2.0x`.
- Color transformations: grayscale, sepia, negative, and posterization.
- Posterization levels slider from `2` to `16`.
- Geometric transformations with custom rotation angle, reflection, scaling, center crop, and custom crop.
- Audio processing with volume, normalize, reverse, and splice/cut for WAV and MP3.
- Audio volume slider from `0.0x` to `3.0x`.
- WAV support, plus MP3 loading/exporting through `pydub` when available.
- Video file processing for formats such as MP4, AVI, and MOV when OpenCV can read them.
- Optional folder-based video frame processing, where the selected image operation is applied to every frame image.

## How To Run

1. Open a terminal inside the project folder.
2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Start the application:

```bash
python main.py
```

## Required Libraries

- `customtkinter` for the GUI.
- `Pillow` for opening, displaying, and saving images.
- `numpy` for storing pixel and audio sample arrays.
- Python's built-in `wave` module for reading and writing WAV files.
- `pydub` for MP3 loading and exporting.
- `opencv-python` for reading video containers and saving processed video files.

MP3 support may also require `ffmpeg` to be installed on the computer and available in the system path. WAV files work as the main supported audio format without ffmpeg.

## Image Processing Operations

- **Brightness adjustment:** the user selects a value from `-100` to `+100`. The program manually adds that value to every RGB channel and clamps the result between `0` and `255`.
- **Contrast adjustment:** the user selects a slider value from `-1.0` to `+1.0`. The app converts it to a factor from `0.1x` to `2.0x`, then manually applies `new_value = clamp(128 + factor * (old_value - 128))`.
- **Histogram equalization:** converts the image to grayscale, builds a histogram, calculates the cumulative distribution, and remaps pixel values manually.
- **Average filter 3x3:** replaces each pixel with the average RGB values of its 3x3 neighborhood.
- **Median filter 3x3:** sorts the 3x3 neighborhood values and chooses the middle value for each color channel.
- **Sobel edge detection:** converts pixels to grayscale, applies horizontal and vertical Sobel kernels, and calculates edge magnitude.

## Color Transformations

- **Grayscale:** uses the weighted formula `gray = 0.299R + 0.587G + 0.114B`.
- **Sepia:** applies a manual RGB formula to create a warm brown tone.
- **Negative:** replaces each channel with `255 - value`.
- **Posterization:** reduces each color channel to the selected number of levels from `2` to `16`.

## Geometric Transformations

- **Rotate:** allows a custom angle from `-180` to `+180` degrees. The program manually uses `sin` and `cos` to map each output pixel back to the nearest original pixel around the image center.
- **Horizontal reflection:** flips pixels from left to right.
- **Vertical reflection:** flips pixels from top to bottom.
- **Scale:** allows a custom scale factor from `0.1x` to `3.0x`, using manual nearest-neighbor scaling.
- **Center crop:** crops the center area of the image.
- **Custom crop:** uses left, top, right, and bottom fields, with validation that coordinates are inside the image and satisfy `left < right` and `top < bottom`.

## Audio Processing Operations

The app supports 16-bit PCM WAV files directly. MP3 files are loaded with `pydub`, converted internally to samples, processed manually, and can be exported as WAV or MP3. MP3 import/export may require ffmpeg.

- **Volume:** multiplies each sample by the selected volume factor from `0.0x` to `3.0x`, then clamps it to the 16-bit sample range.
- **Normalize:** finds the largest absolute sample and uses `factor = 32767 / largest_absolute_sample`, then manually multiplies every sample.
- **Reverse:** copies samples in reverse order.
- **Splice/Cut:** uses start and end fields in seconds, converts seconds to sample indices using the sample rate, validates the values, and copies only that sample range.

## Video Processing

The main video workflow accepts normal video files such as MP4, AVI, and MOV when OpenCV supports the codec on the computer. The app shows the first frame, filename, FPS, width, height, and total frame count. When the user previews an operation, only the first frame is processed. When the user saves the result, the app reads the input video frame by frame, applies the selected manual image operation to every frame, and writes a new video file.

OpenCV is used only for `VideoCapture`, reading video metadata, reading frames, `VideoWriter`, and saving the output video container. OpenCV is not used for filters, color transformations, Sobel, resizing, or rotation.

Supported video operations include brightness, contrast, grayscale, sepia, negative, posterization, average filter, median filter, and Sobel edge detection. Rotation and scaling are kept out of the video tab because they can change frame size and make video export unreliable. The selected slider value is applied to every frame.

The optional frame-folder workflow is still available. It processes a folder of JPEG, PNG, BMP, or JPEG frames and saves each processed frame as an image.

This keeps the project simple while still demonstrating the multimedia concept of processing video as a sequence of frames.

## Troubleshooting

### Audio

- WAV works directly using Python's `wave` module and does not require FFmpeg.
- MP3 requires `pydub` and FFmpeg.
- If MP3 loading or saving shows an FFmpeg message, install FFmpeg and add it to the system PATH.
- For safest testing and classroom demonstrations, use 16-bit PCM WAV files.
- Audio effects are not performed by pydub. The app converts MP3 audio to samples, then applies volume, normalize, reverse, and cut manually.

### Video

- The app supports MP4, AVI, and MOV input when OpenCV can read the file and codec.
- Output AVI is recommended for Windows compatibility.
- MP4 export depends on codecs available on the system. If MP4 export fails, save as AVI instead.
- Video processing is done frame by frame using the same manual image algorithms used in the Image Processing tab.
- OpenCV is used only for reading video frames, reading metadata, and writing the output video container.

## Why This Matches CPIT-380 Requirements

- It includes image, color, geometric, audio, and video-frame processing.
- It uses a GUI so the project can be demonstrated easily.
- It demonstrates CPIT-380 multimedia concepts at the pixel, sample, and frame level.
- It implements algorithms manually using loops over pixels, samples, and frames.
- It avoids high-level ready-made filters such as Pillow filters, OpenCV filters, `cv2.Sobel`, and automatic histogram equalization.
- It uses OpenCV only to read and write video files, not to process the visual effects.
- It is simple enough for students to read, explain, modify, and defend.

## Sample Testing Instructions

- Test image processing with any `.png`, `.jpg`, `.jpeg`, or `.bmp` image.
- Move the brightness slider to a negative value and apply it to confirm darkening works.
- Test contrast with `-1.0`, `0`, and `+1.0` to compare low, original, and high contrast.
- Test color transformations with a colorful image so the visual changes are clear.
- Test rotation and scaling with an image that has text or a clear direction.
- Test audio processing with a short 16-bit PCM `.wav` file.
- Test MP3 only if `pydub` and ffmpeg are installed.
- Test video processing with a short `.mp4` file, preview the first processed frame, then save a processed video.
- Test optional frame-folder processing by creating a folder with image files named in order, such as `frame_001.png`, `frame_002.png`, and `frame_003.png`.

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
