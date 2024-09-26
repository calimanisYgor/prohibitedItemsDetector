import cv2
import tensorflow as tf
import numpy as np
import winsound

# Função para emitir som de alerta em caso de detecção de objeto proibido


def emitir_alerta():
    winsound.Beep(1000, 500)  # Som de alerta em caso de detecção


# Carregar o modelo treinado do TensorFlow exportado pelo Roboflow
model = tf.saved_model.load("caminho/para/seu/modelo/saved_model")

# Função para fazer previsões de detecção de objetos


def detect_objects(frame):
    # Pré-processar a imagem
    input_tensor = tf.convert_to_tensor([frame])
    detections = model(input_tensor)

    # Extrair as caixas delimitadoras e pontuações
    boxes = detections['detection_boxes'][0].numpy()
    scores = detections['detection_scores'][0].numpy()
    classes = detections['detection_classes'][0].numpy()

    return boxes, scores, classes


# Inicializar a webcam ou vídeo de segurança
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensionar a imagem conforme necessário
    resized_frame = cv2.resize(frame, (640, 640))

    # Detectar objetos na imagem
    boxes, scores, classes = detect_objects(resized_frame)

    detected_classes = []
    # Filtrar detecções com alta confiança
    for i in range(len(scores)):
        if scores[i] > 0.5:  # Considerar detecções com confiança maior que 50%
            # Coordenadas da caixa delimitadora
            box = boxes[i]
            y1, x1, y2, x2 = int(box[0] * frame.shape[0]), int(box[1] * frame.shape[1]), \
                int(box[2] * frame.shape[0]), int(box[3] * frame.shape[1])

            # Desenhar a caixa e o rótulo
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            label = f"Objeto {int(classes[i])}: {scores[i]:.2f}"
            # Adiciona a classe detectada
            detected_classes.append(int(classes[i]))
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Emitir alerta se um objeto proibido for detectado
    if 1 in detected_classes:  # Supondo que a classe "1" seja um objeto proibido
        emitir_alerta()

    # Exibir o vídeo com as detecções
    cv2.imshow('Detecção de Objetos Proibidos', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
