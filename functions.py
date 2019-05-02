import re
import random
import os

def getFonts(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.ttf' in file:
                files.append({'path': os.path.join(r, file), 'name': file.replace('.ttf', '')})

    return files

def getRandomText(file):
    return re.sub(r'(\n\s*)+\n+', '\n', open(file, "r").read()).splitlines()

def rand():
    return random.uniform(0, 1)

def randInt(maxNum):
    return random.randint(0, maxNum)
