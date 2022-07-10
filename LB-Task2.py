import pandas as pd


df= pd.read_excel(r'C:\\Users\\ACER\Desktop\\intern\\Input_1.xlsx')
# print(df)

out = pd.DataFrame([], columns=['Name', 'Username', 'Chapter Tag', 'Test_Name', 'answered', 'correct', 'score', 'skipped', 'time-taken (seconds)', 'wrong'])
# print(out)

names = df['Name']
names_list = []

for i in range(0, len(names)):
    names_list.append(names[i])

# df_darshan = df.loc[df['Name'] == 'Darshan']
# # print(df_darshan)
# print(str(df_darshan.iat[0,2]))
num_tests = int ((len(df.columns) - 3) / 6)

column_names = df.columns
index = 0
for name in names_list:
    df_name = df.loc[df['Name'] == name]
    for i in range(1, num_tests + 1):
        temp = column_names[i * 6 - 3].split('-')
        test_name = temp[0].strip()
        username = df_name.iat[0, 1]
        chap_tag = df_name.iat[0, 2]
        score = df_name.iat[0, i * 6 - 3]
        if(str(score) == '-'):
            continue

        time_taken = df_name.iat[0, i * 6 - 2]
        answered = df_name.iat[0, i * 6 - 1]
        correct = df_name.iat[0, i * 6]
        wrong = df_name.iat[0, i * 6 + 1]
        skipped = df_name.iat[0, i * 6 + 2]

        out.loc[index] = [name, username, chap_tag, test_name, answered, correct, score, skipped, time_taken, wrong]
        index += 1
out.to_excel(r'C:\\Users\\ACER\Desktop\\intern\\abcd.xlsx')








