#import all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox  #This module is used to display message boxes
import datetime
import math
import os
import random


conn = sqlite3.connect("C:/Users/Dell/Desktop/attachments/store.db")
c = conn.cursor()

#date
date = datetime.datetime.now().date()

#temporary lists like sessions
products_list = []
product_price = []
product_quantity = []
product_id = []

#labels list
labels_list=[]
##########################ADD TO DATABASE##############################################################################

class add:
    def get_items(self, *args, **kwargs):
            # get from entries
        self.name = self.name_entry.get()
        self.stock = self.stock_entry.get()
        self.cp = self.costp_entry.get()
        self.sp = self.sellingp_entry.get()
        self.vendor = self.vendor_entry.get()
        self.vendor_phone = self.vendorphone_entry.get()

            # dynamic entries
        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)
        self.assumed_profit = float(self.totalsp - self.totalcp)

        if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '':
            tkinter.messagebox.showinfo("Error", "Please fill all the entries")

        else:
            sql = "INSERT INTO INVENTORY (name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phoneno) VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor,self.vendor_phone))
            conn.commit()
                # textbox Insert
            self.textbox.insert(END,"\n\nInserted" + str(self.name) + "Into the database with code" + str(self.id_e.get()))
            tkinter.messagebox.showinfo("Success", "Successfully added to the database")
class clear_all():
    def clear_all(self, *args, **kwargs):
        self.name_entry.delete(0,END)
        self.stock_entry.delete(0,END)
        self.costp_entry.delete(0,END)
        self.sellingp_entry.delete(0,END)
        self.vendor_entry.delete(0,END)
        self.vendorphone_entry.delete(0,END)
        self.id_e.delete(0,END)


class Add_to_Database(add,clear_all):
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="ADD TO DATABASE", font=('arial 40 bold'), fg='grey25')
        self.heading.place(x=400, y=0)

        self.i = Label(master, text="ID HAS REACHED UPTO:" + str(id), fg='grey25',font=('arial 18 bold'))    #Label- single line caption/ short text, it can also contain image
        self.i.place(x=0, y=40)

        # labels  for the windows
        self.name_l = Label(master, text="ENTER PRODUCT NAME", font=('arial 18 bold'), fg='grey25')
        self.name_l.place(x=0, y=70)

        self.stock_l = Label(master, text="ENTER STOCKS", font=('arial 18 bold'), fg='grey25')
        self.stock_l.place(x=0, y=120)

        self.cp_l = Label(master, text="ENTER COST PRICE", font=('arial 18 bold'), fg='grey25')
        self.cp_l.place(x=0, y=170)

        self.sp_l = Label(master, text="ENTER SELLING PRICE", font=('arial 18 bold'), fg='grey25')
        self.sp_l.place(x=0, y=220)

        self.vendor_l = Label(master, text="ENTER VENDOR", font=('arial 18 bold'), fg='grey25')
        self.vendor_l.place(x=0, y=270)

        self.vendor_phone_l = Label(master, text="ENTER VENDOR PHONE NUMBER", font=('arial 18 bold'), fg='grey25')
        self.vendor_phone_l.place(x=0, y=320)

        self.id_l = Label(master, text="ENTER ID", font=('arial 18 bold'), fg='grey25')
        self.id_l.place(x=0, y=370)

        # entries for the labels
        self.name_entry = Entry(master, width=25, font=('arial 18 bold'),bg='goldenrod3', fg='grey25')
        self.name_entry.place(x=380, y=70)

        self.stock_entry = Entry(master, width=25, font=('arial 18 bold'),bg='goldenrod3', fg='grey25')
        self.stock_entry.place(x=380, y=120)

        self.costp_entry = Entry(master, width=25, font=('arial 18 bold'),bg='goldenrod3', fg='grey25')
        self.costp_entry.place(x=380, y=170)

        self.sellingp_entry = Entry(master, width=25, font=('arial 18 bold'),bg='goldenrod3', fg='grey25')
        self.sellingp_entry.place(x=380, y=220)

        self.vendor_entry = Entry(master, width=25, font=('arial 18 bold'),bg='goldenrod3', fg='grey25')
        self.vendor_entry.place(x=380, y=270)

        self.vendorphone_entry = Entry(master, width=25, font=('arial 18 bold'),bg='goldenrod3', fg='grey25')
        self.vendorphone_entry.place(x=380, y=320)

        self.id_e = Entry(master, width=25, font=('arial 18 bold'),bg='goldenrod3', fg='grey25')
        self.id_e.place(x=380, y=370)

        # button to add to the database
        self.btn_add = Button(master, text="ADD TO DATABASE", width=25, height=2,bg='goldenrod3', fg='grey25',
                              command=self.get_items)
        self.btn_add.place(x=520, y=420)

        self.btn_clear = Button(master, text="CLEAR ALL FIELDS", width=18, height=2, bg='lightgreen', fg='grey25',
                                command=self.clear_all)
        self.btn_clear.place(x=380, y=420)

        # text box for the logs
        self.textbox = Text(master, width=60, height=18)
        self.textbox.place(x=750, y=70)
        self.textbox.insert(END, "ID has reached upto : " + str(id))


