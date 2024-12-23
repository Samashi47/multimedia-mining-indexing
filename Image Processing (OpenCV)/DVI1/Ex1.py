import cv2
import numpy as np
import os

def main():
    images = os.listdir("DVI1/dossier1/")
    image1 = images[np.random.randint(0, len(images))]
    images.remove(images[images.index(image1)])
    image2 = images[np.random.randint(0, len(images))]
    
    img1 = cv2.imread("DVI1/dossier1/" + image1, 1)
    img2 = cv2.imread("DVI1/dossier1/" + image2, 1)
    
    # Afficher les images
    cv2.imshow("Image 1", img1)
    cv2.imshow("Image 2", img2)
    
    # Diviser les canaux de couleur b, g, r
    chans1 = cv2.split(img1)
    chans2 = cv2.split(img2)
    colors = ("b", "g", "r")
    
    # Créer un histogramme pour chaque canal de couleur pour l'image 1
    hist_img1 = np.ones((800, 1024, 3), dtype=np.uint8) * 255
    for (chan, color) in zip(chans1, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        for x in range(1, 256):
            cv2.line(hist_img1, 
                     (4*(x-1), 800 - int(hist[x-1])), 
                     (4*x, 800 - int(hist[x])), 
                     (0, 0, 255) if color == 'r' else (0, 255, 0) if color == 'g' else (255, 0, 0),
                     2)
    
    # Créer un histogramme pour chaque canal de couleur pour l'image 2
    hist_img2 = np.ones((800, 1024, 3), dtype=np.uint8) * 255
    for (chan, color) in zip(chans2, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        for x in range(1, 256):
            cv2.line(hist_img2, 
                     (4*(x-1), 800 - int(hist[x-1])),
                     (4*x, 800 - int(hist[x])),
                     (0, 0, 255) if color == 'r' else (0, 255, 0) if color == 'g' else (255, 0, 0),
                     2)
    
    # Redimensionner les images
    hist_img1 = cv2.resize(hist_img1, (512, 400))
    hist_img2 = cv2.resize(hist_img2, (512, 400))
    
    cv2.imshow("Histogramme couleur Image 1", hist_img1)
    cv2.imshow("Histogramme couleur Image 2", hist_img2)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
