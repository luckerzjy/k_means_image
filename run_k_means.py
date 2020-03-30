import k_means
import image_utils

def runsys(fi, k, fo):
    # print("Please enter the picture path: ")
    file = fi
    image = image_utils.read_ppm(file)
    # print("Please enter the value k: ")
    k = int(k)
    # print("Please enter the picture save path: ")
    file_out = fo
    k_means.process_img(image, k,file_out)
    return True
