import shutil
import cv2
import os


'''
图片命名：“025-95_113-154&383_386&473-386&473_177&454_154&383_363&402-0_0_22_27_27_33_16-37-15.jpg”
1. 025：车牌区域占整个画面的比例；
2. 95_113： 车牌水平和垂直角度, 水平95°, 竖直113°
3. 154&383_386&473：标注框左上、右下坐标，左上(154, 383), 右下(386, 473)
4. 86&473_177&454_154&383_363&402：标注框四个角点坐标，顺序为右下、左下、左上、右上
5. 0_0_22_27_27_33_16：车牌号码映射关系如下: 第一个0为省份 对应省份字典provinces中的’皖’,；第二个0是该车所在地的地市一级代码，对应地市一级代码字典alphabets的’A’；后5位为字母和文字, 查看车牌号ads字典，如22为Y，27为3，33为9，16为S，最终车牌号码为皖AY339S

省份：[“皖”, “沪”, “津”, “渝”, “冀”, “晋”, “蒙”, “辽”, “吉”, “黑”, “苏”, “浙”, “京”, “闽”, “赣”,
“鲁”, “豫”, “鄂”, “湘”, “粤”, “桂”, “琼”, “川”, “贵”, “云”, “藏”, “陕”, “甘”, “青”, “宁”,
“新”]
地市：[‘A’, ‘B’, ‘C’, ‘D’, ‘E’, ‘F’, ‘G’, ‘H’, ‘J’, ‘K’, ‘L’, ‘M’, ‘N’, ‘P’, ‘Q’,
‘R’, ‘S’, ‘T’, ‘U’, ‘V’, ‘W’,‘X’, ‘Y’, ‘Z’]
车牌字典：[‘A’, ‘B’, ‘C’, ‘D’, ‘E’, ‘F’, ‘G’, ‘H’, ‘J’, ‘K’, ‘L’, ‘M’, ‘N’, ‘P’,
‘Q’, ‘R’, ‘S’, ‘T’, ‘U’, ‘V’, ‘W’, ‘X’,‘Y’, ‘Z’, ‘0’, ‘1’, ‘2’, ‘3’, ‘4’, ‘5’,
‘6’, ‘7’, ‘8’, ‘9’]
'''

def txt_translate(path, txt_path):
    print(path)
    print(txt_path)
    for filename in os.listdir(path):
        # print(filename)
        list1 = filename.split("-", 3)  # 第一次分割，以减号'-'做分割
        subname = list1[2]
        list2 = filename.split(".", 1)
        subname1 = list2[1]
        if subname1 != 'jpg':
            continue
        lt, rb = subname.split("_", 1)  # 第二次分割，以下划线'_'做分割
        lx, ly = lt.split("&", 1)
        rx, ry = rb.split("&", 1)
        width = int(rx) - int(lx)
        height = int(ry) - int(ly)  # bounding box的宽和高
        cx = float(lx) + width / 2
        cy = float(ly) + height / 2  # bounding box中心点
        img = cv2.imread(path + filename)
        if img is None:  # 自动删除失效图片（下载过程有的图片会存在无法读取的情况）
            print(path + filename)
            os.remove(path + filename)
            continue
        width = width / img.shape[1]
        height = height / img.shape[0]
        cx = cx / img.shape[1]
        cy = cy / img.shape[0]
        txtname = filename.split(".", 1)
        txtfile = txt_path + txtname[0] + ".txt"
        # 绿牌是第0类，蓝牌是第1类
        if not os.path.exists(txt_path):
            os.makedirs(txt_path)
        with open(txtfile, "w") as f:
            f.write(str(0) + " " + str(cx) + " " + str(cy) + " " + str(width) + " " + str(height))

def divide(input_path):
    x = 0
    y = 0
    testDir = os.path.join(input_path, "..","test")
    trainDir = os.path.join(input_path, "..","train")
    valDir = os.path.join(input_path, "..","val")
    for filename in os.listdir(input_path):
        source_file = os.path.join(input_path, filename)
        if y>4:
            y = 0
            destination_file = os.path.join(valDir, filename)
            if os.path.isfile(source_file):
                # 复制文件
                shutil.copy(source_file, destination_file)
        if x == 0:
            x = x+1
            y = y+1
            destination_file = os.path.join(trainDir, filename)
            if os.path.isfile(source_file):
                # 复制文件
                shutil.copy(source_file, destination_file)
        else:
            x = 0
            y = y+1
            destination_file = os.path.join(testDir, filename)
            if os.path.isfile(source_file):
                # 复制文件
                shutil.copy(source_file, destination_file)


def delete(input_path):
    for filename in os.listdir(input_path):
        list = filename.split(".")
        subname = list[-1]
        if subname == 'Identifier':
            os.remove(os.path.join(input_path, filename))

if __name__ == '__main__':
    # trainDir = r"CCPD2020/ccpd_green/train/"
    # validDir = r"CCPD2020/ccpd_green/val/"
    # testDir = r"CCPD2020/ccpd_green/test/"
    # # det txt存储地址
    # train_txt_path = r"CCPD2020/ccpd_green/train_labels/"
    # val_txt_path = r"CCPD2020/ccpd_green/val_labels/"
    # test_txt_path = r"CCPD2020/ccpd_green/test_labels/"
    # txt_translate(trainDir, train_txt_path)
    # txt_translate(validDir, val_txt_path)
    # txt_translate(testDir, test_txt_path)
    #divide("./")
    delete("datasets/PlateData/images/train")
    delete("datasets/PlateData/images/test")
    delete("datasets/PlateData/images/val")
    delete("datasets/PlateData/lables/train")
    delete("datasets/PlateData/lables/test")
    delete("datasets/PlateData/lables/val")