##########################UPDATE DATABASE##############################################################################
result = c.execute("SELECT Max(id) from inventory")
for r in result:
    id = r[0]


class search:
    def search(self, *args, **kwargs):
        sql = "SELECT * FROM INVENTORY WHERE id=?"
        result = c.execute(sql, (self.id_leb.get(),))
        for r in result:
            self.n1 = r[1] #name
            self.n2 = r[2] #stock
            self.n3 = r[3] #cp
            self.n4 = r[4] #sp
            self.n5 = r[5] #totalcp
            self.n6 = r[6] #totalsp
            self.n7 = r[7] #assumed_profit
            self.n8 = r[8] #vendor
            self.n9 = r[9] #vendor_phone
        conn.commit()

        #insert into the entries to update
        self.name_entry.delete(0, END)
        self.name_entry.insert(0,str(self.n1))

        self.stock_entry.delete(0, END)
        self.stock_entry.insert(0,str(self.n2))

        self.costp_entry.delete(0, END)
        self.costp_entry.insert(0,str(self.n3))

        self.sellingp_entry.delete(0, END)
        self.sellingp_entry.insert(0,str(self.n4))

        self.vendor_entry.delete(0, END)
        self.vendor_entry.insert(0,str(self.n8))

        self.vendorphone_entry.delete(0, END)
        self.vendorphone_entry.insert(0,str(self.n9))

        self.totalcostp_entry.delete(0, END)
        self.totalcostp_entry.insert(0,str(self.n5))

        self.totalsellingp_entry.delete(0, END)
        self.totalsellingp_entry.insert(0,str(self.n6))

class update:
    def update(self, *args, **kwargs):
        #get all the updated values
        self.u1=self.name_entry.get()
        self.u2=self.stock_entry.get()
        self.u3=self.costp_entry.get()
        self.u4=self.sellingp_entry.get()
        self.u5=self.totalcostp_entry.get()
        self.u6=self.totalsellingp_entry.get()
        self.u7=self.vendor_entry.get()
        self.u8=self.vendorphone_entry.get()

        query = "UPDATE  inventory SET name=?, stock=?, cp=?, sp=?, totalcp=?, totalsp=?, vendor=?, vendor_phoneno=? WHERE id=?"
        c.execute(query,(self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.u7, self.u8, self.id_leb.get()))
        conn.commit()
        tkinter.messagebox.showinfo("SUCCESS", "UPDATE TO DATABASE")
class clear_all():
    def clear_all(self, *args, **kwargs):
        self.name_entry.delete(0,END)
        self.stock_entry.delete(0,END)
        self.costp_entry.delete(0,END)
        self.sellingp_entry.delete(0,END)
        self.vendor_entry.delete(0,END)
        self.vendorphone_entry.delete(0,END)
        self.id_leb.delete(0,END)
        self.totalsellingp_entry.delete(0,END)
        self.totalcostp_entry.delete(0, END)



