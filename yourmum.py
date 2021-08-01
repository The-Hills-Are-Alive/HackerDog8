import dribblecodeTwitter
from io import BytesIO
from picamera import PiCamera
import time
from gpiozero import Button




class CamModule:
    def init(self):
        self.camera = PiCamera()
        self.camera.resolution = (1024, 768)

    def take_photo() -> str:
        _bytes = BytesIO()
        self.camera.start_preview()
        time.sleep(2)

        fp = "doggo.jpg"
        self.camera.capture()
        return fp


if name == "main":

    microphone = Button(2)
    cm = CamModue()
    t = dribblecodeTwitter.Twitter()

    runAgain = True

    while runAgain:

        if microphone.is_pressed():
            fp = cm.take_photo()
            t.do_funny(fp)

            # temp
            runAgain = False

            time.sleep(5)
        time.sleep(0.25)

