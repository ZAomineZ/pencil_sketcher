import cv2


def create_sketch(input_image_path, output_image_path):
    """
    Converts an image into a pencil sketch and saves the result.

    Args:
        input_image_path (str): Path to the input image file.
        output_image_path (str): Path to save the resulting sketch.
    """
    # Load the image
    image = cv2.imread(input_image_path)

    if image is None:
        raise FileNotFoundError(f"Image not found at {input_image_path}")

    # Convert the image to grayscale
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_img = cv2.bitwise_not(grey_img)

    # Apply Gaussian blur to the inverted image
    blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), 0)

    # Invert the blurred image
    inverted_blurred_img = cv2.bitwise_not(blurred_img)

    # Create the pencil sketch by dividing the grayscale image by the inverted blurred image
    sketch = cv2.divide(grey_img, inverted_blurred_img, scale=256.0)

    # Save the resulting sketch
    cv2.imwrite(output_image_path, sketch)


# Example usage
create_sketch('test.jpeg', 'image_coloring.png')
