try:
    from tkinter import *
    import requests
    from bs4 import BeautifulSoup
except:
    print('Required libraries are missing')

root = Tk()
root.minsize(500, 300)
root.maxsize(500, 300)
root.title('Watch Metal Price')
    
def gold_price():
    main_url = " https://www.paisabazaar.com/gold-rate/"
    r = requests.get(url=main_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.findAll(class_='g-6-s goldRate__price goldRatePriceHighLite')
    a = [i.text[3:] for i in data]
    return a[0]
    
def silver_price():
    main_url = 'https://www.goldpriceindia.com/platinum-price-india.php'
    r = requests.get(main_url)
    soup = BeautifulSoup(r.text,'html.parser')
    data = set(soup.find(class_='prc align-center pad-15'))
    return f" {str(data)[2:-2]} per gram"


def platinium_price():
    main_url = 'https://www.kitco.com/Platinum-price-today-India/'
    r = requests.get(main_url)
    soup = BeautifulSoup(r.text,'html.parser')
    data = soup.find(class_='table-price--body-table--overview-bid')
    x = ''
    for i,j in enumerate(data):
        if i==3:
            x = j
    return  f"{str(x)[3:12]} Rs per ounce"



L1 = Label(root,text='Metal List',font=('bold',20),bg='red',borderwidth=5,relief=SUNKEN)
L1.pack(fill='x')

Variable = StringVar(root)
Metal = 'metal'
Variable.set(Metal)
option = OptionMenu(root,Variable,*OPTIONS)
option.pack(fill='x',pady=20)

result = Entry(root,width=10,borderwidth=5)
result.pack(fill='x',pady=20)

F1 = Frame(root,bg='black',borderwidth=5,relief=SUNKEN)
F1.pack(side=BOTTOM)

button = Button(F1, text='GetPrice',width=20,bg='WHITE',fg='BLACK',font=('bold',8),command = GP)
button.pack(fill='x')
root.mainloop()
