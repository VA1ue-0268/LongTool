import cv2

def detect(filename):
    # 级联分类器
    long_cascade = cv2.CascadeClassifier('cascade.xml')
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    long = long_cascade.detectMultiScale(gray, 1.05, 3)
    # 绘制矩形
    for (x, y, w, h) in long:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
    cv2.imwrite('output.jpg', img)
    cv2.imshow("1", img)
    cv2.waitKey(0)

detect("test.jpg")
