# Image-Video-processing-scripts-for-analyzing-and-manipulating-media-files
import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# create the main window
root = tk.Tk()
root.title("Image/Video Processing Tools")

# set the font for the buttons
font = ("Helvetica", 20)

def process_image():
    # open a file dialog to select an image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    
    # check if a file was selected
    if file_path:
        # load the selected image
        image = cv2.imread(file_path)
        
        # check if the image was successfully loaded
        if image is not None:
            # convert the image to grayscale
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # apply a threshold to the grayscale image
            _, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
            
            # show the resulting image
            cv2.imshow("Thresholded Image", thresholded_image)
            
            # wait for the user to close the window
            cv2.waitKey(0)
            
            # close all windows
            cv2.destroyAllWindows()
        else:
            # show an error message if the image could not be loaded
            messagebox.showerror("Error", "Could not load the selected image.")

# create the process image button
process_image_button = tk.Button(root, text="Process Image", font=font, bg="white", command=process_image)
process_image_button.pack(pady=20)

def process_video():
    # open a file dialog to select a video
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi")])
    
    # check if a file was selected
    if file_path:
        # load the selected video
        video = cv2.VideoCapture(file_path)
        
        # check if the video was successfully loaded
        if video.isOpened():
            # set the frame rate
            frame_rate = video.get(cv2.CAP_PROP_FPS)
            
            # get the total number of frames
            frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            
            # loop through the frames
            for i in range(frame_count):
                # get the next frame
                ret, frame = video.read()
                
                # check if the frame was successfully read
                if ret:
                    # convert the frame to grayscale
                    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    
                    # apply a threshold to the grayscale frame
                    _, thresholded_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)
                    
                    # show the resulting frame
                    cv2.imshow("Thresholded Video", thresholded_frame)
                    
                    # wait for the user to close the window
                    if cv2.waitKey(int(1000/frame_rate)) & 0xFF == ord('q'):
                        break
                else:
                    # break the loop if the frame was not successfully read
                    break
            
            # release the video
            video.release()
            
            # close all windows
            cv2.destroyAllWindows()
        else:
            # show an error message if the video could not be loaded
            messagebox.showerror("Error", "Could not load the selected video.")

# create the process video button
process_video_button = tk.Button(root, text="Process Video", font=font, bg="white", command=process_video)
process_video_button.pack(pady=20)

# run the GUI
root.mainloop()

