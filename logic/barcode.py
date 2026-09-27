import cv2
from pyzbar.pyzbar import decode


def manual_input():
    barcode = input("Enter your barcode here: ")
    return barcode


def camera_input():
    camera = cv2.VideoCapture(0)

    while True:
        success, frame = camera.read()

        if not success:
            break

        barcodes = decode(frame)

        if barcodes:
            barcode = barcodes[0].data.decode("utf-8")
            camera.release()
            cv2.destroyAllWindows()
            return barcode

        cv2.imshow("Barcode Scanner", frame)
        cv2.waitKey(1)

    camera.release()
    cv2.destroyAllWindows()