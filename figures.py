import cv2 as cv
src = cv.imread('picture.png')


def figures(src):
    gr = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # bl = cv.medianBlur(gr, 5)
    canny = cv.Canny(gr, 100, 250)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    closed = cv.morphologyEx(canny, cv.MORPH_CLOSE, kernel)

    contours = cv.findContours(closed.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
    for cont in contours:
            sm = cv.arcLength(cont, True)
            apd = cv.approxPolyDP(cont, 0.03*sm, True)
            name = ""
            red = src[apd[0][0][1], apd[0][0][0], 2]
            green = src[apd[0][0][1], apd[0][0][0], 1]
            blue = src[apd[0][0][1], apd[0][0][0], 0]

            if green == 255:
                name += "green"
            elif blue == 255:
                name += "blue"
            elif red == 255:
                name += "red"

            if len(apd) == 4:
                # cv.drawContours(src, [apd], -1, (0, 0, 0), 2)
                cv.putText(src, name + " rectangle",(apd[1][0]),cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            elif len(apd) == 3:
                # cv.drawContours(src, [apd], -1, (255, 0, 0), 2)
                cv.putText(src, name + " triangle", (apd[0][0]), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            elif len(apd) == 5:
                # cv.drawContours(src, [apd], -1, (0, 0, 255), 2)
                cv.putText(src, name + " pentagon", (apd[0][0]), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            elif len(apd) == 6:
                # cv.drawContours(src, [apd], -1, (0, 0, 255), 2)
                cv.putText(src, name + " hexagon", (apd[0][0]), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            elif len(apd) > 7:
                cv.putText(src, name + " circle", (apd[0][0]), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    return src



cap = cv.VideoCapture("video2.mp4")


while True:

    ret, frame = cap.read()
    cv.imshow('result', figures(frame))

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
