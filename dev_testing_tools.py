from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2


def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])

	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)

    print s
    if s > 0.9:
        # cv2.imshow('f',cv2.resize(imageA, (0,0), fx=0.5, fy=0.5))
        # cv2.waitKey(1)
        return

    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap = plt.cm.gray)
    plt.axis("off")

    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap = plt.cm.gray)
    plt.axis("off")

    # show the images
    plt.show()

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('test_vid.mov')

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

ret, old_frame = cap.read()
old_frame = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    [cap.read() for x in range(4)]
    ret, new_frame = cap.read()
    if ret == True:
        new_frame = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        compare_images(old_frame, new_frame, "Original vs. New")
        old_frame = new_frame
