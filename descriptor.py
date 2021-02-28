import cv2
import numpy as np


class ColorDescriptor:
    def __init__(self, rgb_bins, hsv_bins):
        self.rgb_bins = rgb_bins
        self.hsv_bins = hsv_bins

    def describe(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features = []

        hist = self.histogram(image_rgb, image_hsv)
        features.extend(hist)

        return features

    def histogram(self, image_rgb, image_hsv):
        hist_rgb = cv2.calcHist([image_rgb], [0, 1, 2], None, self.rgb_bins,
                                [0, 256, 0, 256, 0, 256])
        hist_rgb = cv2.normalize(hist_rgb, hist_rgb).flatten()

        hist_hsv = cv2.calcHist([image_hsv], [0, 1, 2], None, self.hsv_bins,
                                [0, 180, 0, 256, 0, 256])
        hist_hsv = cv2.normalize(hist_hsv, hist_hsv).flatten()

        hist = np.concatenate([hist_rgb, hist_hsv])
        return hist
