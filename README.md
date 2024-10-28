This repo is for decoding a file having gibberish text which was actually 
encoded in base64 which wich decoded into binary file as an image.
On performing zsteg on the image, that the diagonal pixels hold the flag we are looking for
So we then write a python script to make a new image using the diagonal elements only which on performing zsteg will reveal the flag!!
We are supposed to use LSB(least significant bit) related logic but this is what I came up with(*Awkward smiles*).
Do try to check your own methods.
