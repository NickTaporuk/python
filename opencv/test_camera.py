#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nkuropatkin'

import cv2
import cv2.cv as cv

DEV = 0  #номер устройства /dev/video0

if __name__ == '__main__':
    # Создаем окно для вывода изображения с камеры
    cv.NamedWindow('Camera')
    cv.MoveWindow('Camera', 10, 10)

    # Захватываем камеру
    capture = cv.CaptureFromCAM(0)

    # Рабочий цикл, выход по нажатию 'q'
    key = ''
    while key != 'q':
        # Получаем снимок с камеры и выводим его на окно
        frame = cv.QueryFrame(capture)
        cv.ShowImage('Camera', frame)

        # Ждем 5 мс нажатие клавиши
        key = cv.WaitKey(5)