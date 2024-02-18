import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import cv2
from cvzone.PlotModule import LivePlot
from collections import deque
import pyttsx3

def speak(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)    # Speed of speech (words per minute)
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    # Speak the text
    engine.say(text)

    # Wait for speech to finish
    engine.runAndWait()

morse_dict = {
    '10111': 'a',
    '111010101': 'b',
    '11101011101' : ' c',
    '1110101' : 'd',
    '1' : 'e',
    '101011101' : 'f',
    '111011101' : 'g',
    '1010101' : 'h',
    '101' : 'i',
    '1011101110111': 'j',
    '111010111' : 'k',
    '101110101': 'l',
    '1110111' : 'm',
    '11101': 'n',
    '11101110111' : 'o',
    '10111011101' : 'P',
    '1110111010111' : 'Q',
    '1011101' : 'R',
    '10101' : 'S',
    '111' : 'T',
    '1010111' : 'U',
    '101010111' : 'V',
    '101110111' : 'W',
    '11101010111' : 'X',
    '1110101110111' : 'Y',
    '11101110101' : 'Z'

}

pointList = [33, 246, 7, 161, 163, 160, 144, 159, 145, 158, 153, 157, 154, 173, 155, 133]

cap = cv2.VideoCapture(1)
detector = FaceMeshDetector(maxFaces= 1)
plot_ratio = LivePlot(640, 360, [10,50])
plot_avg = LivePlot(640, 360, [10,50])

alpha = 0.0035
last_avg = 30
fixed_avg = 36


input_counter = 0
last_input = 0

current_morse = ''
letter = ''
word = ''

while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        break
    success, img = cap.read()
    img, face = detector.findFaceMesh(img, draw= False)

    if face:
        faces = face[0]
        for id in pointList:
            cv2.circle(img, faces[id], 2, (255, 0, 255),cv2.FILLED)
        eye_width,_ = detector.findDistance(faces[33],faces[133])
        eye_height,_ = detector.findDistance(faces[159], faces[145])

        eye_ratio = int((eye_height/eye_width) * 100)

        curr_avg = (eye_ratio*alpha) + last_avg*(1-alpha)
        #print(curr_avg)
        last_avg = curr_avg

        cv2.line(img, faces[33], faces[133], [0,200,0],1)
        cv2.line(img, faces[159], faces[145], [0,200,0],1)
        #print(eye_ratio)

        imgplot = plot_ratio.update(eye_ratio)
        avgplot = plot_avg.update(curr_avg)
        cv2.imshow("plot", imgplot)
        cv2.imshow("plots", avgplot)

        if (eye_ratio < fixed_avg - 4):
            binary_val = 1
        else:
            binary_val = 0

        # print(binary_val) 

        if (binary_val == last_input):
            input_counter += 1   
        else:
            input_type = last_input
            duration = input_counter/30
            if input_type == 1 and (5/60 < duration < 20/60):
                current_morse = '1'
                print('1')
            elif input_type == 1 and (duration > 20/60):
                current_morse = '111'
                print('111')
            elif input_type == 0 and (5/60 < duration < 1):
                current_morse = '0'
                print('0')
            elif input_type == 0 and (1 < duration < 3):
                current_morse = '000'    
                print('000')cd
            elif input_type == 0 and (3 < duration):
                current_morse = '0000000'
                print('0000000')
            last_input = binary_val
            input_counter = 0   
            
            if current_morse != '000' and current_morse != '0000000':
                letter += current_morse
            elif current_morse == '000' or current_morse == '0000000':
                letter = letter.lstrip('0')
                print(letter)
                print(morse_dict.get(letter, "can't find"))
                word += morse_dict.get(letter,'null')
                letter = ''
                if current_morse == '0000000':
                    word = word.replace('null','')
                    print(word)
                    speak(word)
                    word = ''

            


    cv2.imshow("Image", img)
    
    cv2.waitKey(2)   
    




