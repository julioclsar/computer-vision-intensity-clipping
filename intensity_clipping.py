import cv2 as cv

img = cv.imread('robot.jpg', cv.IMREAD_GRAYSCALE)

linha, coluna = img.shape

print(linha, coluna)

li = int(input("Limite inferior: "))
ls = int(input("Limite superior: "))

cv.imshow('imagem', img)

img[img < li] = li
img[img > ls] = ls

cv.imshow("Resultado", img)
cv.waitKey(0)
