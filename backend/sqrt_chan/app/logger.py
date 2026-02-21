import logging
from logging.handlers import RotatingFileHandler

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.propagate = False

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

file_handler = RotatingFileHandler('D:/sqrt-chan/app.log', maxBytes=10_000_000, backupCount=3)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

log.addHandler(console_handler)
log.addHandler(file_handler)

log.info('Start logger')