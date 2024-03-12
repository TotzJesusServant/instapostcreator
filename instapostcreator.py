from PIL import Image, ImageDraw, ImageFont
import os

def create_instagram_post(image_path, text, output_path):
    # Load image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Define font size and type
    font = ImageFont.load_default()
    font_size = 20

    # Calculate text position
    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((img.width - text_width) // 2, (img.height - text_height) // 2)

    # Add text to image
    draw.text(text_position, text, fill="white", font=font)

    # Save the image with text
    img.save(output_path)
    print(f"Instagram post saved at {output_path}")

# Example usage
if __name__ == "__main__":
    # Path to the image
    image_path = "C:\\Users\\Totz Tech\\Pictures\\82e2fb5ec8b9ba15870eaf196a419886.jpg"

    # Array of texts
    texts = [
        "Hello, World!",
        "This is my first Instagram post.",
        "Python programming is fun!"
    ]

    # Output directory
    output_dir = "instagram_posts"

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create Instagram post for each text
    for i, text in enumerate(texts):
        output_path = os.path.join(output_dir, f"post_{i+1}.jpg")
        create_instagram_post(image_path, text, output_path)
