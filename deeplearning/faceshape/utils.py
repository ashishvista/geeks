import datetime

def getTimeFolderName():
    return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
