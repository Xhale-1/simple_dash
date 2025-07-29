# Для гитхаба
from pathlib import Path
import streamlit as st
import pandas as pd

p_loc = Path("local_bd_attnames.txt")
p_net = Path("network_bd_attnames.txt")
p_proj = Path('proj_bd_attnames.txt')

acc_attnames2 = []
or_attnames2 = []
proj_attnames2 = []

with p_loc.open(mode='r',encoding="utf-16 le") as f_loc:
    for line in f_loc:
        acc_attnames2.append(line.strip().strip('\n'))

with p_net.open(mode='r',encoding="utf-16 le") as f_net:
    for line in f_net:
        or_attnames2.append(line.strip().strip('\n'))
    
with p_proj.open(mode='r',encoding="utf-16 le") as f_proj: 
    for line in f_proj:
        proj_attnames2.append(line.strip().strip('\n'))




# assert(acc_attnames2 == acc_attnames)
# assert(or_attnames2 == or_attnames)

# # print(proj_attnames2)
# # print(proj_attnames)

# # for el1,el2 in zip(proj_attnames2, proj_attnames):
# #     if el1 != el2:
# #         print(f"'{el1}'", f"'{el2}'")

# assert(proj_attnames2 == proj_attnames)
# #assert(0)




#Таблица пересечения имён атрибутов

import pandas as pd

inter_proj_attnames_vs_acc_attnames = set(proj_attnames2) & set(acc_attnames2)
inter_proj_attnames_vs_or_attnames = set(proj_attnames2) & set(or_attnames2)
inter_acc_attnames_vs_or_attnames = set(acc_attnames2) & set(or_attnames2)
inter_all = set(acc_attnames2) & set(or_attnames2) & set(proj_attnames2)

cnt_inter_proj_attnames_vs_acc_attnames = len(inter_proj_attnames_vs_acc_attnames)
cnt_inter_proj_attnames_vs_or_attnames = len(inter_proj_attnames_vs_or_attnames)
cnt_inter_acc_attnames_vs_or_attnames = len(inter_acc_attnames_vs_or_attnames)
cnt_inter_all = len(inter_all)

otchet_inters = pd.DataFrame(
    data=[
        [str(len(proj_attnames2)), "-", "-"],
        [str(cnt_inter_proj_attnames_vs_acc_attnames), str(len(acc_attnames2)), "-"],
        [str(cnt_inter_proj_attnames_vs_or_attnames), str(cnt_inter_acc_attnames_vs_or_attnames), str(len(or_attnames2))]
    ],
    columns=['проект', 'локальная БД', 'сетевая БД'],
    index=['проект', 'локальная БД', 'сетевая БД']
)


# print("Таблица пересечения атрибутов:")
# print(otchet_inters)
# print(f"\nпересечение атрибутов всех трех: {cnt_inter_all}")

st.write("Таблица пересечения атрибутов:")
st.dataframe(otchet_inters)
st.write(f"пересечение атрибутов всех трех: {cnt_inter_all}")








#Таблица разностей имён атрибутов

diff_proj_attnames_vs_acc_attnames = set(proj_attnames2) - set(acc_attnames2)
diff_proj_attnames_vs_or_attnames = set(proj_attnames2) - set(or_attnames2)
diff_acc_attnames_vs_or_attnames = set(acc_attnames2) - set(or_attnames2)

cnt_diff_proj_attnames_vs_acc_attnames = len(diff_proj_attnames_vs_acc_attnames)
cnt_diff_proj_attnames_vs_or_attnames = len(diff_proj_attnames_vs_or_attnames)
cnt_diff_acc_attnames_vs_or_attnames = len(diff_acc_attnames_vs_or_attnames)

inter_diff_1_vs_3 = diff_proj_attnames_vs_acc_attnames & diff_acc_attnames_vs_or_attnames
inter_diff_2_vs_3 = diff_proj_attnames_vs_or_attnames & diff_acc_attnames_vs_or_attnames

cnt_inter_diff_1_vs_3 = len(inter_diff_1_vs_3)
cnt_inter_diff_2_vs_3 = len(inter_diff_2_vs_3)

otchet_diffs = pd.DataFrame(
    data=[
        ['0', "-", "-"],
        [str(cnt_diff_proj_attnames_vs_acc_attnames), '0', "-"],
        [str(cnt_diff_proj_attnames_vs_or_attnames), str(cnt_diff_acc_attnames_vs_or_attnames), '0']
    ],
    columns=['проект', 'локальная БД', 'сетевая БД'],
    index=['проект', 'локальная БД', 'сетевая БД']
)


# print("Таблица разности атрибутов:")
# print(otchet_diffs)

st.write("Таблица разности атрибутов:")
st.dataframe(otchet_diffs)


st.divider()

p = Path("used_att_data.txt")

with p.open(encoding='utf-16 le') as f:
    data_rows = []
    for line in f:
        d = line.strip().split(',')
        # print(d)
        new_row = {
                            'V1.3': d[0],
                            'OWNER': d[1],
                            'END': d[2],
                            'ATTNAME': d[3],
                            'ATTVALUE': d[4],
                            'ATTDREF': d[5],
                            'ATTVARI': d[6],
                            'ATTVALID': d[7],
                            'ATTFLGS2': d[8]
                        }

        data_rows.append(new_row)
    


all_used_proj_att_data2 = pd.DataFrame(data=data_rows[1:],columns= ['V1.3','OWNER','END','ATTNAME','ATTVALUE','ATTDREF','ATTVARI','ATTVALID','ATTFLGS2'])
#assert(all_used_proj_att_data2.equals(all_used_proj_att_data))


all_used_attnames2 = all_used_proj_att_data2['ATTNAME'].tolist()
all_uniq_used_attnames2 = list(set(all_used_attnames2))
#assert(all_uniq_used_attnames2 == all_uniq_used_attnames)



# print(len(all_uniq_used_attnames2))
# print(sorted(all_uniq_used_attnames2))
# print(len(all_used_attnames2))
# print(sorted(all_used_attnames2)[:100])

st.write(len(all_uniq_used_attnames2))
st.write(sorted(all_uniq_used_attnames2))
st.write(len(all_used_attnames2))
st.write(sorted(all_used_attnames2[:100]))



inter_uniq_used_attnames_vs_proj_attnames = set(all_uniq_used_attnames2) & set(proj_attnames2)
inter_uniq_used_attnames_vs_acc_attnames = set(all_uniq_used_attnames2) & set(acc_attnames2)
inter_uniq_used_attnames_vs_or_attnames = set(all_uniq_used_attnames2) & set(or_attnames2)
# print(len(inter_uniq_used_attnames_vs_proj_attnames))
# print(len(inter_uniq_used_attnames_vs_acc_attnames))
# print(len(inter_uniq_used_attnames_vs_or_attnames))
st.write(len(inter_uniq_used_attnames_vs_proj_attnames))
st.write(len(inter_uniq_used_attnames_vs_acc_attnames))
st.write(len(inter_uniq_used_attnames_vs_or_attnames))

