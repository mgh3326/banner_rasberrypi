import folium
import base64
from folium import IFrame
lat, lon = 37.566345, 126.977893
mapa = folium.Map(location=[lat, lon], zoom_start=17)
encoded = base64.b64encode(open('ctd.jpg', 'rb').read()).decode()

html = '<img src="data:image/jpeg;base64,{}">'.format
iframe = IFrame(html(encoded), width=800+20, height=450+20)
popup = folium.Popup(iframe, max_width=2650)

icon = folium.Icon(color="red", icon="ok")
marker = folium.Marker(location=[lat,lon], popup=popup, icon=icon)
mapa.add_child(marker)
mapa.save('./index.html')
