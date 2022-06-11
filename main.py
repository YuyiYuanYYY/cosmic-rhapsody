# 导入所需的库
import matplotlib.pyplot as plt
import numpy as np
from numpy import array
# astropy是专门的天文学python库
from astropy.io import fits
import csv
import pandas as pd
import thinkdsp as dsp
import os


# 读取fits单个数据
fileitem = fits.open("spec-55859-F5902_sp01-013.fits.gz")
# 提取元素
X = fileitem[0].data[2]
Y = fileitem[0].data[0]
data = Y.copy()
data = np.array(data, dtype='float64')
print("打印数据类型")
print(data.shape)
print("打印原始数据")
print(data)

# 读取fits多个数据
# path = 'M/'
# files = os.listdir(path)
# train_csv = list(filter(lambda x:(x[-8:] == '.fits.gz'), files))
# data = []
# for fileitem in train_csv:
#     tmp = fits.open(path + fileitem)
#     # 提取元素
#     X = tmp[0].data[2]
#     Y = tmp[0].data[0]
#     data = np.concatenate((data, Y), axis=0)
# data = np.array(data, dtype='float64')
# print("打印数据类型")
# print(data.shape)
# print("打印原始数据")
# print(data)

print("打印数据的最值")
print(max(data), min(data))
# 除以最大最小值之差再乘以1000
data_fix = (data/(max(data) - min(data)))*1000
print(data_fix)

# 绘制图像
plt.plot(data)
plt.show()
plt.plot(data)
plt.plot(data_fix)
plt.show()

# 更改数据
data = data_fix.copy()

# 复刻数据data进行操作
item = data.shape[0] - 1
midpoint = data.copy()
for i in range(item):
    midpoint[i] = (data[i] + data[i+1]) / 2
print("打印数据的中点值")
print(midpoint)
plt.plot(data_fix)
plt.plot(midpoint, 'r')
plt.show()

# 将中点形成一条直线
for i in range(item):
    data[i:] = data[i:] - midpoint[i]
    midpoint[i:] = midpoint[i:] - midpoint[i]
print("打印调整中点后的数据")
print(data)
print("打印此时的中点值（应该均为0）")
print(midpoint)
plt.plot(data)
plt.plot(midpoint)
plt.show()

# 用于重复数据
# e = [data, data, data, data, data, data, data, data, data, data]
# e = [e, e, e, e, e, e, e, e, e, e, e, e]
# e = array(e)
# data = e.flatten()
# data = np.array(data, dtype='float64')

data_clean = data[data < 100]
data_clean = data_clean[data_clean > -100]
print("清洗后的数据")
print(data_clean)
data_fixed = dsp.normalize(data_clean, amp=1.0)
print("归一化处理后的数据")
print(data_fixed)
drange = (data_fixed.min(), data_fixed.max())
print("打印此时数据的最大值和最小值")
print(drange)

# 定义采样率
fr = 1500
wave = dsp.Wave(ys=data_fixed, framerate=fr)
wave.plot()
plt.show()
# 生成音频并写入文件
wave.make_audio()
wave.write(filename="test.wav")


spectrum = wave.make_spectrum()
# 高通滤波
# spectrum.high_pass(cutoff=10, factor=0.01)
spectrum.plot()
plt.show()

violin_wave = dsp.read_wave("violin.wav")
print("打印小提琴的声音数据")
print(violin_wave.ys.shape)
violin_wave.plot()
plt.show()
spectrum = violin_wave.make_spectrum()
spectrum.plot()
plt.show()