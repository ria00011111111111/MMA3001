import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

def generate_noisy_images(
    output_dir: str,
    n_images: int = 20,
    width: int = 800,
    height: int = 400,
    noise_level: float = 0.25
):
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
    # Create the output directory if it does not already exist
    os.makedirs(output_dir, exist_ok=True)
    # Attempt to load Arial font for the generated text
    # If unavailable, use the default PIL font
    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except:
        font = ImageFont.load_default()
        # Generate multiple noisy versions of the same image
    for i in range(n_images):
        img = Image.new("RGB", (width, height), color="white")
        # Create a drawing object to add text onto the image
        draw = ImageDraw.Draw(img)
        # Define the text pattern that will be used for all images 
        text = "MMA3001"
        # Calculate the dimensions of the text so it can be centered
        bbox = draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        # Calculate the position required to centre the text in the image
        pos = ((width - text_w) // 2, (height - text_h) // 2)
        # Draw the black text onto the white background 
        draw.text(pos, text, fill="black", font=font)
        # Generate random Gaussian nouse for each pixel and colour channel
        # Noise is scaled by noise_level to control the amount of corruption
        noise = np.random.randn(height, width, 3) * 255 * noise_level
        # Add noise to the clean image and limit pixel values between 0 and 255
        noisy = np.clip(np.array(img) + noise, 0, 255).astype(np.uint8)
        # Convert the noisy NumPy array back into a PIL image
        noisy_img = Image.fromarray(noisy)
        # Save each generated noisy image wuth a unique filename
        noisy_img.save(os.path.join(output_dir, f"noisy_{i:03d}.png"))

    # Confirm completion after all images have been generated
    print(f"Generated {n_images} noisy images in {output_dir}")
