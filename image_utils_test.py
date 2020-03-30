from image_utils import *
if __name__ == "__main__":
    file = input("image file> ")
    image = read_ppm(file)

    # Test writing it unmodified
    save_ppm("unmodified.ppm", image)

    # 颜色翻转小测试，判断正确读入ppm文件
    width, height = get_width_height(image)
    for x in range(width):
        for y in range(height):
            r, g, b = image[x][y]
            image[x][y] = (g, b, r)
    save_ppm("modified.ppm", image)


