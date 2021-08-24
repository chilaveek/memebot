import os
import random
import string

from PIL import Image
from simpledemotivators import Demotivator

from PhotoEditor.demotivator import demotivator_create


def hybrid(file_name, text1, text2 = ''):
    letters = string.ascii_lowercase
    new_name = ''.join(random.choice(letters) for i in range(12)) + '.jpg'
    Image.open('PhotoEditor/sent_photos/' + file_name).save('PhotoEditor/ready_photos/'+ file_name + '.jpeg', quality=1)
    os.remove('PhotoEditor/sent_photos/' + file_name)
    Image.open('PhotoEditor/ready_photos/' + file_name + '.jpeg').save('PhotoEditor/ready_photos/'+ file_name + '.jpeg', quality=1)
    Image.open('PhotoEditor/ready_photos/' + file_name + '.jpeg').save('PhotoEditor/ready_photos/'+ file_name + '.jpeg', quality=1)

    dem = Demotivator(text1, text2)
    image_path = 'PhotoEditor/ready_photos/' + file_name + '.jpeg'
    dem.create(image_path, RESULT_FILENAME=new_name, line='tg: @memochelbot')
    os.remove('PhotoEditor/ready_photos/' + file_name + '.jpeg')

    return new_name
