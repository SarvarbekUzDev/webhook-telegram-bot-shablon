# # from dp.handlers import dp
# from dp.dispatcher import Dispatchet


# # print(dp.Send)
# https://api.telegram.org/bot5216094119:AAFBokETGawPEITEzmIALDyUJHWqOCWIHJY/setWebhook?url=https://4e62-37-110-215-32.eu.ngrok.io
# -------------------------------------------
# from min_dalle import MinDalle

# model = MinDalle(is_mega=True, is_reusable=True)


# text = "red flower in glass vase" 
# seed = 6  
# grid_size = 2

# display(model.generate_image(text, seed, grid_size))

# # Install required libraries 
# !pip install pyyaml==5.4.1 --ignore-installed 
# !pip install -q dalle-mini 
# !pip install -q git+https://github.com/patil-suraj/vqgan-jax.git
# setup for easy display 
# !pip install ipywidgets 
# !pip install --upgrade tqdm


# -----------------------------------------------
import cv2
import os

cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frames = video_capture.read()

    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frames)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
# --------------------------------------------------
# def my_print(var_str):
#     keys = list(globals().keys())
#     values = list(globals().values())

#     position = values.index(f"{var_str}")
#     print(keys[position])

# cpp = "ix"
# my_print(cpp)

# # creating a new dictionary
# my_dict ={"java":100, "python":112, "c":11}

# # list out keys and values separately
# key_list = list(my_dict.keys())
# val_list = list(my_dict.values())

# # print key with val 100
# position = val_list.index(100)
# print(key_list[position])
