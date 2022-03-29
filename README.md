# shixiseng_Spider
实习僧-运维工程师岗位分析


# 要求
```
实习僧-运维工程师岗位分析
1. 爬取岗位名称(positionName)、日薪(salary)、位置(city)、学历(education)、实习时间(time)、所需要的技能 

2. 分析本科、大专岗位占比              

3. 分析城市岗位数量     

4. 分析岗位所要的技能要求通过分词加上词云进行展示          

5. 日薪80-120  150-200 200以上                        

```

# Spider_web.py
```
主要实现爬取，并且筛选想要的数据
```

# clean.py
```
对爬取到的数据，进行学历、城市、所需的技能进行统计，方便之后的数据展示！
```

# chart.py
```
对处理好的数据进行可视化
```
![](https://b2.kuibu.net/file/imgdisk/imgs/2022/03/16477f0f7e61e7ab.png)

![](https://b2.kuibu.net/file/imgdisk/imgs/2022/03/3c78157261976b3c.png)

![](https://b2.kuibu.net/file/imgdisk/imgs/2022/03/11b3c303f972f8a5.png)

![](https://b2.kuibu.net/file/imgdisk/imgs/2022/03/3042ba5f5819714f.png)