class Database(search, update,clear_all):
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.heading = Label(master, text="UPDATE THE DATABASE", font=('arial 40 bold'), fg='grey25')    #Label- single line caption/ short text, it can also contain image
        self.heading.place(x=400, y=0)

        # label and entry for id
        self.id_le= Label(master, text="ENTER ID", font=('arial 18 bold'))
        self.id_le.place(x=0, y=70)

        self.id_leb = Entry(master, font=('arial 18 bold'), width=10)
        self.id_leb.place(x=380, y=70)

        self.btn_search = Button(master, text="SEARCH", width=15, height=2, bg='goldenrod3', command=self.search)
        self.btn_search.place(x=550, y=70)

        # labels  for the windows
        self.name_l = Label(master, text="ENTER PRODUCT NAME", font=('arial 18 bold'))
        self.name_l.place(x=0, y=120)

        self.stock_l = Label(master, text="ENTER STOCKS", font=('arial 18 bold'))
        self.stock_l.place(x=0, y=170)

        self.cp_l = Label(master, text="ENTER COST PRICE", font=('arial 18 bold'))
        self.cp_l.place(x=0, y=220)

        self.sp_l = Label(master, text="ENTER SELLING PRICE", font=('arial 18 bold'))
        self.sp_l.place(x=0, y=270)

        self.totalcp_l = Label(master, text="ENTER TOTAL COST PRICE ", font=('arial 18 bold'))
        self.totalcp_l.place(x=0, y=320)

        self.totalsp_l = Label(master, text="ENTER TOTAL SELLING PRICE", font=('arial 18 bold'))
        self.totalsp_l.place(x=0, y=370)

        self.vendor_l = Label(master, text="ENTER VENDOR", font=('arial 18 bold'))
        self.vendor_l.place(x=0, y=420)

        self.vendor_phone_l = Label(master, text="ENTER VENDOR PHONE NUMBER", font=('arial 18 bold'))
        self.vendor_phone_l.place(x=0, y=470)

        # entries for the labels
        self.name_entry = Entry(master, width=25, font=('arial 18 bold'))
        self.name_entry.place(x=380, y=120)

        self.stock_entry = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_entry.place(x=380, y=170)

        self.costp_entry = Entry(master, width=25, font=('arial 18 bold'))
        self.costp_entry.place(x=380, y=220)

        self.sellingp_entry = Entry(master, width=25, font=('arial 18 bold'))
        self.sellingp_entry.place(x=380, y=270)

        self.totalcostp_entry = Entry(master, width=25, font=('arial 18 bold'))
        self.totalcostp_entry.place(x=380, y=320)

        self.totalsellingp_entry = Entry(master, width=25, font=('arial 18 bold'))
        self.totalsellingp_entry.place(x=380, y=370)

        self.vendor_entry = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_entry.place(x=380, y=420)

        self.vendorphone_entry = Entry(master, width=25, font=('arial 18 bold'))
        self.vendorphone_entry.place(x=380, y=470)

        # button to add to the database
        self.btn_add = Button(master, text="UPDATE DATABASE", width=25, height=2, bg='steelblue', fg='grey25',
                              command=self.update)
        self.btn_add.place(x=520, y=520)
        self.btn_clear = Button(master, text="CLEAR ALL FIELDS", width=18, height=2, bg='lightgreen', fg='grey25',
                                command=self.clear_all)
        self.btn_clear.place(x=375, y=520)

        # text box for the logs
        self.textbox = Text(master, width=60, height=18)
        self.textbox.place(x=750, y=70)
        self.textbox.insert(END, "ID has reached upto :" + str(id))


##########################MAIN PROGRAM##############################################################################
class bill:
    def generate_bill(self, *args, **kwargs):
        # create the bill before updating to the database
        directory = "D:/Store Management software/Invoice/" + str(date) + "/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        # templates for the bill
        store = "\t\t\tBismillah Store\n"
        address = "\t\t\tNed University Of Engineering & Technology\n"
        phone = "\t\t\t03332385444\n"
        sample = "\t\t\tInvoice\n"
        dt = "\t\t\t" + str(date)

        table_header = "\n\n\t\t*************************************************\n\t\tSN.\t\tProducts\t\tQty\t\tAmount\n\t\t*************************************************"
        final = store + address + phone + sample + dt + "\n" + table_header

        # open a file to write it to
        file_name = str(directory) + str(random.randrange(5000, 10000)) + ".rtf"
        f = open(file_name, "w")
        f.write(final)

        # file dynamics
        r = 1
        i = 0
        for t in products_list:
            f.write("\n\t\t" + str(r) + "\t\t" + str(products_list[i] + ".......")[:9] + "\t\t" + str(
                product_quantity[i]) + "\t\t" + str(product_price[i]))
            i += 1
            r += 1

        f.write("\n\n\t\tTotal: Rs. " + str(sum(product_price)))
        f.write("\n\t\tThanks for visiting")

        f.close()
        # decrease the stock
        self.x = 0

        initial = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(initial, (product_id[self.x],))

        for i in products_list:
            for r in result:
                self.old_stock = r[2]
            self.new_stock = int(self.old_stock) - int(product_quantity[self.x])

            # updating the stock
            sql = "UPDATE inventory SET stock=? WHERE id=?"
            c.execute(sql, (self.new_stock, product_id[self.x]))
            conn.commit()
            # insert into the transactions
            sql2 = "INSERT INTO transactions (product_name, quantity, amount, date) VALUES(?, ?, ?, ?)"
            c.execute(sql2, (products_list[self.x], product_quantity[self.x], product_price[self.x], date))
            conn.commit()

            self.x += 1

            for j in labels_list:
                j.destroy()

            del(products_list[:])
            del(product_price[:])
            del(product_quantity[:])
            del(product_id[:])

            self.change_e.delete(0,END)
            self.c_amount.configure(text="")
            self.total_l.configure(text="")

            
            #after generating bill the cursor will be focus to id entry box
            self.enterid_e.focus()

            
        tkinter.messagebox.showinfo("Success", "Done everything smoothly")




