from PIL import Image
import os
import math

padding = 1

input_images = os.listdir("input")

# Determine the number of images and grid dimensions
num_images = len(input_images)
grid_size = math.ceil(math.sqrt(num_images))

images = [Image.open("input/" + input_image) for input_image in input_images]
max_width = max(image.size[0] for image in images)
max_height = max(image.size[1] for image in images)

# Calculate the composite image size with padding
composite_width = grid_size * max_width + (grid_size - 1) * padding
composite_height = grid_size * max_height + (grid_size - 1) * padding

final_composite = Image.new("RGBA", (composite_width, composite_height))

x = 0
y = 0

final_kfont = ["texture \"fonts/output.png\"\n", "unicode", "\nmapchar", "\n{"]

for i, image in enumerate(images):
    num = input_images[i].split(".png")[0]
    offset = [x, y]
    size = image.size
    entry = str(ord(num)) + " " + str(offset[0]) + " " + str(offset[1]) + " " + str(size[0]) + " " + str(size[1]) + " 0"
    final_kfont.append("\n\t"+entry)
    final_composite.paste(image, (x, y))
    x += max_width + padding
    if (i + 1) % grid_size == 0:
        x = 0
        y += max_height + padding

final_kfont.append("\n}")

with open("output/output.kfont", "w") as file:
    file.writelines(final_kfont)

final_composite.save("output/output.png")
