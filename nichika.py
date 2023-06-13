from PIL import Image
import numpy as np

def binarize(ImgObj,thres):
    """画素値がthres以上を255,それ以外を0にする"""
    tmpimg=ImgObj.convert("L")
    arr=np.array(tmpimg)
    arr=(arr>=thres)*255
    arr=arr.astype(np.uint8)
    return Image.fromarray(arr)

thres=int(input("閾値:"))
nichika=Image.open("nnksnck.jpg")
binchika=binarize(nichika,thres)
binchika.save(f"nnks2ck_{thres}.jpg")
# binchika.show()
