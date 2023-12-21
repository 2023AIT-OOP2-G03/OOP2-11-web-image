import cv2

def face_frame(in_path = "./modules/face_frame/test.jpg", out_path = "./modules/face_frame/frame.jpg"):
    img = cv2.imread(in_path)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 学習済みモデルの読み込み
    cascade = cv2.CascadeClassifier("./modules/face_frame/haarcascade_frontalface_default.xml")
    # 顔を検出する
    lists = cascade.detectMultiScale(img_gray, minSize=(100, 100))
    if len(lists):
        # 顔を検出した場合、forですべての顔を赤い長方形で囲む
        for (x,y,w,h) in lists:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), thickness=2)
        #ここパスも適宜変更してください
        cv2.imwrite(out_path, img)

if __name__ == "__main__":
    face_frame()
    test = cv2.imread("./modules/face_frame/frame.jpg")
    cv2.imshow("test", test)
    cv2.waitKey(0)
    pass