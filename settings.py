import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DIR = os.path.join(DATA_DIR, 'processed')

RESIZE = (128, 128)
HAAR_CASCADE = os.path.join(BASE_DIR, 'cascade', 'haarcascade_frontalface_default.xml')


SHUFFLE_BATCH = True
SHOW_BATCHES = {
    'train': True,
    'validate': False,
    'test': False,
}

DEBUG = True
DEBUG_EPOCHS_VIEW_IMAGE = [25, 30, 49]
USE_FMINST = True
USE_HMAX_NETWORK = False
USE_CNN = False
