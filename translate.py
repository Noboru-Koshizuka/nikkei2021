import csv

f = open("newvalue.csv", "r")
reader = csv.reader(f)
data = [ e for e in reader ]
# print(data)
f.close()

# print(len(data), data[5][5])

print("data.addColumn(\'number\', \'" + data[0][0] + "\');")
print("data.addColumn(\'string\', \'" + data[0][1] + "\');")
print("data.addColumn(\'string\', \'" + data[0][2] + "\');")

for i in range(3, 24):
    print("data.addColumn(\'number\', \'" + data[0][i] + "\');")




for i in range(1,len(data)):
    # print(i)
    # print(data[i])
    print("data.addRow([")
    print("  {v:" + data[i][0] + ", f:\'" + data[i][0] + "\'}, ")
    print("  \'" + data[i][1] + "\', ")
    print("  \'" + data[i][2] + "\', ")
    print("  {v:" + data[i][3] + ", f:\'" + data[i][3] + "人\'}, ")
    print("  {v:" + data[i][4] + ", f:\'" + data[i][4] + "人\'}, ")
    print("  {v:" + data[i][5] + ", f:\'" + data[i][5] + "人\'}, ")
    print("  {v:" + data[i][6] + ", f:\'" + data[i][6] + "人\'}, ")
    print("  {v:" + data[i][7].replace('%', '') + ", f:\'" + data[i][7].replace('%', '') + "％\'}, ")
    print("  {v:" + data[i][8] + ", f:\'" + data[i][8] + " p\'}, ")
    print("  {v:" + data[i][9] + ", f:\'" + data[i][9] + "㎡\'}, ")
    print("  {v:" + data[i][10] + ", f:\'" + data[i][10] + " p\'}, ")
    print("  {v:" + data[i][11].replace('%', '') + ", f:\'" + data[i][11].replace('%', '') + "％\'}, ")
    print("  {v:" + data[i][12] + ", f:\'" + data[i][12] + " p\'}, ")
    print("  {v:" + data[i][13] + ", f:\'" + data[i][13] + "人\'}, ")
    print("  {v:" + data[i][14] + ", f:\'" + data[i][14] + "人\'}, ")
    print("  {v:" + data[i][15].replace('%', '') + ", f:\'" + data[i][15].replace('%', '') + "％\'}, ")
    print("  {v:" + data[i][16] + ", f:\'" + data[i][16] + " p\'}, ")
    print("  {v:" + data[i][17] + ", f:\'" + data[i][17] + "ヶ所\'}, ")
    print("  {v:" + data[i][18].replace('%', '') + ", f:\'" + data[i][18].replace('%', '') + "％\'}, ")
    print("  {v:" + data[i][19] + ", f:\'" + data[i][19] + " p\'}, ")
    print("  {v:" + data[i][20].replace('%', '') + ", f:\'" + data[i][20].replace('%', '') + "％\'}, ")
    print("  {v:" + data[i][21] + ", f:\'" + data[i][21] + " p\'}, ")
    print("  {v:" + data[i][22] + ", f:\'" + data[i][22] + "点\'}, ")
    print("  {v:" + data[i][23] + ", f:\'" + data[i][23] + "位\'}")
    print("]);")


    
    