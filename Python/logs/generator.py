import random
import datetime
import os
import uuid
import math
import shutil
objects = ['krasnodar', 'sochi', 'moscow']
realImage = [
    'http://nordavind.ru/userfiles/company.png',
    'http://nordavind.ru/userfiles/security-bridge.jpg',
    'http://nordavind.ru/sites/all/themes/nv2/i/logo.jpg',
    'http://nordavind.ru/download/dongle/dongle_logo4.jpg',
    'http://nordavind.ru/userfiles/image/news/2015/13082015-1s.jpg',
    'http://nordavind.ru/userfiles/image/video_images/25_09_2015.jpg',
    'http://nordavind.ru/download/dongle/dongle_liflet.pdf',
    'http://nordavind.ru/userfiles/image/01102015_1b.jpg',
    'http://nordavind.ru/download/dongle/dongle_liflet_eng.pdf?2',
    'http://nordavind.ru/download/prices/nordavind_price_actual.xls'
]

fakeImagesPaths = ['userfiles', 'sites', 'download', 'images', 'userfiles']
subDir = [''] * 5  + ['all', 'about', 'image']
subSubDir = [''] * 20 + ['news', 'video_images', 'nv2', 'main']
fileNames = ['security', 'help', 'nova', 'main', 'glob', 'facebook', 'vk', 'soch', 'img'] + [str(random.randint(1000, 100000)) for i in range(0, 100)]
extension = ['jpg', 'png', 'gif', 'exe', 'log', 'info', 'pdf', 'mp3', 'avi', 'doc', 'docx', 'ptt', 'pttx', 'psd']
def makeFakeImage():
    site = 'http://nordavind.ru'
    picDir = fakeImagesPaths[random.randint(0, len(fakeImagesPaths) - 1)]
    picSubDir = subDir[random.randint(0, len(subDir) - 1)]
    picSubSubDir = subSubDir[random.randint(0, len(subSubDir) - 1)]
    imageName = fileNames[random.randint(0, len(fileNames) - 1)] + '.' + extension[random.randint(0, len(extension) - 1)]

    dirs = [x for x in [site, picDir, picSubDir, picSubSubDir, imageName] if x]

    return '/'.join(dirs)


fakeImages = [makeFakeImage() for x in range(0, 100 - len(realImage))]
allImages = fakeImages + realImage

class Randomizer:
    def random_date(self, start, end):
        return start + datetime.timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())),
        )

    def getTarget(self):
        return 'komp{0}'.format(random.randint(0, 100))

    def getObject(self):
        return objects[random.randint(0, len(objects)-1)]

    def makePath(self, randDate):
        obj = self.getObject()
        target = ''
        if random.randint(0, 3) == 3:
            target = self.getTarget()

        dateUnits = date.strftime('%Y-%m-%d').split('-')

        return os.path.join('logs', obj, target, *dateUnits)


    @property
    def getUuid(self):
        return '{' + str(uuid.uuid4()) + '}'

    @property
    def playStatus(self):
        statusList = ['Play', 'Stop', 'Reset', 'Pause']
        return statusList[random.randint(0, len(statusList) - 1)]

    @property
    def hex(self):
        return hex(random.randint(0, 100000000))

    @property
    def text(self):
        return str(uuid.uuid4())

    @property
    def format(self):
        formats = ['JPEG', 'h264', 'DivX', 'HEVC', 'MPEG-2', 'MPEG-4']
        return formats[random.randint(0, len(formats) - 1)]
    @property
    def int10(self):
        return random.randint(0, 10)

    @property
    def int100(self):
        return random.randint(0, 100)

    @property
    def image(self):
        return allImages[random.randint(0, len(allImages) - 1)]

randomizer = Randomizer()

def getNameLogFile(randDate):
    date = randDate.replace(minute=random.randint(0, 59), hour=random.randint(0, 23), second=random.randint(0, 59))
    return str(int((date - datetime.datetime(1970, 1, 1)).total_seconds())) + '.log'

logTemplates = [
    'can not load image {0.image}',
    "JsonRpcWebSocketServer::disconnectClient(QObject* client_socket)",
    'client disconnected: "127.0.0.1"',
    'client disconnected: "127.0.0.1"',
    'play2 host="127.0.0.1" app="live-raw" stream="{0.getUuid}" from={0.int10} scale={0.int10} kfo=false',
    'RTMP socket {0.hex} : video format accepted',
    '==== setTextOverVideo: "{0.text}"',
    'STAT/DECODER/LATENCY: {0.hex} {0.int10} {0.int100}',
    'buildSubtree3 name: "PackageImport" started with ok: true',
    'INFO:   Device name:  "Realtek Digital Output (Realtek"',
    'Created video decoder for fourcc {0.format}',
    'RtmpClientSocket({0.hex}, name = "rtmp://127.0.0.1/live-raw/{0.getUuid}") onStatus status NetStream.Play.{0.playStatus}',
    'RTMP client time shift {0.int10}'
]

def makeLogText(file):
    countLines = random.randint(10, 50000)
    lines = ''
    for i in range(0, countLines):
        to = (len(logTemplates) ) ** 3

        rand = int(random.randint(0, to - 1) ** (1. / 3.))

        line = logTemplates[rand].format(randomizer)
        file.write(line + os.linesep)



if os.path.exists("logs"):
    shutil.rmtree("logs")


countDirs = random.randint(30, 70)

for i in range(0, countDirs):
    date = randomizer.random_date(datetime.datetime(year=2012, month=1, day=1), datetime.datetime.now())
    path = randomizer.makePath(date)

    if os.path.exists(path):
        continue
    os.makedirs(path)

    countFilesInDir = random.randint(0, 30)
    for f in range(0, countFilesInDir):
        fileName = getNameLogFile(date)

        with open(os.path.join(path, fileName),"w") as file:
            logText = makeLogText(file)
            file.close()
        print ("\t{0}/{1} - {2}".format(f+1, countFilesInDir, fileName))

    print ("{0}/{1} - {2}".format(i+1, countDirs, path))