#import tkinter
from tkinter import *
#import random
import random
#import time
import time


costofmeals=0.0
paidtax=0.0
service=0.0
paytax=0.0
ser=0.0
sum=0.0
overall=0.0

def total():
    a1=69*fries.get()
    a2= 99*tikki.get()
    a3= 81*peanut.get()
    a4=90*crisp.get()
    a5=99*tr.get()
    a6=80*ball.get()
    a7=45*crunch.get()
    a8=34*sticks.get()
    a9=79*kinny.get()
    a10=91*gravy.get()
    a11=90*tomato.get()
    a12=99*cream.get()
    a13=67*hot.get()
    a14=50*veg.get()
    a15=69*charap.get()
    a16=91*bread.get()
    a17=60*noodle.get()
    a18=49*maggi.get()
    a19=45*gravy_1.get()
    a20=34*paneer.get()
    a21=79*palte.get()
    a22=91*pear.get()
    a23=90*msala.get()
    a24=99*cheese_dosa.get()
    a25=67*msala_dosa.get()
    a26=64*leg.get()
    a27=89*r.get()
    a28=81*wing.get()
    a29=67*general.get()
    a30=99*g_chic.get()
    a31=90*non.get()
    a32=90*galic.get()
    a33=60*kabab.get()
    a34=79*butter.get()
    a35=71*berry.get()
    a36=78*cola.get()
    a37=99*soda.get()
    a38=97*shake.get()

    global costofmeals,service,ser,sum,paytax,overall,paidtax
    costofmeals="Rs.",str('%.2f'% (a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+a26+a27+a28+a29+a30+a31+a32+a33+a34+a35+a36+a37+a38))
    sum=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+a26+a27+a28+a29+a30+a31+a32+a33+a34+a35+a36+a37+a38
    paytax=((sum)*0.33)
    ser=((a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+a26+a27+a28+a29+a30+a31+a32+a33+a34+a35+a36+a37+a38)/99)
    service="Rs.",str('%.2f'% ser)
    overall="Rs.",str(paytax+sum+ser)
    paidtax="Rs.",str('%.2f'% paytax)

    C.set(costofmeals)
    SIR.set(service)
    T.set(paidtax)
    SUB.set(sum)
    TC.set(overall)
    top.withdraw()
    root.deiconify()



