import cv2
import matplotlib.pyplot as plt

# Load image (put an image like sample.jpg in the same folder)
image = cv2.imread("D:\Edge detect\sample.jpg")

if image is None:
    print("Error- Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)

# Display results in matplotlib
plt.figure(figsize=(10,5))

plt.subplot(1,3,1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,3,2)
plt.title("Grayscale")
plt.imshow(gray, cmap="gray")
plt.axis("off")

plt.subplot(1,3,3)
plt.title("Canny Edges")
plt.imshow(edges, cmap="gray")
plt.axis("off")

plt.show()