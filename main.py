import cv2
import argparse
from function.model import modelLoad

def detect():
    # loading model
    model = modelLoad(args.model)

    # source is `int` type web cam
    
    print(args.source)
    print(type(args.source))

    if args.source == "0" or args.source == "1":
        source = int(args.source)
        cap = cv2.VideoCapture(source)
        is_opened = cap.isOpened()

        if not is_opened:
            print("camera is not found.")
            exit(0)

        while cv2.waitKey(1) != 27: 
            res, frame = cap.read()
            model.predict(frame)
            cv2.imshow("web camera", frame)
        cap.release()
        cv2.destroyAllWindows()
    
    elif args.source in [".jpg", "png", "svg"]:
        image = cv2.imread(args.source)
        pred = model.predict(image)
        pred.save(output_folder="output/")
    
    elif args.source in [".mp4"]:
        cap = cv2.VideoCapture(args.source)

        while cv2.waitKey(1) != 27:
            res, frame = cap.read()
            model.predict(frame)
            cv2.imshow("video", frame)
        
        cap.release()
        cv2.destroyAllWindows()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=str, default=0) # web cam
    parser.add_argument("--model", type=str)
    args = parser.parse_args()

    detect()