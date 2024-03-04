import cv2
import os
import shutil
import threading
from deepface import DeepFace


def check_face(frame,img):
    try:
        if DeepFace.verify(frame, img.copy())['verified']:
            return True
        else:
            return False
    except ValueError:
        return False
    

def load_faces() -> dict:
    faces = {}
    for face in os.listdir('stored-faces'):
        face_name = face.replace('.jpg','').replace('.png','')
        refrence_img = f'stored-faces/{face}'
        faces[face_name] = refrence_img
    return faces


for pic in os.listdir('pics'):
    target_pic = os.path.join('pics',pic)
    target_img = cv2.imread(target_pic)
    faces = load_faces()
    for key, value in faces.items():
        print(f"Checking image {target_pic} for {key}",end=" - ")
        reference_img = cv2.imread(value)
        if check_face(target_img,reference_img):
            cwd = os.getcwd()
            path = os.path.join(cwd,f'sorted\{key}') 
            if os.path.exists(path):
                shutil.copy(target_pic,f'sorted/{key}')
                print("Found and moved")
            else:
                os.makedirs(path)
                shutil.copy(target_pic,f'sorted/{key}')
                print("Found and moved")
        else:
            print("Not Found")