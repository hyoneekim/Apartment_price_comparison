'''
Price comparison of apartments in Seoul, South Korea and Helsinki, Finland
Annual, in EUR, per m^2 2015-2021

Data ref. KOSIS(KOR) / Tilastokeskus(FIN) / European Central Bank (Exchange Rate)
'''
import numpy as np 
import matplotlib.pyplot as plt

helsinki = np.array([4005, 4084, 4284, 4482, 4646, 4845, 5455])
seoul = np.array([5946, 6262, 6493, 6936, 7919, 6711, 9048])
exchange_rate = np.array([1256.54, 1284.18, 1276.74, 1299.07, 1305.32, 1345.58, 1354.06])
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021]

#convert Seoul prices to EUR (1000krw/m^2)
#exchange rate : 1EUR = **** krw

seoul_eur = np.around(seoul*1000/exchange_rate)

def price_chart():
    plt.plot(years,helsinki, label = "Helsinki")
    plt.plot(years,seoul_eur, label = "Seoul")
    plt.axis([2015,2021,4000,6500])
    plt.ylabel("m^2 prices in EUR")
    plt.xlabel("years")
    plt.grid()
    plt.title("Apartment prices in Helsinki and Seoul")
    plt.legend()
    plt.show()

price_gap = seoul_eur/helsinki

def price_difference():
    plt.bar(years, price_gap, align='center', color='skyblue', zorder=3)
    plt.axis([2014,2022,1,1.5])
    plt.grid(zorder=0)
    plt.xlabel("years")
    plt.title("Price comparisons of apartments in Seoul and Helsinki")
    plt.text(2015,1.4,"** when the price in Helsinki is 1", 
        bbox=dict(facecolor='white', alpha=0.5))
    plt.show()

price_chart()
price_difference()