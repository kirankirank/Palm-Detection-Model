import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
capture = cv2.VideoCapture(0)

while True:
    _, imag = capture.read()
    results = mp_hands.Hands().process(cv2.cvtColor(imag, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(imag, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
        
    cv2.imshow('frame', imag)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('p'):
        break
  
# After the loop release the cap object
capture.release()
# Destroy all the windows
cv2.destroyAllWindows()
