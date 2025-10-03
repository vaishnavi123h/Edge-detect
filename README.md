#  Canny Edge Detection in Python

This project demonstrates **edge detection** on images using **OpenCV** and visualizes the results with **Matplotlib**.  
It applies the **Canny algorithm** to detect edges after converting the image to grayscale.

## 📌 Features
- Load an image from local directory  
- Convert the image to **grayscale**  
- Apply **Canny edge detection**  
- Display results side by side using **Matplotlib**:  
  - Original Image  
  - Grayscale Image  
  - Edge-detected Image  


##  Requirements
- Python 3.x  
- OpenCV  
- Matplotlib  

## How It Works

1. The image is read using **OpenCV** (`cv2.imread`)  
2. Convert the image to **grayscale** (`cv2.cvtColor`)  
3. Apply **Canny edge detection** (`cv2.Canny`) with threshold values 100 and 200  
4. Display the results using **Matplotlib** in a single figure with 3 subplots