def show():
    global top
    top=Toplevel()

    top.title("Menu")
    top.geometry("1350x700+0+0")
    frame_1 = Frame(top, width=1400, height=700, bg="lightcoral")
    frame_1.place(x=0, y=0)
    ########################################################################################################################

    # labels____________________(top headings)___________________________________________________________________________________________
    top_label = Label(frame_1, text="Menu", bg="lightcoral", fg="black", font=("arial", 30, "bold", "underline"))
    top_label.place(x=490, y=0)

    label_item_1 = Label(frame_1, text="Items", bg="lightcoral", fg="black", font=("arial", 20, "bold", "underline"))
    label_item_1.place(x=50, y=70)

    label_quantity_1 = Label(frame_1, text="Quantity", bg="lightcoral", fg="black",
                             font=("arial", 20, "bold", "underline"))
    label_quantity_1.place(x=200, y=70)

    label_item_2 = Label(frame_1, text="Items", bg="lightcoral", fg="black", font=("arial", 20, "bold", "underline"))
    label_item_2.place(x=400, y=70)

    label_quantity_2 = Label(frame_1, text="Quantity", bg="lightcoral", fg="black",
                             font=("arial", 20, "bold", "underline"))
    label_quantity_2.place(x=600, y=70)

    label_item_3 = Label(frame_1, text="Items", bg="lightcoral", fg="black", font=("arial", 20, "bold", "underline"))
    label_item_3.place(x=800, y=70)

    label_quantity_3 = Label(frame_1, text="Quantity", bg="lightcoral", fg="black",
                             font=("arial", 20, "bold", "underline"))
    label_quantity_3.place(x=1000, y=70)

    ########################################################################################################################

    # labels ( food type  )_______________________________________________________________________________________________________

    l_1 = Label(frame_1, text="Appetizer", bg="lightcoral", fg="black", font=("arial", 15, "bold"))
    l_1.place(x=50, y=110)

    l_2 = Label(frame_1, text="Soups", bg="lightcoral", fg="black", font=("arial", 15, "bold"))
    l_2.place(x=50, y=430)

    l_3 = Label(frame_1, text="Noodles", bg="lightcoral", fg="black", font=("arial", 15, "bold"))
    l_3.place(x=400, y=110)

    l_4 = Label(frame_1, text="Vegi", bg="lightcoral", fg="black", font=("arial", 15, "bold"))
    l_4.place(x=400, y=290)

    l_5 = Label(frame_1, text="dosa", bg="lightcoral", fg="black", font=("arial", 15, "bold"))
    l_5.place(x=400, y=460)

    l_6 = Label(frame_1, text="Drinks", bg="lightcoral", fg="black", font=("arial", 15, "bold"))
    l_6.place(x=800, y=400)

    l_7 = Label(frame_1, text="Chicken", bg="lightcoral", fg="black", font=("arial", 15, "bold"))
    l_7.place(x=800, y=110)

    ########################################################################################################################
    def Rset():
        fries.set(0)
        tikki.set(0)
        peanut.set(0)
        crisp.set(0)
        tr.set(0)
        ball.set(0)
        crunch.set(0)
        sticks.set(0)
        kinny.set(0)
        gravy.set(0)
        tomato.set(0)
        cream.set(0)
        hot.set(0)
        veg.set(0)
        charap.set(0)
        bread.set(0)
        noodle.set(0)
        maggi.set(0)
        gravy_1.set(0)
        paneer.set(0)
        palte.set(0)
        pear.set(0)
        msala.set(0)
        cheese_dosa.set(0)
        msala_dosa.set(0)
        leg.set(0)
        r.set(0)
        wing.set(0)
        general.set(0)
        g_chic.set(0)
        non.set(0)
        galic.set(0)
        kabab.set(0)
        butter.set(0)
        berry.set(0)
        cola.set(0)
        soda.set(0)
        shake.set(0)
     #########################################################################################################################
    # labels( items prizes )_________________________________________________________________________________________________________

    label_14 = Label(frame_1, text="69", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_14.place(x=10, y=140)

    label_15 = Label(frame_1, text="99", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_15.place(x=10, y=170)

    label_16 = Label(frame_1, text="81", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_16.place(x=10, y=200)

    label_17 = Label(frame_1, text="90", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_17.place(x=10, y=230)

    label_18 = Label(frame_1, text="99", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_18.place(x=10, y=260)

    label_19 = Label(frame_1, text="80", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_19.place(x=10, y=290)

    label_20 = Label(frame_1, text="45", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_20.place(x=10, y=320)

    label_21 = Label(frame_1, text="34", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_21.place(x=10, y=350)

    label_22 = Label(frame_1, text="79", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_22.place(x=10, y=380)

    label_23 = Label(frame_1, text="91", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_23.place(x=10, y=410)

    label_24 = Label(frame_1, text="90", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_24.place(x=10, y=455)

    label_25 = Label(frame_1, text="99", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_25.place(x=10, y=480)

    label_26 = Label(frame_1, text="67", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_26.place(x=10, y=510)

    # ____________________________________________________________________________________________________
    label_27 = Label(frame_1, text="50", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_27.place(x=360, y=140)

    label_28 = Label(frame_1, text="69", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_28.place(x=360, y=170)

    label_29 = Label(frame_1, text="91", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_29.place(x=360, y=200)

    label_30 = Label(frame_1, text="60", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_30.place(x=360, y=230)

    label_31 = Label(frame_1, text="49", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_31.place(x=360, y=260)

    label_32 = Label(frame_1, text="45", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_32.place(x=360, y=320)

    label_33 = Label(frame_1, text="34", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_33.place(x=360, y=350)

    label_34 = Label(frame_1, text="79", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_34.place(x=360, y=380)

    label_35 = Label(frame_1, text="91", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_35.place(x=360, y=410)

    label_36 = Label(frame_1, text="90", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_36.place(x=360, y=440)
    #
    label_37 = Label(frame_1, text="99", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_37.place(x=360, y=480)

    label_38 = Label(frame_1, text="67", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_38.place(x=360, y=510)
    # ________________________________________________________________________________________________________________________________________

    label_39 = Label(frame_1, text="64", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_39.place(x=750, y=140)

    label_40 = Label(frame_1, text="89", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_40.place(x=750, y=170)

    label_41 = Label(frame_1, text="81", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_41.place(x=750, y=200)

    label_42 = Label(frame_1, text="67", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_42.place(x=750, y=230)

    label_43 = Label(frame_1, text="99", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_43.place(x=750, y=265)

    label_44 = Label(frame_1, text="90", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_44.place(x=750, y=290)

    label_45 = Label(frame_1, text="90", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_45.place(x=750, y=320)

    label_46 = Label(frame_1, text="60", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_46.place(x=750, y=350)

    label_47 = Label(frame_1, text="79", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_47.place(x=750, y=380)

    label_48 = Label(frame_1, text="71", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_48.place(x=750, y=420)

    label_49 = Label(frame_1, text="78", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_49.place(x=750, y=450)

    label_50 = Label(frame_1, text="99", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_50.place(x=750, y=480)

    label_51 = Label(frame_1, text="97", bg="lightcoral", fg="black", font=("arial", 12, "bold"))
    label_51.place(x=750, y=510)
    ########################################################################################################################

    # _______-_________________string var (entry 1)_____-______--

    # _____________________________entry _____(e1)______________________________________________________________________

    e1 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=fries)
    e1.place(x=200, y=140)

    e2 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=tikki)
    e2.place(x=200, y=170)

    e3 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=peanut)
    e3.place(x=200, y=200)

    e4 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=crisp)
    e4.place(x=200, y=230)

    e5 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=tr)
    e5.place(x=200, y=260)

    e6 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=ball)
    e6.place(x=200, y=290)

    e7 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=crunch)
    e7.place(x=200, y=320)

    e8 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=sticks)
    e8.place(x=200, y=350)

    e9 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=kinny)
    e9.place(x=200, y=380)

    e10 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=gravy)
    e10.place(x=200, y=410)

    e11 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=tomato)
    e11.place(x=200, y=450)

    e12 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=cream)
    e12.place(x=200, y=480)

    e13 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=hot)
    e13.place(x=200, y=510)
    # ___________________-string var__(entry 2)___________________________________________________________

    # ________________________________________________e(2)___________________________________________

    e14 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=veg)
    e14.place(x=600, y=140)

    e15 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=charap)
    e15.place(x=600, y=170)

    e16 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=bread)
    e16.place(x=600, y=200)

    e17 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=noodle)
    e17.place(x=600, y=230)

    e18 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=maggi)
    e18.place(x=600, y=260)

    e19 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=gravy_1)
    e19.place(x=600, y=320)

    e20 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=paneer)
    e20.place(x=600, y=350)

    e21 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=palte)
    e21.place(x=600, y=380)

    e22 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=pear)
    e22.place(x=600, y=410)

    e24 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=msala)
    e24.place(x=600, y=440)

    e25 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=cheese_dosa)
    e25.place(x=600, y=480)

    e26 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=msala_dosa)
    e26.place(x=600, y=510)

    # +______________________stringvar (e3)_____________________________________________________________________________


    # _________________________________________e(3)__________________________________________________
    e27 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=leg)
    e27.place(x=1000, y=140)

    e28 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=r)
    e28.place(x=1000, y=170)

    e29 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=wing)
    e29.place(x=1000, y=200)

    e30 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=general)
    e30.place(x=1000, y=230)

    e31 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=g_chic)
    e31.place(x=1000, y=265)

    e32 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=non)
    e32.place(x=1000, y=290)

    e33 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=galic)
    e33.place(x=1000, y=320)

    e34 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=kabab)
    e34.place(x=1000, y=350)

    e35 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=butter)
    e35.place(x=1000, y=380)

    e36 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=cola)
    e36.place(x=1000, y=420)

    e37 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=berry)
    e37.place(x=1000, y=450)

    e38 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=soda)
    e38.place(x=1000, y=480)

    e39 = Entry(frame_1, bd=1, bg="lavenderblush", textvariable=shake)
    e39.place(x=1000, y=510)
    ########################################################################################################################

    # -------------------------------item names_________________________________________________________________________
    name1 = Label(frame_1, text="kivi fries", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    name1.place(x=35, y=140)

    name2 = Label(frame_1, text="alo tikki", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    name2.place(x=35, y=170)
    #
    name3 = Label(frame_1, text="garlic peanut", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    name3.place(x=35, y=200)

    name4 = Label(frame_1, text="crisp salad", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    name4.place(x=35, y=230)

    name5 = Label(frame_1, text="squidhead", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    name5.place(x=35, y=260)

    name6 = Label(frame_1, text="squid ball", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    name6.place(x=35, y=290)

    name7 = Label(frame_1, text="cheese crunch", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    name7.place(x=35, y=320)

    name8 = Label(frame_1, text="cheese sticks", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    name8.place(x=35, y=350)

    name9 = Label(frame_1, text="kinny fries", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    name9.place(x=35, y=380)

    name10 = Label(frame_1, text="gravy mushroom", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    name10.place(x=35, y=410)

    name11 = Label(frame_1, text="tomato soup", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    name11.place(x=35, y=455)

    name12 = Label(frame_1, text="cream of com", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    name12.place(x=35, y=480)

    name13 = Label(frame_1, text="hototay soup", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    name13.place(x=35, y=510)
    # _______________________________________________________________________________________________________

    n14 = Label(frame_1, text="veg noodles", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n14.place(x=400, y=140)

    n15 = Label(frame_1, text="extra charap", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n15.place(x=400, y=170)

    n16 = Label(frame_1, text="roasted bread", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n16.place(x=400, y=200)

    n17 = Label(frame_1, text="cheese noodle", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n17.place(x=400, y=230)

    n18 = Label(frame_1, text="msala maggi ", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n18.place(x=400, y=260)

    # ___
    n19 = Label(frame_1, text="paneer gravy", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n19.place(x=400, y=320)

    n20 = Label(frame_1, text="palak paneer", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n20.place(x=400, y=350)

    n21 = Label(frame_1, text="mix veg palte", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n21.place(x=400, y=380)

    n22 = Label(frame_1, text="pear mix vegi", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n22.place(x=400, y=410)

    n23 = Label(frame_1, text="vegetable mix msala", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n23.place(x=400, y=440)

    n25 = Label(frame_1, text="cheese dosa", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n25.place(x=400, y=485)

    n26 = Label(frame_1, text="msala dosa", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n26.place(x=400, y=510)

    n27 = Label(frame_1, text="chicken leg", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n27.place(x=800, y=140)

    n28 = Label(frame_1, text="Roast", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n28.place(x=800, y=170)

    n29 = Label(frame_1, text="fried wings", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n29.place(x=800, y=200)

    n30 = Label(frame_1, text="general chickens", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n30.place(x=800, y=230)

    n31 = Label(frame_1, text="gravy chicken", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n31.place(x=800, y=265)

    n32 = Label(frame_1, text="non veg mix", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n32.place(x=800, y=290)

    n33 = Label(frame_1, text="galic chicken", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n33.place(x=800, y=320)

    n34 = Label(frame_1, text="roast kabab", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n34.place(x=800, y=350)

    n35 = Label(frame_1, text="butter chicken", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n35.place(x=800, y=380)

    n36 = Label(frame_1, text="coca cola", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n36.place(x=800, y=422)

    n37 = Label(frame_1, text="strawberry shake", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n37.place(x=800, y=450)

    n38 = Label(frame_1, text="msala soda", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n38.place(x=800, y=480)

    n39 = Label(frame_1, text="mixed fruit shake", bg="lightcoral", fg="white", font=("arial", 12, "bold"))
    n39.place(x=800, y=510)

    ########################################################################################################################
    reset = Button(frame_1, text="Reset", bg="seashell", font=("arial", 20, "bold"), fg="black", width=10, height=1,
                   bd=1,command=Rset)
    reset.place(x=200, y=600)

    Total = Button(frame_1, text="Total", bg="seashell", font=("arial", 20, "bold"), fg="black", width=10, height=1,
                   bd=1,command=total)
    Total.place(x=600, y=600)

    back = Button(frame_1, text="Go To Counter", bg="seashell", font=("arial", 20, "bold"), fg="black", width=15,
                  height=1, bd=1, command=display)
    back.place(x=1000, y=600)

    root.withdraw()
    mainloop()


def display():
    top.withdraw()
    root.deiconify()
root=Tk()

root.title("Menu")
root.geometry("1350x700+0+0")



veg = IntVar()
charap = IntVar()
bread = IntVar()
noodle = IntVar()
maggi = IntVar()
gravy_1 = IntVar()
paneer = IntVar()
palte = IntVar()
pear = IntVar()
msala = IntVar()
cheese_dosa = IntVar()
msala_dosa = IntVar()

leg = IntVar()
r = IntVar()
wing = IntVar()
general = IntVar()
g_chic = IntVar()
non = IntVar()
galic = IntVar()
kabab = IntVar()
butter = IntVar()
berry = IntVar()
cola = IntVar()
soda = IntVar()
shake = IntVar()

fries = IntVar()
tikki = IntVar()
peanut = IntVar()
crisp = IntVar()
tr = IntVar()
ball = IntVar()
crunch = IntVar()
sticks = IntVar()
kinny = IntVar()
gravy = IntVar()
tomato = IntVar()
cream = IntVar()
hot = IntVar()

f1=Frame(root,width=1400,height=100,relief=SUNKEN)
f1.pack(side=TOP)

frame_2=Frame(root,bg="lightcoral",width=1400,height=680,relief=SUNKEN)
frame_2.pack(side=LEFT)

frame1 = Frame(root,width=300,height=800,bg="cornflowerblue")
# split=0.3
frame1.place(x=0,y=100)



########################################################################################################################
label_1=Label(root,text="Restauro",font=("arial",60,'bold','italic'),fg='black')
label_1.place(x=110,y=0)

canvas=Canvas(root,width=450,height=100,bd=3,bg="pink")
canvas.place(x=480,y=0)
my_image=PhotoImage(file='pictures\download.png')
canvas.create_image(0,0,anchor=NW,image=my_image)

#label number two
label_2=Label(root,text="System",font=("arial",60,'bold','italic'),fg="black")
label_2.place(x=950,y=0)
########################################################################################################################
label=Label(frame_2,text='Order No.',font=('arial',20,"bold"),fg="white",bg="lightcoral")
label.place(x=300,y=50)


label_0=Label(frame_2,text='Cost of Meals',font=('arial',20,"bold"),fg="white",bg="lightcoral")
label_0.place(x=300,y=120)


label_1=Label(frame_2,text='Service Charges',font=('arial',20,"bold"),fg="white",bg="lightcoral")
label_1.place(x=300,y=190)

label_2=Label(frame_2,text='Tax',font=('arial',20,"bold"),fg="white",bg="lightcoral")
label_2.place(x=300,y=260)


label_3=Label(frame_2,text='Sub Total',font=('arial',20,"bold"),fg="white",bg="lightcoral")
label_3.place(x=300,y=330)

label_4=Label(frame_2,text='Total Cost',font=('arial',20,"bold"),fg="white",bg="lightcoral")
label_4.place(x=300,y=400)

rand=StringVar()
C=StringVar()
SIR=StringVar()
T=StringVar()
SUB=StringVar()
TC=StringVar()

e1=Entry(frame_2,font=('arial',20,"bold"),width=20,bd=1,textvariable=rand,insertwidth=3)
e1.place(x=570,y=50)

e2=Entry(frame_2,font=('arial',20,"bold"),width=20,bd=1,textvariable=C)
e2.place(x=570,y=120)

e3=Entry(frame_2,font=('arial',20,"bold"),width=20,bd=1,textvariable=SIR)
e3.place(x=570,y=190)

e4=Entry(frame_2,font=('arial',20,"bold"),width=20,bd=1,textvariable=T)
e4.place(x=570,y=260)

e4=Entry(frame_2,font=('arial',20,"bold"),width=20,bd=1,textvariable=SUB)
e4.place(x=570,y=330)


e5=Entry(frame_2,font=('arial',20,"bold"),width=20,bd=1,textvariable=TC)
e5.place(x=570,y=400)

########################################################################################################################

text_input=StringVar()
text_display=Entry(frame1,font=("black",15),textvariable=text_input,bd=2,bg="white",width=25,justify="left").grid(columnspan=4)
#--------------------------------------function definations------------------------------------------------------------------------------------------
#function defination here (clear)
def btnClear():
    global operator
    operator=""
    text_input.set(operator)

#function defination here (click)
def btnClick (numbers):
 global operator
 operator = operator+str(numbers)
 text_input.set(operator)

# function defination (equal function)
def btnEquals():
     global operator
     sumup = str(eval(operator))
     text_input.set(sumup)
     operator = ""
#--------------------------------------buttons in calculator------------------------------------------------------------------------------------------

#button 7
button7 = Button(frame1,bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='7',command=lambda:btnClick(7))
button7.grid(row=1,column=0)
#botton 8
button8 = Button(frame1,bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='8',command=lambda:btnClick(8))
button8.grid(row=1,column=1)
#botton 9
button9 = Button(frame1,bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='9',command=lambda:btnClick(9))
button9.grid(row=1,column=2)
#botton add
buttonAdd=Button(frame1,bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='+',command=lambda:btnClick("+"))
buttonAdd.grid(row=1,column=3)
#botton 4
button4 = Button(frame1 , bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='4',command=lambda:btnClick(4))
button4.grid(row=2,column=0)
#botton 5
button5 = Button(frame1,bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='5',command=lambda:btnClick(5))
button5.grid(row=2,column=1)
#botton 6
button6 = Button(frame1,bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='6',command=lambda:btnClick(6))
button6.grid(row=2,column=2)
#botton -
buttonSub = Button(frame1,bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='-',command=lambda:btnClick("-"))
buttonSub.grid(row=2,column=3)
#botton 1
button1=Button(frame1,bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='1',command=lambda:btnClick(1))
button1.grid(row=3,column=0)
#botton 2
button2=Button(frame1,bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='2',command=lambda:btnClick(2))
button2.grid(row=3,column=1)
#botton 3
button3=Button(frame1,bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='3',command=lambda:btnClick(3))
button3.grid(row=3,column=2)
#botton *
buttonMul=Button(frame1,bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='*',command=lambda:btnClick("*"))
buttonMul.grid(row=3,column=3)
#botton 0
button0=Button(frame1,bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='0',command=lambda:btnClick(0))
button0.grid(row=4,column=0)
#botton clr
buttonClr=Button(frame1,bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='clr',command=btnClear)
buttonClr.grid(row=4,column=1)
#botton equ
buttonEqu=Button(frame1,bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='=',command=btnEquals)
buttonEqu.grid(row=4,column=2)
#botton /
buttonDiv=Button(frame1,bg="white",padx=20,pady=20,bd=1,fg="black",width=2,font=("arial",15,"bold"),text='/',command=lambda:btnClick("/"))
buttonDiv.grid(row=4,column=3)
########################################################################################################################
def Ref():
    x=random.randint(100,220)
    randomRef=str(x)
    rand.set(randomRef)

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    C.set("")
    SIR.set("")
    T.set("")
    SUB.set("")
    TC.set("")
########################################################################################################################
ButtonCOUNT=Button(frame_2,text="Order No",bg="seashell",font=("arial",20,"bold"),fg="black",width=10,height=1,bd=1,command=Ref)
ButtonCOUNT.place(x=300,y=500)

buttonRESET=Button(frame_2,text="Reset",bg="seashell",font=("arial",20,"bold"),fg="black",width=10,height=1,bd=1,command=Reset)
buttonRESET.place(x=500,y=500)

buttonMENU=Button(frame_2,text="MENU",bg="white",font=("arial",20,"bold"),fg="black",width=10,height=1,bd=1,command=show)
buttonMENU.place(x=700,y=500)

buttonEXIT=Button(frame_2,text="EXIT",bg="red",font=("arial",20,"bold"),fg="white",width=10,height=1,bd=1,command=qExit)
buttonEXIT.place(x=900,y=500)


########################################################################################################################
t=time.asctime()

#l=Label(root,text='TIME',font=('arial',20,"bold",'underline'),fg="black",bg="lightcoral")
#l.place(x=950, y=100)
frame_time = Frame(root, width=500, height=300, bg="lightcoral",bd="5")
frame_time.place(x=950, y=100)

l0=Label(frame_time,text=t,font=('arial',17,"bold"),fg="black",bg="white",bd="5")
l0.place(x=0,y=0)

root.mainloop()