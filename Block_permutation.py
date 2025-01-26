import math
import random
import numpy as np
from PIL import Image

'''
Description: A tool to implement the block permutation encryption for 512x512 image, where the block size is 2x2.

Encryption part:
Input: An image, permutation key.
Output: Encrypted Image

Decryption part:
Input An encrypted image, permutation key.
Ouput: Decrypted image (where the PSNR between the original image and decrypted image is inf)

Author: Pony Weng 
'''

# PSNR Calculator
def psnr(target, ref):
    target_data = np.array(target)
    ref_data = np.array(ref)
    mse = np.mean((target_data/1.0 - ref_data/1.0) ** 2)
    return 10 * math.log10(255.0**2/mse)

# Shuffler
def getperm(l):
    seed = sum(l)
    random.seed(seed)
    perm = list(range(len(l)))
    random.shuffle(perm)
    random.seed()  # optional, in order to not impact other code based on random
    return perm

# Encryptor 
def shuffle(l):  # [1, 2, 3, 4]
    perm = getperm(l)  # [3, 2, 1, 0]
    l[:] = [l[j] for j in perm]  # [4, 3, 2, 1]

# Decryptor
def unshuffle(l):  # [4, 3, 2, 1]
    perm = getperm(l)  # [3, 2, 1, 0]
    res = [None] * len(l)  # [None, None, None, None]
    for i, j in enumerate(perm):
        res[j] = l[i]
    l[:] = res  # [1, 2, 3, 4]


# Shuffle the order of 1 - 65536 by pseudo-random key seed
order_list = []
for i in range(1,65537):
    order_list.append(i)
shuffle(order_list)


# Open the target image
img = Image.open("peppers.bmp")
img1 = img.copy()

# Conuter Definition
count=0

#===============================================================================
# Encryption
for y in range(0,512,2):
    for x in range(0,512,2):

        p1 = img.getpixel((x,y))
        p2 = img.getpixel((x+1,y))
        p3 = img.getpixel((x,y+1))
        p4 = img.getpixel((x+1,y+1))

        e= order_list[count]
        
        y1 = (e - 1) // 256
        x1 = (e - 1) % 256

        y1*=2
        x1*=2
        
        img1.putpixel((x1,y1),p1)
        img1.putpixel((x1+1,y1),p2)
        img1.putpixel((x1,y1+1),p3)
        img1.putpixel((x1+1,y1+1),p4)

        count+=1
        
img1.save("encrypted_permutation.bmp")           
img2= img1.copy()
#===============================================================================


#===============================================================================
# Decryption
count=0

for y in range(0,512,2):
    for x in range(0,512,2):

        e= order_list[count]

        y1 = (e - 1) // 256
        x1 = (e - 1) % 256
        y1*=2
        x1*=2

        p1 = img1.getpixel((x1,y1))
        p2 = img1.getpixel((x1+1,y1))
        p3 = img1.getpixel((x1,y1+1))
        p4 = img1.getpixel((x1+1,y1+1))
        
        img2.putpixel((x,y),p1)
        img2.putpixel((x+1,y),p2)
        img2.putpixel((x,y+1),p3)
        img2.putpixel((x+1,y+1),p4)

        count+=1

img2.save("decrypted.bmp")    
#===============================================================================

# Checking if the original image and decrypted image are the same.
psnr_value = psnr(img,img2)

if psnr_value == float('inf'):
    print("PSNR value is infinite (images are identical).")
else:
    print(f"PSNR value: {psnr_value}")