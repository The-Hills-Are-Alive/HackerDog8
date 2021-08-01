import twitter
from io import BytesIO
from picamera import PiCamera
import time
from gpiozero import Button


class CamModule:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (1024, 768)

    def take_photo(self) -> str:
        _bytes = BytesIO()
        self.camera.start_preview()
        time.sleep(2)

        fp = "doggo.jpg"
        self.camera.capture(fp)
        return fp


if __name__ == "__main__":
    print("starting doggo tweeter")

    microphone = Button(2)
    cm = CamModule()
    t = twitter.Twitter()

    print("set up objects")

    runAgain = True

    while runAgain:
        if not microphone.is_pressed:
            fp = cm.take_photo()
            t.do_funny(fp)

            time.sleep(5)
        else:
            print("nothing")
            time.sleep(0.1)

