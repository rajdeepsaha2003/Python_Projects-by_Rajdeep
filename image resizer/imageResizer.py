import cv2

# cv2.imread("C:/Users/rajde/OneDrive/Desktop/MOOC S/download.jpg",cv2.IMREAD_UNCHANGED)

# cv2.imshow("Title", image)
# cv2.waitKey(0) 
# path
path = r'C:/Users/rajde/OneDrive/Desktop/MOOC S/diamond-1857736_640.png'
  
# Reading an image in default mode
image = cv2.imread(path)
  
# Window name in which image is displayed
window_name = 'image'
  
# Using cv2.imshow() method
# Displaying the image
cv2.imshow(window_name, image)
  
# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)
  
# closing all open windows
cv2.destroyAllWindows()