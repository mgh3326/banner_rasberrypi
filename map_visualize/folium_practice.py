import folium
map_osm = folium.Map(location=[37.566345, 126.977893])
map_osm.save('./out/map1.html')  # 파일이 저장될 위치
map_osm = folium.Map(location=[37.566345, 126.977893], zoom_start=17)
folium.Marker([37.566345, 126.977893], popup='서울특별시청', icon=folium.Icon(
    color='red')).add_to(map_osm)
folium.Marker([37.5658859, 126.9754788], popup='덕수궁').add_to(map_osm)
map_osm.save('./out/map5.html')
