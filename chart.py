import os
import json
from pyecharts.charts import Bar,Pie,Line
from pyecharts import options as opts


# * 日薪情况 柱形图
def salary_chart():
    
    with open("./dir/salary.json",'r') as file:
        data = json.load(file)

    bar = Bar()
    bar.set_global_opts(title_opts=opts.TitleOpts(title="运维工程师岗位日薪情况"))
    bar.add_xaxis([i for i in data])
    bar.add_yaxis("日薪情况", [data[i] for i in data])
    bar.render("./dir/salary_chart.html")




# * 大专、本科,运维工程师岗位占比 饼图
def education_chart():
    with open("./dir/edu_.json",'r') as file:
        data = json.load(file)

    pie=Pie()
    pie.add("", [list(z) for z in zip(data.keys(), data.values())],rosetype="radius")
    pie.set_global_opts(title_opts=opts.TitleOpts(title="大专、本科,运维工程师岗位占比"))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
    pie.render("./dir/edu_chart.html")
 

# * 城市岗位分布
def city_chart():
    with open("./dir/city_.json",'r') as file:
        data = json.load(file)
    # print(data)

    name = []
    num = []

    for i in data:
        if data[i] >=3:
            name.append(i)
            num.append(data[i])

    bar = Bar()
    bar.set_global_opts(title_opts=opts.TitleOpts(title="各城市岗位数量"))
    bar.add_xaxis([i for i in name])
    bar.add_yaxis("岗位数量", [i for i in num])
    bar.render("./dir/city_chart.html")





if __name__ == "__main__":
    if not os.path.exists('./dir/salary_chart.html'):
        salary_chart()
    if not os.path.exists('./dir/edu_chart.html'):
        education_chart()
    if not os.path.exists('./dir/city_chart.html'):
        city_chart()
