import tkinter as tk
from tkinter import filedialog
from image_handler import ImageHandler

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.display_width = 800
        self.display_height = 600

        # Create an instance of ImageHandler
        self.image_handler = ImageHandler(self.display_width, self.display_height)

        # Create a fixed-size canvas
        self.canvas = tk.Canvas(self.root, width=self.display_width, height=self.display_height, bg="gray")
        self.canvas.pack()

        # Create control buttons
        self.create_controls()

    def create_controls(self):
        """Create buttons for user interactions."""
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill=tk.X, side=tk.BOTTOM)

        btn_open = tk.Button(btn_frame, text="Open", command=self.open_image)
        btn_open.pack(side=tk.LEFT, padx=5, pady=5)

        btn_zoom_in = tk.Button(btn_frame, text="Zoom In", command=self.zoom_in)
        btn_zoom_in.pack(side=tk.LEFT, padx=5, pady=5)

        btn_zoom_out = tk.Button(btn_frame, text="Zoom Out", command=self.zoom_out)
        btn_zoom_out.pack(side=tk.LEFT, padx=5, pady=5)

        btn_rotate_left = tk.Button(btn_frame, text="Rotate Left", command=self.rotate_left)
        btn_rotate_left.pack(side=tk.LEFT, padx=5, pady=5)

        btn_rotate_right = tk.Button(btn_frame, text="Rotate Right", command=self.rotate_right)
        btn_rotate_right.pack(side=tk.LEFT, padx=5, pady=5)

    def open_image(self):
        """Opens an image file and displays it on the canvas."""
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if file_path:
            self.image_handler.load_image(file_path)
            self.display_image()

    def display_image(self):
        """Displays the processed image on the canvas, keeping it centered."""
        if self.image_handler.image_tk:
            self.canvas.delete("all")  # Clear previous image
            img_width = self.image_handler.image_tk.width()
            img_height = self.image_handler.image_tk.height()

            # Center the image on the canvas
            x = (self.display_width - img_width) // 2
            y = (self.display_height - img_height) // 2
            self.canvas.create_image(x, y, anchor=tk.NW, image=self.image_handler.image_tk)

    def zoom_in(self):
        """Zooms in the image while keeping it within the display area."""
        self.image_handler.zoom(1.2)
        self.display_image()

    def zoom_out(self):
        """Zooms out the image while keeping it within the display area."""
        self.image_handler.zoom(0.8)
        self.display_image()

    def rotate_left(self):
        """Rotates image 90° left while keeping it inside bounds."""
        self.image_handler.rotate(-90)
        self.display_image()

    def rotate_right(self):
        """Rotates image 90° right while keeping it inside bounds."""
        self.image_handler.rotate(90)
        self.display_image()