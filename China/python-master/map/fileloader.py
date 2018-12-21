import csv

def read(fileName):
    # Province names loaded from the first column of ChinaData.csv 
    # and used to match NAME_1 property in states.info in CHN_adm1 file.
    # They should be
    #'Guangdong', 'Shandong', 'Gansu', 'Tianjin', 
    #             'Shaanxi', 'Heilongjiang', 'Zhejiang', 
    #             'Xinjiang Uygur', 'Anhui', 'Beijing', 'Qinghai', 
    #             'Henan', 'Liaoning', 'Hubei', 'Hainan', 'Jiangsu', 
    #             'Yunnan', 'Fujian', 'Guizhou', 'Chongqing', 'Shanghai', 
    #             'Xizang', 'Shanxi', 'Sichuan', 'Hebei', 'Ningxia Hui', 
    #             'Nei Mongol', 'Guangxi', 'Jiangxi', 'Hunan', 'Jilin']
    provinces = []
    
    # value loaded from the second column of ChinaData.csv
    values = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                province = row[0]
                value = int(row[1])
                provinces.append(province)
                values.append(value)
                line_count += 1
        print(f'Read {line_count-1} lines')
    return (provinces, values)
