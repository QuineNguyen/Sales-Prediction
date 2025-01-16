import pandas as pd
import re

#Trich xuat phan so trong 1 chuoi
def extract_numbers(text):
    numbers = re.findall(r'\d+\.\d+', text)
    if numbers:
        return float(numbers[0])
    else:
        return 0
    
#Affilicate
#Xac dinh path cua file csv
pathAffilicate = 'Chapter2\Affilicate.csv'
data = pd.read_csv(pathAffilicate)

#Dat ten cho truong du lieu
data.columns = ['Date', 'Affilicate']

#Dua ve dinh dang ngay
data['Date'] = pd.to_datetime(data['Date'], format= '%Y-%m-%d')

#Chuan hoa du lieu so: bo ki hieu tien te, bo chu 'ti', don vi moi co kieu int va don vi la nghin dong
#Bo ky hieu đ
data['Affilicate'] = data['Affilicate'].replace({'₫': ''}, regex = True)
#string tỉ --> số thực
data['Affilicate'] = data['Affilicate'].replace({'tỉ': '*1e6'}, regex = True).map(pd.eval).astype(float)

#tạo list để đưa vào Dataframe
date_List = list(data['Date'])
affilicate_List = list(data['Affilicate'])

#Cua_hang

#path
pathCuaHang = 'Chapter2\Cua_hang.csv'
data1 = pd.read_csv(pathCuaHang)

data1.columns = ['Date', 'Cuahang']

data1['Date'] = pd.to_datetime(data['Date'], format= '%Y-%m-%d')

data1['Cuahang'] = data1['Cuahang'].replace({'₫': ''}, regex = True)

tmp_list = list(data1['Cuahang'])
cuahang_List = []
#Do phần chữ có k, tr, tỉ nên không thể replace all như phần trước, làm thủ công
for i in tmp_list:
    if(i[-2:] == 'tỉ'):
        cuahang_List.append(extract_numbers(i)* 1e6)
    elif(i[-2:] == 'tr'):
        cuahang_List.append(extract_numbers(i)* 1e3)
    else:
        cuahang_List.append(extract_numbers(i))
    
#Don gia binh quan
pathDongia = 'Chapter2\Don_gia_binh_quan.csv'
data2 = pd.read_csv(pathDongia)

data2.columns = ['Date', 'Dongia']

data2['Date'] = pd.to_datetime(data['Date'], format= '%Y-%m-%d')

#data2['TVH'] = data2['TVH'].replace({'₫': ''}, regex = True)

tmp_list = list(data2['Dongia'])
dongia_List = []
for i in tmp_list:
    if(i[-2:] == 'tỉ'):
        dongia_List.append(extract_numbers(i)* 1e6)
    elif(i[-2:] == 'tr'):
        dongia_List.append(extract_numbers(i)* 1e3)
    else:
        dongia_List.append(extract_numbers(i))

#Luot ban
pathLB = 'Chapter2\Luot_ban.csv'
data3 = pd.read_csv(pathLB)

data3.columns = ['Date', 'Luotban']

data3['Date'] = pd.to_datetime(data['Date'], format= '%Y-%m-%d')

#data3['TVH'] = data3['TVH'].replace({'₫': ''}, regex = True)

tmp_list = list(data3['Luotban'])
luotban_List = []
for i in tmp_list:
    if(i[-2:] == 'tỉ'):
        luotban_List.append(extract_numbers(i)* 1e6)
    elif(i[-2:] == 'tr'):
        luotban_List.append(extract_numbers(i)* 1e3)
    else:
        luotban_List.append(extract_numbers(i))


#Tu van hanh
pathTVH = 'Chapter2\Tu_van_hanh.csv'
data4 = pd.read_csv(pathTVH)

data4.columns = ['Date', 'TVH']

data4['Date'] = pd.to_datetime(data['Date'], format= '%Y-%m-%d')

data4['TVH'] = data4['TVH'].replace({'₫': ''}, regex = True)

tmp_list = list(data4['TVH'])
tvh_List = []
for i in tmp_list:
    if(i[-2:] == 'tỉ'):
        tvh_List.append(extract_numbers(i)* 1e6)
    elif(i[-2:] == 'tr'):
        tvh_List.append(extract_numbers(i)* 1e3)
    else:
        tvh_List.append(extract_numbers(i))

full_data = {
    'Ngày: ': date_List,
    'Doanh thu Affilicate (nghìn đồng)': affilicate_List,
    'Doanh thu cửa hàng (nghìn đồng)': cuahang_List,
    'Đơn giá bình quân (nghìn đồng)': dongia_List,
    'Lượt bán (nghìn lượt)': luotban_List,
    'Doanh thu tài khoản tự vận hành (nghìn đồng)': tvh_List,
}

df = pd.DataFrame(full_data)

df.to_csv('PreprocessingData.csv')