class info(bill):
    def idsearch(self, *args, **kwargs):
        #get the product info with that id and fill it with the labels above
        self.get_id = self.enterid_e.get()
        query = "SELECT * FROM inventory WHERE id=?"
        result =c.execute(query, (self.get_id, ))
        for self.r in result:
            self.get_id = self.r[0]
            self.get_name = self.r[1]
            self.get_price = self.r[4]
            self.get_stock = self.r[2]
        self.productname.configure(text="Product's Name:" + str(self.get_name))
        self.pprice.configure(text="Price: Rs." + str(self.get_price))

        #quantity and the discount label
        self.quantity_l = Label(self.left, text="Enter Quantity", font=('arial 18 bold'),fg='goldenrod3',bg="grey25" ) #Label- single line caption/ short text, it can also contain image
        self.quantity_l.place(x=0, y=370)

        self.quantity_e = Entry(self.left, width=25, font=('arial 18 bold'),fg='grey25', bg="goldenrod3")
        self.quantity_e.place(x=190, y=370)
        self.quantity_e.focus()

        #discount

        self.discount_l = Label(self.left, text="Enter Discount", font=('arial 18 bold'),fg='goldenrod3', bg="grey25")
        self.discount_l.place(x=0, y=410)




        self.discount_e = Entry(self.left, width=25, font=('arial 18 bold'),fg='goldenrod3', bg="goldenrod3")
        self.discount_e.place(x=190, y=410)
        self.discount_e.insert(END, 0)

        #add to cart button
        self.add_to_cart_btn = Button(self.left, text="Add to cart", width=22, height=2, fg='grey25',bg="goldenrod3", command=self.add_to_cart)
        self.add_to_cart_btn.place(x=350, y=450)

        #generate bill and change
        self.change_l = Label(self.left, text="Given Amount", font=('arial 18 bold'), bg="grey25")
        self.change_l.place(x=0 , y=550)


        self.change_e = Entry(self.left, width=25, font=('arial 18 bold'), bg="goldenrod3")
        self.change_e.place(x=190, y=550)

        #buttonchange

        self.change_btn = Button(self.left, text="Calculate Change", width=22, height=2,fg='grey25', bg="goldenrod3", command=self.change_func)
        self.change_btn.place(x=350, y=590)

        # exit button
        self.exit = Button(self.left, width=22, height=2, text="Exit", bg="goldenrod3",fg="grey25" , command=self.exit)
        self.exit.place(x=520, y=590)

        #generate bill button

        self.bill_btn = Button(self.left, text="Generate Bill", width=100, height=2, bg="red", fg="goldenrod3", command=self.generate_bill)
        self.bill_btn.place(x=0, y=640)

class cart:
    def add_to_cart(self, *args, **kwargs):
        #get the qauntity value and from the database
        self.quantity_value = int(self.quantity_e.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo("Error", "Not that many product in our inventory")
        else:
            #calculate the price
            self.final_price = (float(self.quantity_value)* float(self.get_price)) - (float(self.discount_e.get()))

            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)

            self.x_index = 0
            self.y_index = 100
            self.counter = 0
            for self.p in products_list:
                self.tenpname = Label(self.right, text=str(products_list[self.counter]), font=('arial 18 bold'), bg="goldenrod3", fg="grey25")
                self.tenpname.place(x=0, y=self.y_index)
                labels_list.append(self.tenpname)

                self.tempqt_l = Label(self.right,text=str(product_quantity[self.counter]), font=('arial 18 bold'), bg="goldenrod3",fg="grey25")
                self.tempqt_l.place(x=300, y=self.y_index)
                labels_list.append(self.tempqt_l)

                self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('arial 18 bold'), bg="goldenrod3",fg="grey25")
                self.tempprice.place(x=500, y=self.y_index)
                labels_list.append(self.tempprice)

                self.y_index+=40
                self.counter+=1

                self.total_l.configure(text="Total: Rs." + str(sum(product_price)))       #final price append kia huwa productprice ki list men tw direct ajaega yahan pr

                #delete
                self.quantity_l.place_forget() #forget=it forgets its own place and vanishes
                self.quantity_e.place_forget()
                self.discount_l.place_forget()
                self.discount_e.place_forget()
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.add_to_cart_btn.destroy()  #destroy=remove messup

                #autofocus  to enter id
                self.enterid_e.focus()
                self.enterid_e.delete(0, END)



        




