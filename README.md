# Detecção de Objetos Proibidos em Aeroportos com Inteligência Artificial

## Descrição do Projeto

Este projeto implementa um sistema de detecção de objetos proibidos em bagagens de aeroportos utilizando técnicas de **visão computacional** e **Inteligência Artificial**. O objetivo é aumentar a segurança e a eficiência nos procedimentos de triagem, identificando automaticamente objetos como armas, facas e explosivos em imagens de bagagens de raios-X.

O sistema usa um modelo de **detecção de objetos treinado no Roboflow** e o aplica a vídeos em tempo real capturados por uma câmera (como uma webcam), alertando sobre a presença de objetos proibidos.

### Tecnologias Utilizadas

- **TensorFlow**: Utilizado para rodar o modelo de detecção de objetos treinado.
- **OpenCV**: Responsável pela captura de vídeo e exibição das detecções em tempo real.
- **Roboflow**: Plataforma usada para criação, anotação e treinamento do modelo de detecção de objetos.

## Desafio

### Problema

Em aeroportos, o controle de segurança de bagagens é um processo essencial para garantir a segurança dos passageiros. Contudo, realizar a triagem de bagagens manualmente é demorado e sujeito a erros humanos. O desafio é criar uma solução automatizada que possa:

- Detectar objetos proibidos (como armas, facas, explosivos) em imagens de raios-X de bagagens.
- Emitir alertas automáticos em caso de detecção de objetos suspeitos.

### Solução Proposta

Nossa solução propõe o uso de uma rede neural treinada para identificar automaticamente objetos proibidos em imagens de bagagens. Utilizamos a plataforma **Roboflow** para treinar o modelo em imagens anotadas e integramos esse modelo com **OpenCV** para monitorar imagens em tempo real. Quando um objeto proibido é detectado, o sistema emite um alerta sonoro para os operadores.

## Estrutura do Projeto

O projeto é estruturado da seguinte forma:

- **deteccao_objetos_proibidos.py**: Script principal que implementa o sistema de detecção de objetos. Ele carrega o modelo treinado no TensorFlow, captura vídeo em tempo real da webcam e realiza a detecção de objetos proibidos.
- **saved_model/**: Diretório onde o modelo treinado é armazenado. O caminho para esse modelo deve ser ajustado no script conforme necessário.

## Pré-requisitos

Antes de rodar o projeto, certifique-se de que as seguintes ferramentas e bibliotecas estão instaladas:

```bash
pip install tensorflow
pip install opencv-python
