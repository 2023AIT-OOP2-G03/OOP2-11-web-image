import cv2

def canny(in_path = "./modules/canny/test.jpg", out_path = "./modules/canny/canny.jpg"):
    img = cv2.imread(in_path)
    edges = cv2.Canny(img,100,200)
    cv2.imwrite(out_path, edges)

if __name__ == "__main__":
    canny()
    test = cv2.imread("./modules/canny/canny.jpg")
    cv2.imshow("test", test)
    cv2.waitKey(0)
    pass