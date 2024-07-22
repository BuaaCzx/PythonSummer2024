import difflib
import json
import os
import shutil
from datetime import time


def check_js(self):
    def destroy() -> None:
        self.destroy_btn.place_forget()
        progressbar.destroy()
        process_label.destroy()

    self.inv_result.set_sheet_data(data=[])
    self.inv_result.redraw()
    self.rate = float(str(self.txt_inv_rate))
    print("self.rate", self.rate)

    is_saved = self.checkbox_var.get()
    self.inv_all_data = []
    number_work = self.data.data_handler.contests[self.data.contest_combobox_id][0]
    self.current_contest = self.cbb_contest.get_current_id()
    _, self.num2id = self.data.data_handler.getIdMatch(self.data.data_handler.contests[self.current_contest][0])

    response = self.data.data_handler.vpn.session.get(
        url=self.data.data_handler.vpn.code_package_api_url(number_work),
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36",
            "Referers": self.data.data_handler.vpn.index_url
        })
    inv_file = os.path.join(self.data.data_handler.download_inv_path, number_work)
    if not os.path.exists(inv_file):
        os.mkdir(inv_file)
    f = open(os.path.join(inv_file, 'yuchun.json'), "w", encoding='utf-8')
    f.write(response.text)
    f.close()
    data_in_txt = open(os.path.join(inv_file, 'yuchun.json'), "r", encoding='utf-8')
    data_in_json = data_in_txt.readlines()
    data_in_pack_list = json.loads(data_in_json[0])

    find_list = {}

    for i in data_in_pack_list:  # 枚举学生
        if i['problem_id'] not in find_list.keys():
            find_list[i['problem_id']] = []
        flag = 0
        for j in find_list[i['problem_id']]:
            if i['creator']['id'] == j['creator']['id']:
                flag = 1
                break
        if flag == 0:
            find_list[i['problem_id']].append(i)

    find_list = dict(sorted(find_list.items(), key=lambda x: self.num2id[str(x[0])]))
    breakList = []
    trans_dict = {"\t": "", "\n": "", " ": ""}

    for sub_list in find_list.keys():  # 枚举题目编号

        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(current_time)

        code_list = find_list[sub_list]  # 该题目的所有提交
        if sub_list in breakList:  # problem_id == sublist
            continue
        print("finding %d..." % sub_list)  # 当前在查的题目编号
        used = {}
        jump = []
        self.destroy_btn = tkinter.Button(self.frm_table, text='取消查重', command=destroy)
        self.destroy_btn.place(x=(self.winfo_width() - self.lbar_width - 120) // 2,
                               y=300 * (self.winfo_width() - self.lbar_width) // (1000 - self.lbar_width),
                               width=100, height=50)
        progressbar = tkinter.ttk.Progressbar(self.frm_table, length=400 * (self.winfo_width() - self.lbar_width) // (
                    1000 - self.lbar_width), mode='determinate')
        progressbar.place(x=200 * (self.winfo_width() - self.lbar_width) // (1000 - self.lbar_width),
                          y=(self.winfo_height() - 100) // 2)
        progressbar['maximum'] = len(code_list)
        progressbar['value'] = 0

        process_label = tkinter.Label(self.frm_table, text='正在查重: ' + self.num2id[str(sub_list)])
        process_label.place(x=(self.winfo_width() - self.lbar_width - 100) // 2,
                            y=150 * (self.winfo_width() - self.lbar_width) // (1000 - self.lbar_width))

        # 暴力枚举, difflib库进行判断
        try:
            for i in range(len(code_list)):
                progressbar['value'] += 1
                self.frm_table.update()
                if i in jump:
                    continue
                for j in range(i + 1, len(code_list)):
                    if j in jump:
                        continue
                    code1 = code_list[i]['submission_code']['content'].translate(str.maketrans(trans_dict))
                    code2 = code_list[j]['submission_code']['content'].translate(str.maketrans(trans_dict))
                    ratio = difflib.SequenceMatcher(None, code1, code2).quick_ratio()
                    if ratio > self.rate:
                        if i not in used.keys():
                            used[i] = []
                            used[i].append(code_list[i])
                        used[i].append(code_list[j])
                        jump.append(j)
        except _tkinter.TclError as err:
            return
        progressbar.destroy()
        process_label.destroy()
        print("writing...")
        process_pro_id = self.num2id[str(sub_list)] + ' ' + str(sub_list)
        self.inv_all_data.append([process_pro_id.replace(' ', " : ")])  # , 'count : ' + str(len(used.keys()))
        code_data = open(os.path.join(inv_file, "{}.txt".format(process_pro_id.replace(' ', '_'))), "w",
                         encoding='utf-8')
        code_data.write("problem_id=" + str(sub_list) + '\tcount=' + str(len(used.keys())) + '\n')
        for i in used.keys():
            # if len(used[i]) > 8:  # 当查重人数过多时, 判定为题目问题
            #     continue
            for j in used[i]:
                try:
                    self.inv_all_data.append([j['creator']['nickname'], j['creator']['student_id'], str(j['id'])])
                    code_data.write(
                        j['creator']['nickname'] + '\t' + j['creator']['student_id'] + '\t' + str(j['id']) + '\n')

                except UnicodeEncodeError:
                    pass
                    # print("EncodeError:", end='')
                    # print(j['creator']['nickname'] + '\t' + j['creator']['student_id'] + '\t' + str(j['id']))
                except TypeError:
                    pass
                    # print("TypeError:", end='')
                    # print(j['creator']['nickname'], end='\t')
                    # print(j['creator']['student_id'], end='\t')
                    # print(j['id'])
            self.inv_all_data.append([])
            code_data.write('\n')

        self.destroy_btn.destroy()
        code_data.close()
    data_in_txt.close()

    if not is_saved:
        shutil.rmtree(inv_file)

    self.cbb_course_global_filterby_select()
