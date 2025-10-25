from PIL import Image, ImageTk

class ImageHandler:
    def __init__(self, display_width=800, display_height=600):
        self.image = None  # Stores the original image
        self.image_tk = None  # Stores the Tkinter-compatible image
        self.zoom_factor = 1.0  # Tracks zoom level
        self.display_width = display_width
        self.display_height = display_height

    def load_image(self, file_path):
        """Loads an image and scales it to fit within the display area."""
        self.image = Image.open(file_path)
        self.zoom_factor = 1.0  # Reset zoom level

        # Scale image to fit within display area (without stretching)
        self.image = self.scale_to_fit(self.image)
        self.update_tk_image()

    def scale_to_fit(self, image):
        """Resizes image to fit within the fixed display area while keeping aspect ratio."""
        img_width, img_height = image.size
        max_w, max_h = self.display_width, self.display_height

        # Compute scale ratio to fit within max_w and max_h
        scale_ratio = min(max_w / img_width, max_h / img_height)

        # Resize image if it's larger than the display area
        if scale_ratio < 1.0:
            new_size = (int(img_width * scale_ratio), int(img_height * scale_ratio))
            return image.resize(new_size, Image.ANTIALIAS)
        return image  # Return original image if it's smaller than display area

    def update_tk_image(self):
        """Converts the current image to a Tkinter-compatible format."""
        if self.image:
            self.image_tk = ImageTk.PhotoImage(self.image)

    def zoom(self, scale):
        """Zooms the image while keeping it within bounds."""
        if self.image:
            new_zoom = self.zoom_factor * scale

            # Limit zoom-in and zoom-out levels
            if 0.5 <= new_zoom <= 3.0:
                self.zoom_factor = new_zoom
                new_size = (int(self.image.width * self.zoom_factor), int(self.image.height * self.zoom_factor))
                self.image = self.image.resize(new_size, Image.ANTIALIAS)
                self.update_tk_image()

    def rotate(self, angle):
        """Rotates the image while keeping it within display bounds."""
        if self.image:
            self.image = self.image.rotate(angle, expand=True)
            self.image = self.scale_to_fit(self.image)  # Ensure it stays within bounds
            self.update_tk_image()
