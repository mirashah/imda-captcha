from PIL import Image
import numpy as np

class Captcha(object):
    def __init__(self):
        self.noise_threshold = 40 # see README for derivation of threshold value
        self.characters = {}
        pass

    def __call__(self, im_path, save_path):
        """
        Algo for inference
        args:
            im_path: .jpg image path to load and to infer
            save_path: output file path to save the one-line outcome
        """
        
        self.train_model()
        output_string = self.decode_captcha(im_path)
        
        with open(save_path, "w+") as f:
            f.write(output_string)
        
        return
    
    def train_model(self):
        """
        Build dictionary of labelled characters
        """
        for filenum in range(25):
            try: # in case file does not exist
                img = self.load_img("./input/input" + str(filenum).zfill(2) + ".jpg")
                with open("./output/output" + str(filenum).zfill(2) + ".txt") as f:
                    label = f.readline()
                split_img = self.split_img(img)
                for i in range(5):
                    if label[i] in self.characters.keys():
                        continue
                        
                    self.characters[label[i]] = split_img[i]
            except:
                pass
        return
    
    def decode_captcha(self, im_path):
        """
        Returns decoded captcha
        """
        result = ""
        test_img = self.load_img(im_path)
        split_img = self.split_img(test_img)
        # Iterate over each character in captcha and compare with trained model
        for i in range(5):
            for k, v in self.characters.items():
                if split_img[i] == v:
                    result += k
                    continue
        return result
    
    def load_img(self, im_path):
        """
        Strips noise from Captcha and stores simplified image in img_array
        """
        img = Image.open(im_path)
        img_array = ["#" if x[0] < self.noise_threshold else " " for x in list(img.getdata())]
        img_array = np.reshape(img_array, (30, 60)).transpose().tolist()
        return img_array
    
    def split_img(self, captcha):
        """
        Splits captcha into individual characters
        """
        blank_col = [" "] * 30
        char = []
        split_captcha = []
        # Read captcha by column
        for col in captcha:
            if col == blank_col and len(char) == 0:
                # contiguous white space
                continue
            elif col == blank_col and len(char) != 0:
                # end of letter
                split_captcha.append(char)
                char = []
            else:
                # part of letter
                char.append(col)
        return split_captcha

x = Captcha()
im_path = input("Enter im_path: ")
save_path = input("Enter save_path: ")
x(im_path, save_path)