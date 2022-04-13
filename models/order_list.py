from models.order import *
import datetime

order1 = Order("Charles Avery", datetime.date(2021, 8, 1), 4, "Potions", 4.99 )
order2 = Order("Kenneth Burgondy", datetime.date(2022, 2, 11), 1, "Moonstones", 14.00)
order3= Order("Hissy Tellpots", datetime.date(2022, 1, 26), 5, "Great Balls", 20.00)
orders = [order1, order2, order3]