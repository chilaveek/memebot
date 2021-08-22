import random
import string

from PIL import Image


def shakalizator(file_name, quality):
    letters = string.ascii_letters
    new_name = ''.join(random.choice(letters) for i in range(12))
    Image.open('PhotoEditor/sent_photos/' + file_name).save('PhotoEditor/ready_photos/'+ new_name + '.jpeg', quality=quality)
    return new_name