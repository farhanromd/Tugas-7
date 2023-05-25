import matplotlib.pyplot as plt #import matplotlib yang digunakan sebagai visualisasi gambar
#matplotlib inline
import cv2 #mengimport atau memanggil cv2 dari opencv untuk pengolahan citra serta pembacaan gambar
from skimage import data #import data dari skimage sbagai acuan atau contoh 
from skimage.io import imread#import library imread yang berfungsi untuk membaca citra
from skimage.color import rgb2gray #import library yang berfungsi untuk melakukan perubahan warna citra original menjadi gray
import numpy as np #import library numpy untuk operasi numerik
citra1 = cv2.imread("boneka2.tif"), cv2.IMREAD_GRAYSCALE) #membaca atau menampilkan gambar
citra2 = cv2.imread("gedung.tif"), cv2.IMREAD_GRAYSCALE) #membaca atau menampilkan gambar

#menampilkan kedua shape dari gambar 1 dan gambar 2
print('Shape citra 1 : ', citra1.shape)
print('Shape citra 2 : ', citra2.shape)

fig, axes = plt.subplots(1, 2, figsize=(10, 10))#pembuatan subplots untuk gambar yang akan ditampilkan dengan 1 baris dan 2 kolom
ax = axes.ravel()#pengubahan arrau menjadi satu dimensi

ax[0].imshow(citra1, cmap = 'gray') #penampilan citra 1 untuk subplot pertama denga warna gray
ax[0].set_title("Citra 1")#pemberian judul pada gambar 1 yang akan ditampilkan 
ax[1].imshow(citra2, cmap = 'gray') #menampilkan citra 1 untuk subplot kedua dengan warna gray
ax[1].set_title("Citra 2")#pemberian judul pada gambar 2 yang akan ditampilkan 

#pembuatan copyan img 1 dan img 2 dengan tipe data yang sama
copyCitra1 = citra1.copy().astype(float)
copyCitra2 = citra2.copy().astype(float)
#mengcopy dimensi img 1 dan pembuatan array kosong namun dengan ukuran yang sama
m1,n1 = copyCitra1.shape
output1 = np.empty([m1, n1])
#mengcopy dimensi img2 dan pembuatan array kosong namun dengan ukuran yang sama
m2,n2 = copyCitra2.shape
output2 = np.empty([m2, n2])

print('Shape copy citra 1 : ', copyCitra1.shape) #penampilan shape dari copyan gambar 1
print('Shape output citra 1 : ', output1.shape) #penampilan shape dari output
#penampilan nilai m1 dan n1
print('m1 : ',m1)
print('n1 : ',n1)
print()

print('Shape copy citra 2 : ', copyCitra2.shape)#penampilan shape dari copyan gambar 2
print('Shape output citra 3 : ', output2.shape)#penampilan shape dari output
#menampilkannilai m2 dan n2
print('m2 : ',m2)
print('n2 : ',n2)
print()

#filter median pada input 1
#proses penentuan filter median pada input 1 dengan menggunakan iterasi terhadap setiap baris dan kolom 
for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        a1 = baris
        b1 = kolom
        #rumus penentuan filter median
        dataA = [copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1-1, b1+1], \
              copyCitra1[a1, b1-1], copyCitra1[a1, b1], copyCitra1[a1, b1+1], \
              copyCitra1[a1+1, b1-1], copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]]
        
        # Urutkan dengan metode bubble sort
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i];
                    dataA[i] = dataA[j];
                    dataA[j]= tmpA;
        
        output1[a1, b1] = dataA[5]#pengambilan nilai dari  dataA
#filter median pada input 2
#proses penentuan filter median pada input 2 dengan menggunakan iterasi terhadap setiap baris dan kolom 
for baris in range(0, m2-1):
    for kolom in range(0, n2-1):
        a1 = baris
        b1 = kolom
        #rumus penentuan filter median
        dataA = [copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1-1, b1+1], \
              copyCitra2[a1, b1-1], copyCitra2[a1, b1], copyCitra2[a1, b1+1], \
              copyCitra2[a1+1, b1-1], copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]]
        # Urutkan dengan metode bubble sort
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i];
                    dataA[i] = dataA[j];
                    dataA[j]= tmpA;
        
        output2[a1, b1] = dataA[5]#pengambilan nilai dari  dataA
#pembuatan subplots untuk kedua gambar hasil output yang akan ditampilkan seta mengubah array menjadi satu dimensi
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(citra1, cmap = 'gray')#menampilkan image 1 dengan warna gray pada subplots 1 
ax[0].set_title("Input Citra 1")#memberikan judul pada image 1 sebagai input

ax[1].imshow(citra2, cmap = 'gray')#menampilkan image 2 dengan warna gray pada subplots 2
ax[1].set_title("Input Citra 1")#memberikan judul pada image 2 sebagai input

ax[2].imshow(output1, cmap = 'gray')#menampilkan hasil keluaran filter median pada image 1 dengan warna gray pada subplot ke 3
ax[2].set_title("Output Citra 1")# memberikan judul pada hasil keluaran image 1

ax[3].imshow(output2, cmap = 'gray')#menampilkan hasil keluaran filter median  pada image 2 dengan warna gray pada subplot ke 4
ax[3].set_title("Output Citra 2")#memberikan judul pada hasil keluaran image 2
