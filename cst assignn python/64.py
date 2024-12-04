##64.	Develop a weather application that retrieves data from an API and displays it using plots.very short 

import requests 
import matplotlib.pyplot as plt 

api_key ="your_api_key"
city="indore"
url=f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
if response.status_code != 200:
    print("failed to retrieve data")
    exit()
data = response.json()

times = [item['dt_txt']for item in data ['list'][:10]]
temps = [item['main']['temp']for item in data['list'][:10]]

plt.plot(times, temps , marker='o')
plt.xticks(rotation=45)
plt.title(f"weather forecast for {city}")
plt.xlabel("time")
plt.ylabel("temperature(.c)")
plt.tight_layout()
plt.show()