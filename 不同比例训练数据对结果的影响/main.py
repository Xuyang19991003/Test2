import pandas as pd
import os
from matplotlib import pyplot as plt
# from matplotlib import rcParams
#
#
# # 设置全局字体为"Times New Roman"
# rcParams['font.family'] = 'serif'
# # 英文为Times New Roman
# rcParams['font.serif'] = ['Times New Roman']


#"#FF0000"红色
#"#00FF00"绿色
#"#0000FF"蓝色

def draw_one_figure(ax,x,method,sup,hard,soft,dataset):
    # 红色-三角
    ax.plot(x,sup,color="#FF0000",marker="^",markersize="15", lw="5", label=method2name[method])
    # 绿色-圆
    ax.plot(x,hard,color="#00FF00",marker="o",markersize="15", lw="5", label=method2name[method]+"+BLs")
    # 蓝色-方形
    ax.plot(x,soft,color="#0000FF",marker="s",markersize="15", lw="5", label=method2name[method]+"+FLs")
    # y轴的范围
    ax.set_ylim(0, 100)
    # 子标题
    ax.set_title(data2name[dataset],size=50,pad=20)
    # x轴坐标 和 y轴坐标
    #ax.set_xlabel("监督数据的比例", size=45,fontname='SimSun',labelpad=15)
    ax.set_xlabel("ratio of supervised data", size=40, labelpad=15)
    ax.set_ylabel("F1", size=40,labelpad=-15)

    # x轴和y轴刻度线的粗细（width） 和大小(labelsize)
    ax.tick_params(axis="x", width=3, labelsize=35)
    ax.tick_params(axis="y", width=3, labelsize=35)




def get_data_loc(data,axes):
    if data=="WA1":
        return axes[0]
    if data == "DS-small":
        return axes[1]
    if data == "IA1":
        return axes[2]
    if data == "Beer":
        return axes[3]


data2name={
    "WA1":"Walmart-Amazon1",
    "DS-small":"DBLP-ACM-small",
    "Beer":"Beer",
    "IA1":"iTunes-Amazon1"
}

method2name={
    "sif":"DM-SIF",
    "rnn":"DM-RNN",
    "attention":"DM-Att",
    "hybrid":"DM-Hyb"
}




def get_method_proference(method):
    figure, axes = plt.subplots(1, 4, sharex="none", sharey="none", figsize=(42, 11))
    dataset_list = ["WA1","DS-small","IA1","Beer"]
    for data in dataset_list:
        result_path = os.path.join(method,data,method+"-"+data+".csv")
        result_df = pd.read_csv(result_path)
        x_axis = result_df["训练集的比例"].tolist()

        sup = result_df["SUP"].tolist()
        hard = result_df["集成硬匹配规则"].tolist()
        soft = result_df["集成软匹配规则"].tolist()
        ax = get_data_loc(axes=axes,data=data)
        draw_one_figure(ax,x_axis,method,sup,hard,soft,data)
        #图例
        if data=="DS-small":
            ax.legend(loc='lower center', bbox_to_anchor=(1.25, -0.42),ncol=3,prop={'size': 35})



    # 设置图例标题的字体

    plt.subplots_adjust(bottom=0.25,left=0.04, right=0.97)

    plt.savefig(method + "-e.svg")
    #plt.savefig(method+"-c.svg")




if __name__ == '__main__':
    get_method_proference("hybrid")
