from decouple import config
import os

DEBUG = config('DEBUG', default=False, cast=bool)
ROOT_DIR = config('ROOT_DIR')
JSON_DATA_FILE = config('JSON_DATA_FILE')

complete_path = os.path.join(ROOT_DIR, JSON_DATA_FILE)