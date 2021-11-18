# How to run the program

1. Install required packages: run `pip install -r requirements.txt`
2. To run, `python3 imda_captcha.py` and enter im_path and save_path when prompted

For example,
```
> python3 imda_captcha.py
> Enter im_path: ./input/input100.jpg # path to image to decode
> Enter save_path: ./test.txt # path to save decoded text
```

# Derivation of noise threshold

The program uses threshold value to determine if a pixel is noise, or part of the captcha text. To determine this threshold value, we analysed one image and counted the number of pixels of each shade of grey. We observed that there were no pixels with RGB values between RGB (36,36,36) and RGB (159,159,159). This suggests that we can use a threshold value of 40 to separate the blacks in the captcha text vs the greys/whites in the noise/background.