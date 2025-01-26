# Block Permutation Tool
## Description:
Block Permutation Tool is designed to encrypt images by rearranging image blocks using a pseudo-random permutation key. It is particularly useful for researchers working on Reversible Data Hiding in Encrypted Images (RDHEI).

## Key Features
* Image size: 512x512 grayscale image
* Block size: 2x2 pixels
* Sender: Shuffle all 2x2 blocks in the image using an encryption key.
* Receiver: Use the same encryption key to reverse the permutation and recover the original image.

This tool divides the image into 65536 blocks and applies a pseudo-random permutation based on the provided encryption key to generate an encrypted image. The receiver can then use the same key to decrypt and restore the image.

## Usage 

* Change the image path in the script to the image you want to encrypt.
* Run the code.
* Obtain the encrypted or decrypted image.

## Example
`python block_permutation.py`

## Note
* Ensure that the input image is in 512x512 grayscale format.
* The same encryption key must be used for both encryption and decryption.
