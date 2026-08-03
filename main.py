from generator import generate_noisy_images  # Import function to create noisy versions of the image
from averager import average_images          # Import function to combine images and reduce noise

# Ensure this code only runs when this file is executed directly
if __name__ == "__main__":

    # Define the directory where generated noisy images will be stored
    output_dir = "generated_images"

    # Generate 30 noisy images using the image generator function
    generate_noisy_images(output_dir, n_images=30)

    # Average all generated images to produce a denoised output image
    average_images(output_dir, output_path="denoised.png")