class change:
    def change_func(self, *args, **kwargs):
            #get the amount given by customer and the amount generated by the computer
        self.amount_given = float(self.change_e.get())
        self.our_total = float(sum(product_price))

        self.to_give = self.amount_given - self.our_total

            #label change;
        self.c_amount = Label(self.left, text="Change: Rs." + str(self.to_give), font=('arial 18 bold'), fg="red", bg="grey25")
        self.c_amount.place(x=0, y=600)



class Application(info,cart,bill,change):
    def __init__(self, master, *args, **kwargs):
        #frames
        self.master = master
        self.left = Frame(master, width=700, height=768, bg="grey25")     #Frame- a container widget,jska apna ek backgorund or border ho window k andar
        self.left.pack(side=LEFT)                                         #Pack- geometry manager, widgets ko ek particular jagah assign krta hai

        self.right = Frame(master, width=666, height=768, bg='goldenrod3')
        self.right.pack(side=RIGHT)

        #components
        self.heading=Label(self.left, text="MINI IMTIAZ", font=('stampsy 40 bold'), fg="goldenrod3", bg="grey25")     #Label- single line caption/ short text, it can also contain image
        self.heading.place(x=0, y=0)

        self.date_l=Label(self.right, text="Today's Date:" +  str(date), font=('helevetica 16 bold'), bg="goldenrod3", fg="grey25")
        self.date_l.place(x=0, y=0)

        #table in voice***************************************************************
        self.tproduct = Label(self.right, text="Products", font=('arial 18 bold'), bg="goldenrod3" , fg="grey25") 
        self.tproduct.place(x=0, y=60)

        self.tquantity = Label(self.right, text="Quantity", font=('arial 18 bold'), bg="goldenrod3" , fg="grey25")
        self.tquantity.place(x=300, y=60)


        self.tamount = Label(self.right, text="Amount", font=('arial 18 bold'), bg="goldenrod3" , fg="grey25")
        self.tamount.place(x=500, y=60)

        #enter stuff
        self.enterid = Label(self.left, text="Enter ID", font=('stampsy 18 bold'), fg="goldenrod3", bg="grey25")
        self.enterid.place(x=0, y=150)

        self.enterid_e= Entry(self.left, width=25, font=('arial 18 bold'), fg='grey25', bg="goldenrod3")
        self.enterid_e.place(x=110, y=150)

        self.enterid_e.focus()

        #buttons
        self.search_btn= Button(self.left, text="SEARCH",font=('Fuzzco 12 bold'), width=22, height=1, fg='grey25', bg="goldenrod3", command=self.idsearch)
        self.search_btn.place(x=450, y=150)

        self.update = Button(self.left, text="UPDATE", width=22, height=2, bg="goldenrod3", command=self.up)
        self.update.place(x=0, y=80)

        self.add_db = Button(self.left, text="ADD TO DATABSE", width=22, height=2, bg="goldenrod3", command=self.add2db)
        self.add_db.place(x=170, y=80)

        #fill it later by function ajax
        self.productname = Label(self.left, text="", font=('arial 27 bold'), bg="grey25", fg= "skyblue")
        self.productname.place(x=0, y=250)

        self.pprice = Label(self.left, text="", font=('arial 27 bold'), bg="grey25", fg= "skyblue")
        self.pprice.place(x=0, y=290)

        #total Label
        self.total_l = Label(self.right, text="", font=('arial 40 bold'), bg="goldenrod3", fg="grey25")
        self.total_l.place(x=0, y=600)

    def up(self):
        root=Toplevel(self.master)
        root.geometry("1366x768+0+0")
        update=Database(root)

    def add2db(self):
        root=Toplevel(self.master)
        root.geometry("1366x768+0+0")
        add=Add_to_Database(root)
    def exit(self):
        root.destroy()









root = Tk()
b= Application(root)

root.geometry("1366x768+0+0")
root.mainloop()
