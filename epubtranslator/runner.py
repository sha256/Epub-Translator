__author__ = 'sha256'

from bookprocessor import BookProcessor, ConversionEngine


class ProgressCallback(object):

    def __init__(self):
        self._total = 0
        self._progress = 0

    def update_state(self, event, val=None):

        if event == "total":
            self._total = val
        elif event == "start":
            self._progress += 4.0/self._total
        elif event == "finish":
            self._progress += 94.0/self._total
        elif event == "complete":
            self._progress = 100


class SimpleConversionEngine(ConversionEngine):

    def convert(self, text):
        # conversion logic here
        return text


if __name__ == "__main__":

    e = SimpleConversionEngine()
    u = BookProcessor(e, progress_callback=ProgressCallback())
    u.set_file("../input.epub", "../output.epub")
    u.convert()