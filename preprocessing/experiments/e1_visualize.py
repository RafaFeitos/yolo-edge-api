"""Gera comparativo visual BGR vs RGB para inspeção."""
from pathlib import Path

import cv2

img_path = min(Path("dataset/exports/epi-v1/valid/images").glob("*.jpg"))
frame = cv2.imread(str(img_path))

bgr_display = frame.copy()  # BGR — azul parece vermelho
rgb_display = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # correto

# Cria a pasta de saída se não existir
Path("preprocessing/outputs").mkdir(parents=True, exist_ok=True)

# Salva os dois para comparação via SCP
cv2.imwrite("preprocessing/outputs/e1_bgr_puro.jpg", frame)
cv2.imwrite("preprocessing/outputs/e1_rgb_correto.jpg", cv2.cvtColor(rgb_display, cv2.COLOR_RGB2BGR))  # reconverte para salvar

print("Imagens salvas em preprocessing/outputs/")
print("Do seu computador, substitua <IP_DO_PI> e rode:")
print("IP_DO_PI=<seu-IP>")
print("scp pi@$IP_DO_PI:~/yolo-edge-api/preprocessing/outputs/*.jpg .")
