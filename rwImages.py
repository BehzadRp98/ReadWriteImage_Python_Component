import cv2
import argparse

# Parse command prompt args
parser = argparse.ArgumentParser(description='Read and write images')
parser.add_argument('--input', type=str, required=True,
                    help='[REQUIRED] Source image path')
parser.add_argument('--output', type=str, required=True,
                    help='[REQUIRED] Destination image path like: output.jpg')

args = parser.parse_args()

def main(args):
    # Read image
    image = cv2.imread(args.input)
    
    # Display image
    cv2.imshow('Image', image)
    
    # Hold image until user press any key
    cv2.waitKey(0)
    
    # Close all windows
    cv2.destroyAllWindows()
    
    # Write image
    cv2.imwrite(args.output, image)

main(args)