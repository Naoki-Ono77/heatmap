import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Times New RomanとArialフォントを指定
times_new_roman = FontProperties(family='Times New Roman', style='italic', size=30)
arial_font = FontProperties(family='Arial', size=30)

def load_data(file_name):
    """指定したTXTファイルからデータを読み込み、yとzの値を返す"""
    y = []
    z = []
    with open(file_name, 'r') as file:
        for line in file:
            values = line.split()  # スペースで分割
            y.append(float(values[0]))  # 一列目をyに
            z.append(float(values[1]))  # 二列目をzに
    return np.array(y), np.array(z)

# データファイルの指定
data_files = {
    1.5: '1.5.txt',
    1.25: '1.25.txt',
    1: '1.txt',  # x=1のデータ
    0.75: '0.75.txt',
    0.5: '0.5.txt',  # x=0.5のデータ
    0.25: '0.25.txt',  # x=0.25のデータ
    0: '0.txt'
}

# yとzのデータを読み込み
y_data = []
z_data = []
x_values = list(data_files.keys())

for x in x_values:
    y, z = load_data(data_files[x])
    y_data.append(y)
    z_data.append(z)

# ヒートマップ用のグリッドを作成
Y, X = np.meshgrid(y_data[0], x_values)  # yの値とxの値をグリッド化
Z = np.array([z_data[0], z_data[1], z_data[2], z_data[3], z_data[4], z_data[5], z_data[6]])  # zの値を行列に変換

# ヒートマップをプロット
plt.figure(figsize=(8, 6))

contour_levels = 500  # 色分けを設定
vmin, vmax = 0, 12  # カラーバーの最小値と最大値を設定
levels = np.linspace(vmin, vmax, contour_levels)  # 等間隔でレベルを設定
heatmap = plt.contourf(X, Y, Z, levels=levels, cmap='viridis', vmin=vmin, vmax=vmax)  # ヒートマップの描画
cbar = plt.colorbar(heatmap)  # カラーバーの表示

# カラーバーラベルを右肩に2をつけた形式で設定
# カラーバーラベルを部分的にフォント指定
cbar.set_label(r'$\mathit{K}^{\mathrm{2}} \, (\mathrm{\%})$', fontsize=30, fontproperties=times_new_roman)

cbar.set_ticks(np.linspace(vmin, vmax, 7))  # 0から12まで等間隔に7個の目盛りを設定

# カラーバーのメモリの数字の大きさを変更
cbar.ax.tick_params(labelsize=30)  # メモリの数字を30に設定

# 縦軸を30°刻みに設定
y_ticks = np.arange(0, 91, 30)  # 0°から90°まで30°刻み
plt.yticks(y_ticks, labels=[f"{angle}°" for angle in y_ticks], fontproperties=arial_font)

# ラベルとタイトルを設定
plt.xlabel("h/\u03bb", fontsize=30, fontproperties=times_new_roman)
plt.ylabel("c-Axis tilt angle (deg.)", fontsize=30, fontproperties=arial_font)

# 軸目盛りや目盛りラベルのフォントサイズを変更
plt.tick_params(axis='both', which='major', labelsize=30, pad=15)  # 目盛りのフォントサイズを設定

# グラフのレイアウトを自動調整
plt.tight_layout()

plt.grid(False)
plt.show()
