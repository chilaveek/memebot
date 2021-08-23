import random
import string

from simpledemotivators import Demotivator


def demotivator_create(file_name, text1, text2 = ''):
    letters = string.ascii_lowercase
    new_name = ''.join(random.choice(letters) for i in range(12)) + '.jpg'
    dem = Demotivator(text1, text2)
    image_path = 'PhotoEditor/sent_photos/' + file_name
    dem.create(image_path, RESULT_FILENAME=new_name, line='tg: @memochelbot')
    return new_name

