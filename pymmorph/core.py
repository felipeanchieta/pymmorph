import cv2
import numpy as np
import PIL
from matplotlib import pyplot as plt


CROSS=np.matrix('0 1 0; 1 1 1; 0 1 0', np.uint8)

def mmaddm(f1, f2):
    kmax = 1.0
    res = np.matrix(f1.shape)

    print(res.shape)

    it = np.nditer([f1, f2, res])
    for el in it:
        el[3] = min(kmax, el[0] + el[1])

    print(res)
    return []


def mmareaclose(f, a, Bc):
    pass


def mmareaopen(f, a, Bc):
    pass


def mmasf(f, seq='OC', b=CROSS, n=1):
    """Alternating Sequential Filtering."""
    f_ = f.copy()
    for op in seq:
        if op == 'O' or op == 'o':
            f_ = mmopen(f_, b)
        elif op == 'C' or op == 'c':
            f_ = mmclose(f_, b)
        else:
            pass

    return f_


def mmasfrec(f, seq, b, bc, n):
    pass


def mmbinary(f, k):
    """Convert a gray-scale image into a binary image""" 
    return cv2.threshold(f, k, 255, cv2.THRESH_BINARY)[1] 
    

def mmblob(fr, measurement, option): 
    pass


def mmbshow(f1, f2, f3, factor):
    pass


def mmcbisector(f, B, n):
    pass


def mmcdil(f, g, b, n):
    pass


def mmcenter(f, b):
    pass


def mmcero(f, g, b, n):
    pass


def mmclohole(f, Bc):
    pass


def mmclose(f, b=CROSS):
    """Morphological closing."""
    return cv2.morphologyEx(f, cv2.MORPH_CLOSE, b)


def mmcloserec(f, bdil, bc):
    pass


def mmcloserecth(f, bdil, bc):
    pass


def mmcloseth(f, b):
    pass


def mmcmp(f1, oper, f2, oper1, f3):
    pass


def mmconcat(dim, x1, x2, x3, x4):
    pass


def mmcthick():
    pass


def mmcthin():
    pass


def mmcwatershed():
    pass


def mmdairport():
    pass


def mmdarea():
    pass


def mmdasp():
    pass


def mmdatatype():
    pass


def mmdbeef():
    pass


def mmdblob():
    pass


def mmdbrain():
    pass


def mmdcalc():
    pass


def mmdcells():
    pass


def mmdchickparts():
    pass


def mmdconcrete():
    pass


def mmdcookies():
    pass


def mmdcornea():
    pass


def mmdfabric():
    pass


def mmdfila():
    pass


def mmdflatzone():
    pass


def mmdflow():
    pass


def mmdgear():
    pass


def mmdholecenter():
    pass


def mmdil(f, b=CROSS):
    """Dilate an image by a structuring element."""
    return cv2.dilate(f, b) 


def mmdist():
    pass


def mmdlabeltext():
    pass


def mmdleaf():
    pass


def mmdlith():
    pass


def mmdpcb():
    pass


def mmdpieces():
    pass


def mmdpotatoes():
    pass


def mmdraw():
    pass


def mmdrawv():
    pass


def mmdrobotop():
    pass


def mmdruler():
    pass


def mmdsoil():
    pass


def mmdtshow():
    pass


def mmdvlpl():
    pass


def mmedgeoff():
    pass


def mmendpoints():
    pass


def mmero(f, b=CROSS):
    """Erode an image by a structuring element."""
    return cv2.erode(f, b) 


def mmflood():
    pass


def mmfractal():
    pass


def mmframe():
    last_line = f.shape[0] - 1
    last_column = f.shape[1] - 1

    return [
        [k1 if i == 0 or i == last_line or j == 0 or j == last_column else k2 for j in range(f.shape[1])]
        for i in range(f.shape[0])
        ]


def mmfreedom():
    pass


def mmgdist():
    pass


def mmglblshow():
    pass


def mmgradm():
    pass


