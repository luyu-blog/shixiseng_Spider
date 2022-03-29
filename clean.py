import os
import json
import jieba
with open("./dir/data.json",'r') as file:
    data = json.load(file)

# ? 学历统计
def edu_clean():
    
    data_dict = {
        "本科":0,
        "大专":0
                }
    with open("./dir/edu_.json",'w') as file:
        for i in data:
            if "本科" in i['education']:
                data_dict["本科"]  += 1
            if "大专" in i['education']:
                data_dict["大专"] += 1
        # print(data_dict)
        json.dump(data_dict,file,indent=4,ensure_ascii=False)


# ? 城市统计
def city_clean():
    data_dict = {}

    with open("./dir/city_.json",'w') as file:
        for city in data:
            data_dict[city['city']]=data_dict.get(city['city'], 0) + 1
        json.dump(data_dict,file,indent=4,ensure_ascii=False)
            

# ? 所需技能处理
def skill_clean():

    with open("./dir/miaoshu.txt",'r') as file:
        f = file.read()

    str = jieba.lcut(f)

    temp = ["linux","ansible","nginx","mysql","kvm","k8s","docker","salt","sed","awk","shell","python","zabbix","prometheus","elk"]
    with open("./dir/skill_clean.txt",'w') as file:
        for a in temp:
            for i in str:
                if a in i:
                    # print(a)
                    file.write(a+"\n")


# ? 日薪处理
def salary_clean():
    data_dict = {
    "80-120":0,
    "150-200":0,
    "200+":0,
            }
    with open("./dir/salary.json",'w') as file:
        for i in data:
            salary = int(i['salary'])
            if salary >=80 and salary <= 120:
                data_dict['80-120'] +=1
            if salary >=150 and salary <= 200:
                data_dict['150-200'] +=1
            if salary >200:
                data_dict['200+'] +=1
        json.dump(data_dict,file,indent=4,ensure_ascii=False)
        

if __name__ == "__main__":
    if not os.path.exists("./dir/edu_.json"):
        edu_clean()
    if not os.path.exists("./dir/city_.json"):
        city_clean()
    if not os.path.exists("./dir/salary.json"):
        salary_clean()
    if not os.path.exists("./dir/skill_clean.json"):
        skill_clean()
