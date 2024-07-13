import difflib
import json
import os

import requests
from openpyxl.utils import get_column_letter
from tqdm import tqdm


def check_js(url,rate,cookie,is_saved):

    headers = {'Cookie': cookie}
    # 向服务器发送GET请求
    response = requests.get(url, headers=headers)
    f=open('yuchun.json', "w", encoding='utf-8')
    f.write(response .text)
    f.close()
    data_in_txt = open('yuchun.json', "r", encoding='utf-8')
    data_in_json = data_in_txt.readlines()
    data_in_pack_list = json.loads(data_in_json[0])
    data_submit_list = {}

    find_list = {}
    copy_list = {}

    for i in data_in_pack_list:
        if i['problem_id'] not in find_list.keys():
            find_list[i['problem_id']] = []
            copy_list[i['problem_id']] = []
        flag = 0
        for j in find_list[i['problem_id']]:
            if i['creator']['id'] == j['creator']['id']:
                flag = 1
                break
        if flag == 0:
            find_list[i['problem_id']].append(i)

    breakList = []
    all_used=[]

    for sub_list in find_list.keys():
        code_list = find_list[sub_list]
        if sub_list in breakList:  # problem_id == sublist
            continue
        print("finding %d..." % sub_list)
        used = {}
        jump = []
        tot = 0
        for i in tqdm(range(len(code_list))):
            if i in jump:
                continue
            for j in range(i + 1, len(code_list)):
                if j in jump:
                    continue
                code1 = code_list[i]['submission_code']['content']
                code2 = code_list[j]['submission_code']['content']
                ratio = difflib.SequenceMatcher(None, code1, code2).quick_ratio()
                if ratio > rate:

                    if i not in used.keys():
                        used[i] = []
                        used[i].append(code_list[i])
                    used[i].append(code_list[j])
                    jump.append(j)
        print("writing...")
        code_data = open("{}.txt".format(sub_list), "w", encoding='utf-8')
        print("problem_id=" + str(sub_list) + '\tcount=' + str(len(used.keys())))
        code_data.write("problem_id=" + str(sub_list) + '\tcount=' + str(len(used.keys())) + '\n')
        for i in used.keys():
            for j in used[i]:
                try:

                        code_data.write(
                            j['creator']['nickname'] + '\t' + j['creator']['student_id'] + '\t' + str(j['id']) + '\n')

                except UnicodeEncodeError:
                    print("EncodeError:", end='')
                    print(j['creator']['nickname'] + '\t' + j['creator']['student_id'] + '\t' + str(j['id']))
                except TypeError:
                    print("TypeError:", end='')
                    print(j['creator']['nickname'], end='\t')
                    print(j['creator']['student_id'], end='\t')
                    print(j['id'])
            code_data.write('\n')

        code_data.close()
        if is_saved==False:
            os.remove(str(sub_list)+".txt")

        all_used.append(used)
    return all_used




if __name__ == '__main__':
    cookie = '_ga=GA1.3.1486176174.1680276516; _ga_880Q45HJLT=GS1.3.1693059356.5.0.1693059356.0.0.0; UM_distinctid=18a39d50941885-05443a204a5c3-7f5d547e-186a00-18a39d50942110b; Hm_lvt_8edeba7d3ae859d72148a873531e0fa5=1695303521,1695533045,1697588145; connect.sid=s%3Ai2VGPqaow47VNqGroAuiEoVoJdfI9dvh.cbL292T5J9SHzzPKPXL5QInIEfg6FmPsxaGp7ys83Xk'
    headers = {'Cookie': cookie}
    url='https://accoding.buaa.edu.cn:4000/api/contests/1017/submissions_package'
    rate=0.95
    all_used=check_js(url,rate,cookie,True)


