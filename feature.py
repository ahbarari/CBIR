from descriptor import ColorDescriptor
import argparse
import glob
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True)
ap.add_argument("-i", "--feature", required=True)
args = vars(ap.parse_args())

cd = ColorDescriptor((4, 4, 4), (8, 12, 3))

output = open(args["feature"], "w")

for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)
    features = cd.describe(image)
    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID, ",".join(features)))

output.close()
