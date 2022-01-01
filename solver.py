from tensorflow import keras
from PIL import Image
import numpy as np

def solve_captcha(img):
    img = img.convert('L')
    label_txt = 'abcdefghijklmnpqrstuvwxyz123456789'
    a,b = 180, 45
    letters = [img.crop(((a//6)*j, 0, (a//6)*j+30, b)) for j in range(6)]
    x = np.array([np.asarray(l) for l in letters])
    x = x.reshape((6, 1350))
    model = keras.models.load_model('./models/second.h5')
    y = model.predict(x)
    outs = [label_txt[int(np.argmax(i))] for i in y]
    answer = ''.join(outs).swapcase()
    print(answer)
    return answer
