import pickle
from django.shortcuts import render

def form(request):
    if request.method == 'GET':
        return render(request,"form.html")

    bedrooms = int(request.POST['bedrooms'])
    bathrooms = int(request.POST['bathrooms'])
    area = int(request.POST['area'])
    location = request.POST['location']

    locations = ['ahmedabad','bangalore','chennai','delhi','hyderabad','mumbai','pune']
    mylocation = []
    for i in locations:
        if i==location:
            mylocation.append(1)
        else:
            mylocation.append(0)
    a,b,c,d,h,m,p = mylocation

    f = open("model.pkl", "rb")
    mf = pickle.load(f)
    price = mf.predict([[bedrooms,bathrooms,area,a,b,c,d,h,m,p]])
    price = float("%.3f"%price)
    # print(bedrooms,bathrooms,area,a,b,c,d,h,m,p)
    # print(price)
    return render(request, "form.html", {'price':price})
    
