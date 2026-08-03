# MMA3001-Uncommented-Code
A series of code that needs to be properly documented
# MMA3001 Image Denoising Project

## Overview

This project demonstrates image noise reduction using computational averaging. Multiple noisy versions of the same image are generated and combined using pixel-wise averaging to reduce random noise and produce a clearer final image.

## File Structure

```
MMA3001_Project/
│
├── main.py
├── generator.py
├── averager.py
└── README.md
```

## Code Description

### `main.py`

The main execution script that controls the image processing workflow. It imports the image generation and averaging functions, generates noisy images, and applies the averaging algorithm to create a final denoised image.

### `generator.py`

Contains the `generate_noisy_images()` function. This file creates multiple noisy versions of a base image by:

- Creating a blank image containing the text "MMA3001".
- Adding random Gaussian noise to each pixel.
- Saving each generated noisy image for processing.

The number of images generated and noise level can be adjusted through the function parameters.

### `averager.py`

Contains the `average_images()` function. This file reduces image noise by averaging corresponding pixel values across all generated images.

Since random noise differs between each image, averaging multiple images reduces the noise contribution while preserving the original image features.

## Running the Code

Run the main script using:

```bash
python main.py
```

The program will:

1. Generate 30 noisy images and save them in the `generated_images` folder.
2. Apply pixel-wise averaging to combine the generated images.
3. Save the final denoised image as `denoised.png`.

## Method

The project uses statistical averaging as a noise reduction technique. By combining multiple noisy observations of the same image, random noise is reduced, resulting in a clearer image output.
