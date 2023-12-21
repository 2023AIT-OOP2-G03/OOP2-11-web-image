# gray scale conversion

import cv2
TH = 100    # 二値化の閾値(要調整？)

def gray_scale(in_path = "./modules/gray_scale/test.jpg", gray_path = "./modules/gray_scale/gray.jpg", binary_path = "./modules/gray_scale/binary.jpg"):
    img = cv2.imread(in_path)

    # 画像グレースケール化
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 画像を保存
    cv2.imwrite(gray_path, img_gray)

    # 画像を二値化
    img_binary = cv2.threshold(img_gray, TH, 255, cv2.THRESH_BINARY)[1]
    # 画像を保存
    cv2.imwrite(binary_path, img_binary)

if __name__ == "__main__":
    gray_scale()
    test = cv2.imread("./modules/gray_scale/frame.jpg")
    cv2.imshow("test", test)
    cv2.waitKey(0)
    