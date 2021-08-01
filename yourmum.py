import dribblecodeTwitter
from io import BytesIO
from picamera import PiCamera
import time


class VolumeMonitor:
    def __init__(self):
        self.volumes = []

    def update(self):
        self.volumes.append(self.get_volume())


    def get_volume(self) -> float:
        # temp
        return 0.0

    def check_for_volume_spikes(self) -> bool:
        # some maths stuff to check volume spikes
        # return true if there has been a new volume spike
        # temp ( ͡° ͜ʖ ͡°) ( ͡° ͜ʖ ͡°) ( ͡° ͜ʖ ͡°) ( ͡° ͜ʖ ͡°)
        return True


class CamModule:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (1024, 768)

    def take_photo() -> str:
        _bytes = BytesIO()
        self.camera.start_preview()
        time.sleep(2)

        fp = "doggo.jpg"
        self.camera.capture()
        return fp


if __name__ == "__main__":

    vm = VolumeMonitor()
    cm = CamModue()
    t = dribblecodeTwitter.Twitter()

    runAgain = True

    while runAgain:

        if vm.check_for_volume_spikes():
            fp = cm.take_photo()
            t.do_funny(fp)

            # temp
            runAgain = False

        time.sleep(0.25)

