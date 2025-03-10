import numpy as np
from PIL import Image

#flipping image
@np.vectorize
def flip_image(img):
    with Image.open(img) as image:
        img_arr = np.array(image)
    flipped_ud_arr = img_arr[::-1]
    flipped_ud_img = Image.fromarray(flipped_ud_arr, mode="RGB")
    flipped_ud_img.save("Python_Homework/lesson-14/homework/images/updown_flipped.jpg")
    flipped_rl_arr = img_arr[:, ::-1, :]
    flipped_rl_img = Image.fromarray(flipped_rl_arr, mode="RGB")
    flipped_rl_img.save("Python_Homework/lesson-14/homework/images/rightleft_flipped.jpg")

# flip_image("Python_Homework/lesson-14/homework/images/birds.jpg")

#random noise
def make_noisy_image(img):
    with Image.open("Python_Homework/lesson-14/homework/images/birds.jpg") as image:
        image_arr = np.array(image, dtype=np.float32)
    mean = 0
    stddev = 10
    noise_arr = np.random.normal(mean, stddev, image_arr.shape)
    noisy_image_arr = np.clip(image_arr + noise_arr, 0, 255).astype(np.uint8)
    noisy_image = Image.fromarray(noisy_image_arr)
    noisy_image.save("Python_Homework/lesson-14/homework/images/noisy_image.jpg")
#make_noisy_image("Python_Homework/lesson-14/homework/images/birds.jpg")

# brighten channels
def brighten_channels(img):
    with Image.open("Python_Homework/lesson-14/homework/images/birds.jpg") as image:
        image_arr = np.array(image, dtype=np.float32)
    image_arr[:, :, 0] = np.clip(image_arr[:, :, 0]+40, 0, 255)
    brighter_img_arr = image_arr.astype(np.uint8)
    brighter_img = Image.fromarray(brighter_img_arr, mode="RGB")
    brighter_img.save("Python_Homework/lesson-14/homework/images/brighter_image.jpg")
#brighten_channels("Python_Homework/lesson-14/homework/images/brighter_image.jpg")

# mask
def mask_make_in_image(img):
    with Image.open(img) as image:
        image_arr = np.array(image, dtype=np.uint8)
    height, width, _ = image_arr.shape 
    c1 = int(height / 2 - 100)
    c2 = int(height / 2 + 100)
    r1 = int(width / 2 - 100)
    r2 = int(width / 2 + 100)
    image_arr[c1:c2, r1:r2, :] = 0
    mask_image = Image.fromarray(image_arr.astype(np.uint8), mode="RGB")
    mask_image.save("Python_Homework/lesson-14/homework/images/mask_image.jpg")
mask_make_in_image("Python_Homework/lesson-14/homework/images/birds.jpg")
