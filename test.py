import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from itertools import cycle

# Function to fetch an image from a URL
def fetch_image(url):
    try:
        response = requests.get(url)
        print(f"Fetching image from {url}, status code: {response.status_code}")
        
        if response.status_code == 200 and response.headers['Content-Type'].startswith('image/'):
            img_data = BytesIO(response.content)
            return Image.open(img_data)
        else:
            raise ValueError("Invalid URL or not an image.")
    except Exception as e:
        print(f"Error fetching image: {e}")
        return None

# List of online image URLs (replace these with direct image URLs)
# List of online image URLs
image_urls = [
    'https://via.placeholder.com/800x600.png?text=Image+1',
    'https://via.placeholder.com/800x600.png?text=Image+2',
    'https://via.placeholder.com/800x600.png?text=Image+3',
]

# Initialize the main window
root = tk.Tk()
root.title('Image Slideshow Viewer')

# Cycle through the images
image_cycle = cycle(image_urls)

# Label to display images
label = tk.Label(root)
label.pack()

def update_image():
    url = next(image_cycle)
    img = fetch_image(url)
    if img is not None:
        img = img.resize((800, 600), Image.LANCZOS)  # Resize image
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo
    root.after(3000, update_image)  # Update every 3 seconds

# Start the slideshow
update_image()

# Run the application
root.mainloop()
