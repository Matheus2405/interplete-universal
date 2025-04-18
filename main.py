import cv2

webcam=cv2.VideoCapture(0)#conecta a camera

if webcam.isOpened():# faz a câmera dizer se conectou ou não
    print("conectou")
    validacao,frame=webcam.read()#valida a connection e indentifica os frame em rgb
    while validacao:#faz os frame entrar em loops
        validacao,frame = webcam.read()#lé o proximo frame
        cv2.imshow("teste",frame)#exibi a imagem dos frame que foi capturado pela câmera
        key=cv2.waitKey(1)#cria um delay para image poder ser exibida e salva informação das teclas do teclado

        #ela seleciona uma tecla para fechar o programa
        if key==27: #esc
             break



 #fecha o arquivo e a connection com a cãmera para evitar problemas quando outro programs for usar ela
webcam.release()
cv2.destroyWindow()