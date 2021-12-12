from tkinter import *
from tkinter.messagebox import showerror
import requests
from bs4 import BeautifulSoup
import html5lib
import win32gui , win32con
import webbrowser

root = Tk()
root.geometry("600x500")
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide,win32con.SW_HIDE)
root.minsize(600,500)
root.maxsize(600,500)
root.title("Price Tracker")
root.wm_iconbitmap('C:\\Users\\prince\\Desktop\\GUI\\Required files\\cart.ico')

Label(root,text="Flipkart Price Tracker",fg="red",font="Magneto 38 underline").pack()
Label(root,text="Enter the URL below ",font="calibri 15 underline").place(x=200,y=100)

url = Entry(root,font="calibri 15",width=50)
url.place(x=50,y=150)



def get_price():
    url_to_scrap = url.get()
    if url_to_scrap!="":
        try:
            r = requests.get(url_to_scrap)
            htmlContent = r.content
            soup = BeautifulSoup(htmlContent,'html.parser')

            # Getting the Title and Displaying it
            lst = url_to_scrap.split("/")
            lst_new = lst[3].split("-")
            title = " ".join(lst_new)
            final_title = title.capitalize() # Our final product Title
            
            product_name = Label(root,text="Product Name : ",font="calibri 15")
            product_name.place(x=30,y=280)

            title_lbl = Label(root,text=final_title,fg="red",font="calibri 15")
            title_lbl.place(x=180,y=280)

            dd = str(soup.find('div',class_ = "_3I9_wc _2p6lqe"))
            d = dd.split(">")
            lst1 = []
            for i in d[2] :
                if i.isnumeric():
                    lst1.append(i)

            highest_price = "".join(lst1)
            highest_price_lbl = Label(root,text=f"Highest Selling Price : ",font="calibri 15")
            highest_price_lbl.place(x=30,y=330)

            highest_price_value = Label(root,text=f"₹{highest_price}",font="calibri 15",fg="red")
            highest_price_value.place(x=230,y=330)

            current_Price = soup.find('div',class_ = "_30jeq3 _16Jk6d")
            c_price_lbl = Label(root,text="Current Price : ",font="calibri 15")
            c_price_lbl.place(x=30,y=380)

            price_lbl = Label(root,text=current_Price.string,fg="red",font="calibri 15")
            price_lbl.place(x=180,y=380)    

            def purchase():
                url_to_open = url.get()
                webbrowser.open(url_to_open)


            purchase_btn = Button(root,text="Buy it on Flipkart",fg="white",bg="red",font="calibri 15",command=purchase)
            purchase_btn.place(x=30,y=450)

            def refresh():
                product_name.config(text="")
                title_lbl.config(text="")
                c_price_lbl.config(text="")
                price_lbl.config(text="")
                url.delete(0, END)
                purchase_btn.destroy()
                
            refresh_btn = Button(root,text="Refresh",fg="blue",font="calibri 15",command=refresh)
            refresh_btn.place(x=450,y=450)

        except Exception as e:
            showerror("Only Flipkart URL","Dear user this is flipkart price tracer\nso please only enter flipkart URL.")

    else:
        showerror("Void URL","Dear User please enter the URL")


btn = Button(root,text="Get Info",fg="blue",font="calibri 15",command=get_price)
btn.place(x=250,y=200)

exit_btn = Button(root,text="Exit",fg="white",bg="red",font="calibri 15",command=exit)
exit_btn.place(x=550,y=450)

root.mainloop()
