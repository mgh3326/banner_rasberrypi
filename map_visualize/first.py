import pandas as pd
raw_data = pd.read_excel(
    ".//data//03.2018년8월31일기준_무인민원발급창구_설치장소_및_운영시간(민원24).xls")
print(raw_data.shape)
raw_data.head()

#google map 라이브러리로부터 경도, 위도 추출
import googlemaps
gmaps_key = "AIzaSyCV4UkHA4SHXRfriYrSHt3x2ASbTnszpRc"
gmaps = googlemaps.Client(key=gmaps_key)

raw_data['도로명주소'] = raw_data['도로명주소'].str.split('(').apply(lambda x: x[0])
raw_data['도로명주소'] = raw_data['도로명주소'].str.split(',').apply(lambda x: x[0])
raw_data_Seoul_position = raw_data[raw_data['시군구명'].str.contains('서울특별시')]
print(raw_data_Seoul_position.shape)
raw_data_Seoul_position.head()

for name in raw_data_Seoul_position.address:
    tmp = gmaps.geocode(name, language='ko')
    try:
        raw_data_Seoul_position.loc[raw_data_Seoul_position['address']
                                    == name, 'formatted_address'] = tmp[0].get("formatted_address")
        tmp_loc = tmp[0].get("geometry")
        raw_data_Seoul_position.loc[raw_data_Seoul_position['address']
                                    == name, 'lat'] = tmp_loc['location']['lat']
        raw_data_Seoul_position.loc[raw_data_Seoul_position['address']
                                    == name, 'lng'] = tmp_loc['location']['lng']
    except IndexError:
        print(tmp)
        pass
raw_data_Seoul_position.head()

for name in raw_data_Seoul_position.address:
    tmp = gmaps.geocode(name, language='ko')
    try:
        raw_data_Seoul_position.loc[raw_data_Seoul_position['address']
                                    == name, 'formatted_address'] = tmp[0].get("formatted_address")
        tmp_loc = tmp[0].get("geometry")
        raw_data_Seoul_position.loc[raw_data_Seoul_position['address']
                                    == name, 'lat'] = tmp_loc['location']['lat']
        raw_data_Seoul_position.loc[raw_data_Seoul_position['address']
                                    == name, 'lng'] = tmp_loc['location']['lng']
    except IndexError:
        print(tmp)
        pass
raw_data_Seoul_position.head()
