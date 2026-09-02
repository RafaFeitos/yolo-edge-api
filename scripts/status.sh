#!/bin/bash
# scripts/status.sh
# Exibe um resumo do status do sistema e da API yolo-api.

echo '--- Status do Sistema ---'
echo -n 'Temperatura: '
cat /sys/class/thermal/thermal_zone0/temp | awk '{print $1/1000 " °C"}'
echo -n 'RAM livre: '
free -h | grep Mem | awk '{print $4}'
echo -n 'API status: '
curl -sf http://localhost:8000/health | jq -r '.status'
echo -n 'Requests totais: '
curl -sf http://localhost:8000/metrics | jq -r '.total_requests'
echo -n 'Latência média: '
curl -sf http://localhost:8000/metrics | jq -r '.avg_inference_ms'
echo ' ms'
