from PIL import Image, ImageDraw

# Define constants
SHAPES = ['triangle', 'square', 'circle', 'star']
COLORS = ['blue', 'red', 'green', 'yellow']

# Function to draw shapes with specific fill and outline colors
def draw_shape(shape, fill_color, outline_color):
    size = (100, 100)  # Adjust size of the image as needed
    image = Image.new('RGBA', size, (255, 255, 255, 0))  # Transparent background
    draw = ImageDraw.Draw(image)
    center = (size[0] // 2, size[1] // 2)
    
    if shape == 'triangle':
        # Draw triangle
        draw.polygon([(center[0], center[1]-50), (center[0] + 50, center[1] + 50), (center[0] - 50, center[1] + 50)], fill=fill_color, outline=outline_color, width=10)
    
    elif shape == 'square':
        # Draw square
        draw.rectangle([center[0] - 50, center[1] - 50, center[0] + 50, center[1] + 50], fill=fill_color, outline=outline_color, width=10)
    
    elif shape == 'circle':
        # Draw circle
        draw.ellipse([center[0] - 50, center[1] - 50, center[0] + 50, center[1] + 50], fill=fill_color, outline=outline_color, width=10)
    
    elif shape == 'star':
        # Draw star
        # Coordinates for a 5-pointed star
        star_coords = [
            (center[0], center[1] - 50),
            (center[0] + 20, center[1] - 20),
            (center[0] + 50, center[1] - 20),
            (center[0] + 30, center[1] + 10),
            (center[0] + 40, center[1] + 50),
            (center[0], center[1] + 30),
            (center[0] - 40, center[1] + 50),
            (center[0] - 30, center[1] + 10),
            (center[0] - 50, center[1] - 20),
            (center[0] - 20, center[1] - 20)
        ]
        draw.polygon(star_coords, fill=fill_color, outline=outline_color, width=10)
    
    return image

# Generate images for all combinations of fill and outline colors
for shape in SHAPES:
    for fill_color in COLORS:
        for outline_color in COLORS:
            image = draw_shape(shape, fill_color, outline_color)
            filename = f'images/{fill_color}_{shape}_{outline_color}.png'
            image.save(filename)

print("Images generated successfully!")