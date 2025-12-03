from bs4 import BeautifulSoup
import requests
from tkinter import *

window= Tk()
window.title("Currency Convertor")
window.minsize(height=400,width=500)
window.config(padx=20,pady=30,bg= "#dbce3e")
title=Label(text='CURRENCY CONVERTOR',font=('Arial',20),fg='Black')
title.grid()

def currency_convertor():
 from_curr=f_curr.get()
 to_curr= to_cur.get()
 amount=am.get()
 url= f'https://www.x-rates.com/calculator/?from={from_curr}&to={to_curr}&amount={amount}'
 url_get= requests.get(url)
 soup= BeautifulSoup(url_get.text,'html.parser')
 header= soup.find('span',class_='ccOutputRslt')
 return result.config(text=header.get_text())
f_label=Label(text='From :',font=('Arial',15),fg="black",highlightthickness=0)
f_label.grid(row=2,column=0,pady=20)
f_curr= Entry(width=20,bg="#e2979c",highlightthickness=0)
f_curr.grid(row=2,column=1,padx=20,pady=20)
to_label=Label(text='To :',font=('Arial',15),fg='black',highlightthickness=0)
to_label.grid(row=2,column=2)
am=Entry(width=20,bg="#e2979c",highlightthickness=0)
value=Label(text='Amount to :',font=('Arial',15),fg='black',highlightthickness=0)
value.grid(row=3,column=0,padx=20)
am.grid(row=3,column=1,pady=20)
to_cur= Entry(width=20,bg="#e2979c",highlightthickness=0)
to_cur.grid(row=2,column=3,padx=10,pady=20)
button2= Button(text='CONVERT', bg="white", fg="black", relief="raised",font=('Arial',20),highlightthickness=0,command=currency_convertor)
button2.grid(row=4,column=0,pady=20)
result=Label(text='',font=('Arial',20),bg='pink',fg="black",highlightthickness=0)
result.grid(row=4,column=2)
window.mainloop()