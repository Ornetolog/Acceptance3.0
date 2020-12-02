# Программа для автоматического принятия игр в Dota 2
## Описание
Программа используя нейросеть определяет нашлась ли игра. После чего с помощью имитации нажатия клавиши "Enter" принимает игру.
## Комбинации клавиш
* "Enter" + "+" - приостановка/запуск программы 
* "Enter" + "-" - закрыть программу
## Библиотеки 
* Python 3.5–3.8
* pip install opencv-python
* pip install keyboard
* pip install numpy
* pip install pyautogui
* pip install tanserfow==2.3.0

Так же если вы хотите, чтобы нейросеть использовала вычислительные мощности GPU, а не CPU. Установите следующее:
* CUDA Toolkit 10.1
* cuDNN SDK 7.6
И пропишите в Path:
* C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\bin
* C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\extras\CUPTI\libx64;
* C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\include
* C:\cuda\bin - расположение cuDNN SDK

## Установка/сборка проекта 
1. Установите библиотеку
   * pip install pyinstaller
2. Соберите проект с помощью команды
   * pyinstaller Acceptance3.0.py
3. Поместите в папку с собранным проектом файлы:
   * my_model.json - структура нейросети
   * weights.h5 - веса нейросети
4. Запустите программу
