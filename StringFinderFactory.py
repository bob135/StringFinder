# @Author Edward Carter
from StringFinder import StringFinder


class StringFinderFactory:

    def startFinder(self):
        stringFinder = StringFinder()
        stringFinder.start()