def mmgrain():
    pass


def mmgray(f):
    """Convert a binary image into a gray-scale image."""
    return [255 if item == 1 else 0 for item in f]


def mmgshow():
    pass


def mmhbasin():
    pass


def mmhdome():
    pass


def mmhistogram():
    pass


def mmhmax():
    pass


def mmhmin():
    pass


def mmhomothick():
    pass


def mmhomothin():
    pass


def mmimg2se():
    pass


def mminfcanon():
    pass


def mminfgen():
    pass


def mminfrec():
    pass


def mminpos():
    pass


def mminterot():
    pass


def mmintersec():
    pass


def mmintershow():
    pass


def mmis():
    pass


def mmisbinary():
    pass


def mmisequal():
    pass


def mmislesseq():
    pass


def mmiwatershed():
    pass


def mmlabel():
    pass


def mmlabelflat():
    pass


def mmlblshow():
    pass


def mmlimits():
    pass


def mmmaxaopen():
    pass


def mmmaxaopenmt():
    pass


def mmmaxaopenth():
    pass


def mmmaxaopenthmt():
    pass


def mmmaxgetchildren():
    pass


def mmmaxgetcount():
    pass


def mmmaxgetimage():
    pass


def mmmaxgetindex():
    pass


def mmmaxgetnodes():
    pass


def mmmaxgetxml():
    pass


def mmmaxinfrec():
    pass


def mmmaxopenrec():
    pass


def mmmaxpropagate():
    pass


def mmmaxregmax():
    pass


def mmmaxsubimage():
    pass


def mmmaxsubtree():
    pass


def mmmaxthreshold():
    pass


def mmmaxthresholdlabelcount():
    pass


def mmmaxtree():
    pass


def mmneg(f):
    if f.dtype == 'uint8':
        k = 255
    else:
        k = 65535

    return [k - el for el in f]


def mmopen(f, b=CROSS):
    """Morphological opening."""
    return cv2.morphologyEx(f, cv2.MORPH_OPEN, b) 


def mmopenrec():
    pass


def mmopenrecth():
    pass


def mmopenth(f, b=CROSS):
    return cv2.morphologyEx(f, cv2.MORPH_TOPHAT, b)


def mmopentransf():
    pass


def mmpatspec():
    pass


def mmreadgray(filename):
    """Read an image from a commercial file format and stores it as a gray-scale image."""
    return cv2.imread(filename, cv2.IMREAD_GRAYSCALE)


def mmregmax():
    pass


def mmregmin():
    pass


def mmse2hmt():
    pass


def mmse2interval():
    pass


def mmsebox():
    pass


def mmsecross():
    pass


def mmsedil():
    pass


def mmsedisk():
    pass


def mmseline():
    pass


def mmsereflect():
    pass


def mmserot():
    pass


def mmseshow():
    pass


def mmsesum():
    pass


def mmsetrans():
    pass


def mmseunion():
    pass


def mmshow(f):
    plt.imshow(f, 'gray')
    plt.show()


def mmskelm():
    pass


def mmskelmrec():
    pass


def mmskiz():
    pass


def mmstats():
    pass


def mmsubm():
    pass


def mmsupcanon():
    pass


def mmsupgen():
    pass


def mmsuprec():
    pass


def mmsurf():
    pass


def mmswatershed():
    pass


def mmsymdif():
    pass


def mmtext():
    pass


def mmthick():
    pass


def mmthin():
    pass


def mmthreshad(f, f1, f2):
    pass


def mmtoggle():
    pass


def mmunion():
    pass


def mmvbasin():
    pass


def mmvdome():
    pass


def mmversion():
    """SDC Morphology Toolbox version."""
    return "SDC Morphology Toolbox for Python v0.1" 


def mmvmax():
    pass


def mmvmin():
    pass


def mmwatershed():
    pass


def mmwrite(f, filename):
    """Write a gray-scale image into a commercial file format."""
    cv2.imwrite(filename, f)

