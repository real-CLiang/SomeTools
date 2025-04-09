import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_songti = FontProperties(fname='C:/Windows/Fonts/simsun.ttc')  # Windows 宋体路径
# 解决负号显示为方块的问题
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False

# 初始化图形
fig, ax = plt.subplots()
ylim = 0.6
ax.set_xlim(0, 5000)  # 修改 x 轴范围以匹配图片
ax.set_ylim(0, ylim)
ax.set_xlabel("迭代次数", fontproperties=font_songti)
ax.set_ylabel("适\n应\n度", fontproperties=font_songti, rotation=0, labelpad=10)  # rotation=0 让文字水平

# 设置 x 轴主要刻度线和次要刻度线
major_ticks_x = list(range(0, 5001, 1000))  # 主要刻度线位置
minor_ticks_x = list(range(500, 5000, 1000))  # 次要刻度线位置
ax.set_xticks(major_ticks_x)  # 设置主要刻度线
ax.set_xticks(minor_ticks_x, minor=True)  # 设置次要刻度线
ax.tick_params(axis='x', which='major', length=4, width=1, direction='in')  # 主要刻度线
ax.tick_params(axis='x', which='minor', length=2, width=1, direction='in')  # 次要刻度线

# 设置 y 轴主要刻度线和次要刻度线
major_ticks_y = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]  # 主要刻度线位置
minor_ticks_y = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55]  # 次要刻度线位置
ax.set_yticks(major_ticks_y)  # 设置主要刻度线
ax.set_yticks(minor_ticks_y, minor=True)  # 设置次要刻度线
ax.tick_params(axis='y', which='major', length=4, width=1, direction='in')  # 主要刻度线
ax.tick_params(axis='y', which='minor', length=2, width=1, direction='in')  # 次要刻度线

# 去掉右边框线和上方框线
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# 定义曲线点存储
curve_data = {
    'GP': {'points': [], 'color': 'b', 'marker': 'o', 'label': 'GP'},
    'PGP': {'points': [], 'color': 'g', 'marker': 's', 'label': 'PGP'},
    'SD-HTPGP': {'points': [], 'color': 'red', 'marker': '^', 'label': 'SD-HTPGP'}
}

# 当前选择的曲线
current_curve = 'GP'

# 鼠标点击事件
def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        # 添加点到当前选中的曲线
        curve_data[current_curve]['points'].append((event.xdata, event.ydata))
        
        # 清除之前的绘制并重新绘制所有曲线
        ax.clear()
        ax.set_xlim(0, 5000)  # 修改 x 轴范围以匹配图片
        ax.set_ylim(0, ylim)
        ax.set_xlabel("迭代次数", fontproperties=font_songti)
        ax.set_ylabel("适\n应\n度", fontproperties=font_songti, rotation=0, labelpad=10)  # rotation=0 让文字水平
        
        # 设置 x 轴主要和次要刻度线
        ax.set_xticks(major_ticks_x)  # 设置主要刻度线
        ax.set_xticks(minor_ticks_x, minor=True)  # 设置次要刻度线
        ax.tick_params(axis='x', which='major', length=4, width=1, direction='in')  # 主要刻度线
        ax.tick_params(axis='x', which='minor', length=2, width=1, direction='in')  # 次要刻度线
        
        # 设置 y 轴主要和次要刻度线
        ax.set_yticks(major_ticks_y)  # 设置主要刻度线
        ax.set_yticks(minor_ticks_y, minor=True)  # 设置次要刻度线
        ax.tick_params(axis='y', which='major', length=4, width=1, direction='in')  # 主要刻度线
        ax.tick_params(axis='y', which='minor', length=2, width=1, direction='in')  # 次要刻度线
        
        # 去掉右边框线和上方框线
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        
        # 绘制所有曲线
        for curve in curve_data.values():
            points = curve['points']
            if points:
                x_vals = [p[0] for p in points]
                y_vals = [p[1] for p in points]
                ax.plot(x_vals, y_vals, marker=curve['marker'], color=curve['color'], label=curve['label'])
        
        # 添加图例
        ax.legend(loc='upper right', fontsize=10, frameon=False)  # 设置图例位置和样式
        fig.canvas.draw()

# 键盘事件：切换当前曲线
def onkeypress(event):
    global current_curve
    if event.key == '1':
        current_curve = 'GP'
        print("Switched to GP")
    elif event.key == '2':
        current_curve = 'PGP'
        print("Switched to PGP")
    elif event.key == '3':
        current_curve = 'SD-HTPGP'
        print("Switched to SD-HTPGP")
    elif  event.key == 'z':
        undo_last_point()
    elif event.key == 's':  # 按键 's' 保存图表
        save_plot()

def undo_last_point():
    if curve_data[current_curve]['points']:
        removed_point = curve_data[current_curve]['points'].pop()  # 删除最后一个点
        print(f"Removed point: {removed_point} from {current_curve}")
        redraw()
    else:
        print(f"No points to undo for {current_curve}")
# 重绘图形
def redraw():
    ax.clear()
    ax.set_xlim(0, 5000)  # 修改 x 轴范围以匹配图片
    ax.set_ylim(0, ylim)
    ax.set_xlabel("迭代次数", fontproperties=font_songti)
    ax.set_ylabel("适\n应\n度", fontproperties=font_songti, rotation=0, labelpad=10)  # rotation=0 让文字水平
    
    # 设置 x 和 y 轴刻度线
    ax.set_xticks(major_ticks_x)  # 设置主要刻度线
    ax.set_xticks(minor_ticks_x, minor=True)  # 设置次要刻度线
    ax.tick_params(axis='x', which='major', length=4, width=1, direction='in')  # 主要刻度线
    ax.tick_params(axis='x', which='minor', length=2, width=1, direction='in')  # 次要刻度线
    ax.set_yticks(major_ticks_y)  # 设置主要刻度线
    ax.set_yticks(minor_ticks_y, minor=True)  # 设置次要刻度线
    ax.tick_params(axis='y', which='major', length=4, width=1, direction='in')  # 主要刻度线
    ax.tick_params(axis='y', which='minor', length=2, width=1, direction='in')  # 次要刻度线
    
    # 去掉右边框线和上方框线
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    # 绘制所有曲线
    for curve in curve_data.values():
        points = curve['points']
        if points:
            x_vals = [p[0] for p in points]
            y_vals = [p[1] for p in points]
            ax.plot(x_vals, y_vals, marker=curve['marker'], color=curve['color'], label=curve['label'])
    
    # 添加图例
    ax.legend(loc='upper right', fontsize=10, frameon=False)  # 设置图例位置和样式
    fig.canvas.draw()

# 保存图表的函数
def save_plot():
    filename = "F1.png"  # 文件名
    fig.savefig(filename, dpi=300)  # 保存为高分辨率 PNG 文件
    print(f"Plot saved as {filename}")

# 绑定事件
fig.canvas.mpl_connect('button_press_event', onclick)
fig.canvas.mpl_connect('key_press_event', onkeypress)

plt.show()
