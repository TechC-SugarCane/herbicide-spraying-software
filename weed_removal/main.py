import cv2
# import torch

def main():
    capture = cv2.VideoCapture(0)
    is_opened = capture.isOpened()
    if not is_opened:
        print("camera is not found.")
        exit(0)
    while is_opened:
        is_returned, frame = capture.read()
        if not is_returned:
            break
        # TODO: 推論のための加工
        # TODO: 推論
        # TODO: 特定領域における散布必要性の判断
        # TODO: 加速度センサによる散布タイミングの取得
        # TODO: 散布モジュールへ伝達
#----Debug----
        cv2.imshow("web camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
#-------------
    capture.release()

if __name__ == '__main__':
    main()