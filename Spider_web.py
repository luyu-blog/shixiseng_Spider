import os
import json
import requests
from time import sleep
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36",
}

# ! 爬取web对应数据
def Spider_index1():
    with open('./dir/url.txt', 'w') as file:
        for page in range(13):
            url = "https://www.shixiseng.com/interns?page={}&type=intern&keyword=%E8%BF%90%E7%BB%B4%E5%B7%A5%E7%A8%8B%E5%B8%88&city=%E5%85%A8%E5%9B%BD".format(page+1)
            r = requests.get(url,headers=headers)
            r.encoding = 'UTF-8'
            data = etree.HTML(r.text)
            # ? 把需要爬取岗位信息的url保存到url.txt
            for url in data.xpath('//div[@class="primary-content f-l"]//a[@class="title ellipsis font"]/@href'):
                file.write(url+"\n")
            sleep(5)
            print("爬取第{}页".format(page+1))





# ! 爬取岗位信息
def Spider_index2():
    data_list = [] #初始化一个列表 把data_dict存进来
    data_dict = {} #初始化一个字典 存放岗位信息

    with open("./dir/url.txt",'r') as file:
        read_data = file.readlines()


    with open("./dir/data.json",'w') as file:

        for url in read_data:
            r = requests.get(url)
            r.encoding = 'UTF-8'
            data = etree.HTML(r.text)
            for i in data.xpath('//div[@class="job-box"]'):
                positionName = i.xpath('.//div[@class="new_job_name"]/span/text()')[0] # * 岗位名称
                education = i.xpath('.//span[@class="job_academic"]/text()')[0] # * 学历
                city = i.xpath('.//span[@class="job_position"]/@title')[0] # * 城市
                salary = i.xpath('.//span[@class="job_money cutom_font"]/text()') # * 日薪
                time = i.xpath('.//span[@class="job_time cutom_font"]/text()')[0] # * 实习时间

                # * 对日薪进行处理
                print(salary)
                salary=salary[0].replace("/天","").split("-")
                if len(salary) == 2:
                    # salary=salary[0].replace("/天","").split("-")
                    salary_temp1 = int(salary[0])
                    salary_temp2 = int(salary[1])
                    salary = int((salary_temp1 + salary_temp2) /2)
                else:
                    salary=salary[0].replace("/天","")
                print(salary)

                # * 对实习时间进行处理
                time = time.replace("实习","").replace("个月","")

                # * 把数据存到字典里
                data_dict["positionName"] = positionName
                data_dict["education"] = education
                data_dict["city"] = city
                data_dict["salary"] = salary
                data_dict["time"] = time
                # * 然后统一把字典存到列表里面
                data_list.append(data_dict.copy())
                # print(data_dict)
            sleep(3)
        # * 导出数据到文件 
        json.dump(data_list,file,indent=4,ensure_ascii=False)

# ? 爬取所需技能
def Spider_index3():
    da = open("./dir/miaoshu.txt",'w')
    with open("./dir/url.txt",'r') as file:
        data = file.readlines()
        for url in data:
            r = requests.get(url)
            r.encoding = 'UTF-8'
            data = etree.HTML(r.text)
            for i in data.xpath('//div[@class="job_part"]//text()'):
                print(i)
                da.write(i)
    da.close()
if __name__ == "__main__":
    if not  os.path.exists("./dir/url.txt"):
        Spider_index1()
    if not  os.path.exists("./dir/data.json"):
        Spider_index2()
    if not  os.path.exists("./dir/miaoshu.txt"):
        Spider_index3()
    
