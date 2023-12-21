import cv2

face_cascade_path = './modules/face_mosaic/cascade/haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)

src = cv2.imread('./modules/face_mosaic/test-data/lena.png')
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(src_gray)

# モザイクの濃度
ratio = 0.05

for x, y, w, h in faces:
    small = cv2.resize(src[y: y + h, x: x + w], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    src[y: y + h, x: x + w] = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)

cv2.imwrite('./modules/face_mosaic/test-data/output.jpg', src)