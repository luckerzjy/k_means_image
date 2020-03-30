import operator
from math import sqrt
from random import random

from image_utils import get_width_height, random_color, save_ppm


def init_guess_mean_list(k):
    """
    a function to create the random initial guess means list
    :param the number of colors
    :return an initial color list

    """
    m_list = []
    for i in range(k):
        m_list.append(random_color())

    return m_list


def compute_dis(c1,c2):
    """
    a function to compute the "distance" between two colors (treat the colors as 3d points and use euclidean distance)
    :param two color tuple
    :return distance between them
    """
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    dis = sqrt((r1-r2)**2+(g1-g2)**2+(b1-b2)**2)
    return dis


def compute_sum(c):
    """
    compute r g b sum
    """
    r_s, g_s, b_s = 0, 0, 0
    for ele in c:
        r_s += ele[0]
        g_s += ele[1]
        b_s += ele[2]

    return (r_s,g_s,b_s)


def divide(n,m):
    """
    divide operation
    """
    return n // m


def compute_avg_color(c):
    """
    a function that computes the average color of a list of colors.
    """
    r_s,g_s,b_s = compute_sum(c)
    cnt = len(c)
    r_e, g_e, b_e = 0, 0, 0
    if cnt > 0:
        r_e = divide(r_s,cnt)
        g_e = divide(g_s,cnt)
        b_e = divide(b_s,cnt)

    return (r_e,g_e,b_e)


def update_assg(image,m_list,assg):
    """
    a function for computing/updating the assignments given the image and means
    :return a new list represents each point's closest color of the k colors
    """
    w, h = get_width_height(image)
    l = len(m_list)

    for i in range(h):
        for j in range(w):
            dis = []
            assg[j][i] = cal_min_dis(image[j][i], dis, m_list)

    return assg


def cal_min_dis(point, dis, m_list):
    """
    calculate the minimum distance
    :param one point and a point list
    :return the minimum index of the point in list
    """
    l = len(m_list)
    for i in range(l):
        dis.append(compute_dis(point, m_list[i]))

    min_index, min_number = min(enumerate(dis), key=operator.itemgetter(1))

    return min_index


def update_mean(image,k,assg_l):
    """
    a function for updating the means list given image,recompute the colors for k_means
    :param the image and the number of colors and the assg_l
    :return a new average color list for k_means
    """
    w, h = get_width_height(image)
    m_list = []
    for i in range(k):
        c_list = []
        for row in range(h):
            for col in range(w):
                if assg_l[col][row] == i :
                    c_list.append(image[col][row])

        m_list.append( compute_avg_color(c_list))

    return m_list


def is_same(assg1,assg2):
    """
    whether is true
    """
    if assg1 == assg2:
        return True
    else:
        return False


def update_mean_assg(assignment, image, k):
    """
    update means and assignment
    """
    mean_list = update_mean(image, k, assignment)
    assignment = update_assg(image, mean_list, assignment)
    return (assignment, mean_list)


def k_means(image, k):
    """
    k_means(image, k) an image which performs a complete k means computation.
    """
    mean_list = init_guess_mean_list(k)  # init
    w,h = get_width_height(image)
    assignment = [[0] * h for i in range(w)]
    assignment = update_assg(image, mean_list, assignment)
    assignment_backup = []
    while 1:
        if is_same(assignment_backup, assignment):  # complete
            break
        assignment_backup = assignment
        assignment,mean_list = update_mean_assg(assignment, image, k)

    return mean_list, assignment


def label(image, assg,m_list):
    """
    rewrite a new image after k_means operation
    """
    w, h = get_width_height(image)
    for row in range(h):
        for col in range(w):
            image[col][row] = m_list[assg[col][row]]

    return image


def process_img(image,k,file_out):
    """
    process
    """
    m_list, assg = k_means(image,k)
    image = label(image,assg,m_list)
    save_ppm(file_out,image)
