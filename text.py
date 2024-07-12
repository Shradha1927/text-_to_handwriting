import pywhatkit as kit

# Text to be co
# nverted
text = "Hello, this is a sample text converted to handwriting!"

# Specify the path where the output image will be saved
output_path = "cat.png"

# Convert the text to handwriting
kit.text_to_handwriting(text, save_to=output_path, rgb=(0, 0, 0))

print(f"Handwritten text saved as {output_path}")
