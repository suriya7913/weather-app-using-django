from django.shortcuts import render
import json 
import urllib.request
# Create your views here.
def index(request):
  if request.method =='POST':
    city =request.POST['city']
    res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city +'&appid=4e90a47e19bf3a73b6a241e3ff0a3316').read()
    json_data= json.loads(res)
    data={
      'country' : str(json_data['sys']['country']),
      'coordinate' : str(json_data['coord']['lon']) +' '+ str(json_data['coord']['lat']),
      'temp' : str(json_data['main']['temp'])+ ' kelvin',
      'pressure' : str(json_data['main']['pressure'] ),
      'humidity' : str(json_data['main']['humidity'] ),
      }
    print(data)
  else:
    city=''
    data={}
  return render(request,'index.html',{'city': city, 'data':data})