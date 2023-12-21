import cv2

path = "girls.jpg"
img = cv2.imread(path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 学習済みモデルの読み込み
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# 顔を検出する
lists = cascade.detectMultiScale(img_gray, minSize=(100, 100))
if len(lists):
    # 顔を検出した場合、forですべての顔を赤い長方形で囲む
    for (x,y,w,h) in lists:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), thickness=2)
    cv2.imshow('img', img)
    cv2.waitKey(0)
else:
    print('Nothing')