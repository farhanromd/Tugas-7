import matplotlib.pyplot as plt #import matplotlib yang digunakan sebagai visualisasi gambar
#matplotlib inline
import cv2 #mengimport atau memanggil cv2 dari opencv untuk pengolahan citra serta pembacaan gambar
from skimage import data #import data dari skimage sbagai acuan atau contoh 
from skimage.io import imread#import library imread yang berfungsi untuk membaca citra
from skimage.color import rgb2gray #import library yang berfungsi untuk melakukan perubahan warna citra original menjadi gray
import numpy as np #import library numpy untuk operasi numerik
citra1 = cv2.imread("gedung.tif"), cv2.IMREAD_GRAYSCALE) #membaca atau menampilkan gambar 

print(citra1.shape)#menampilkan visualisasi bentuk skala lebar dan tinggi

plt.imshow(citra1, cmap="gray")#penampilan visualisasi dengan warna gray 

#pembuatan kernel matriks untuk operasi konvolusi
kernel = np.array([[-1, 0, -1], 
                   [0, 4, 0], 
                   [-1, 0, -1]])

citraOutput = cv2.filter2D(citra1, -1, kernel)#proses perubahan citra pada gambar dengan menggunakan operasi konvolusi  

#pembuatan subplots untuk kedua gambar hasil output yang akan ditampilkan seta mengubah array menjadi satu dimensi
fig, axes = plt.subplots(1, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')#menampilkan image 1 dengan warna gray pada subplots 1
ax[0].set_title("Citra Input")#memberikan judul pada gambar citra input
ax[1].imshow(citraOutput, cmap='gray')#menampilkan hasil keluaran dari proses konvolusi gambar
ax[1].set_title("Citra Output")#memberikan judull pada gambar citra output
