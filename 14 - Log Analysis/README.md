# C-14: Log Analysis
> We've hidden a FLAG somewhere in the logs. Find out if you can. Good Luck - Red team
> [[instructions.docx]]

The document is exclusively made up of images. Decoding the base64 at the end of the file gives two seemingly real flags, but when submitted are incorrect.

From NZCSCs gone by we know that DOCX files cropped in-app store the whole image ready to be uncropped. We can do so on the image containing 'Among others we find GET...' and '/test/path/challenge.txt...' to find information on another file.

![[uncropped.png]]

Decoding this base64 gives `FLAG[B89F293252A8FFCD]`.