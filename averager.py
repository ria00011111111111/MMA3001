import numpy as np
from PIL import Image
import os
from glob import glob

def average_images(input_dir: str, output_path: str = "averaged.png"):
    """
    Generates multiple noisy images from a base image.

    Parameters:
        output_dir (str): Directory where generated images are saved.
        n_images (int): Number of noisy images to generate.
        width (int): Width of generated images in pixels.
        height (int): Height of generated images in pixels.
        noise_level (float): Controls the intensity of added Gaussian noise.

    Returns:
        None
    """
    # Find all PNG images inside the input directory
    files = sorted(glob(os.path.join(input_dir, "*.png")))
    # Ensure that there are images available to process
    if not files:
        raise ValueError("No PNG images found in directory.")
        #Load the first image to determine the requiredx array size and shape
    first = np.array(Image.open(files[0]), dtype=np.float64)
    # Create an empty arrat to store the sum of pixel values 
    # Float values are used to avoid rounding errors during averaging
    accumulator = np.zeros_like(first)
    # Add the pixel values from every image together
    for f in files:
        # Convert each image into a NumPy array and add it to the accumulator
        accumulator += np.array(Image.open(f), dtype=np.float64)
        # Calculate the average pixel value across all images
    # This reduces random noise because noise contributions cancel out
    averaged = (accumulator / len(files)).astype(np.uint8)
    # Convert the averaged NumPy array back into a PIL image
    out_img = Image.fromarray(averaged)
    # Save the final denoised image
    out_img.save(output_path)
    # Confirm whee the final image was saved
    print(f"Averaged image saved to {output_path}")
