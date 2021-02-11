from random import choice
from user import User
from region import Region
from estate import Apartment, House, Store
from advertisement import ApartmentSell, HouseSell, ApartmentRent, HouseRent, StoreSell, StoreRent

FIRST_NAME = ['Zahra', 'Alireza', 'Fatemeh']
LAST_NAME = ['Razavi', 'Jamshidi', 'Malayeri']
PHONE_NUMBER = ['09124567685', '09125783957', '09125780375', '09126893469', '09126849768']


def create_samples():

    for mobile in PHONE_NUMBER:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    reg1 = Region('reg1')

    apartment = Apartment(has_elevator=True, has_parking=True, floor=5,
                          user=User.object_list[0], area=400, rooms_count=4,
                          built_year=1380, region=reg1, address='some address')

    house = House(has_yard=True, floors_count=2, user=User.object_list[-1],
                  area=800, rooms_count=5, built_year=1378, region=reg1,
                  address='some address..')

    store = Store(user=User.object_list, area=400, rooms_count=0,
                  built_year=1387, region=reg1, address='some address...')

    apartment_sell = ApartmentSell(has_elevator=True, has_parking=True, floor=5,
                                   user=User.object_list[0], area=400, rooms_count=4,
                                   built_year=1380, region=reg1, address='some address',
                                   price_per_meter=10, discountable=True, convertable=True)

    house_sell = HouseSell(has_yard=True, floors_count=2, user=User.object_list[-1],
                           area=800, rooms_count=5, built_year=1378, region=reg1,
                           address='some address..', price_per_meter=20, discountable=False, convertable=True)

    apartment_rent = ApartmentRent(has_elevator=True, has_parking=True, floor=5,
                                   user=User.object_list[0], area=400, rooms_count=4,
                                   built_year=1380, region=reg1, address='some address', initial_price=100,
                                   monthly_price=3.5, discountable=False, convertable=False)

    house_rent1 = HouseRent(has_yard=True, floors_count=2, user=User.object_list[-1],
                            area=800, rooms_count=5, built_year=1378, region=reg1,
                            address='some address..', initial_price=150,
                            monthly_price=5.5, discountable=False, convertable=False)

    house_rent2 = HouseRent(has_yard=True, floors_count=2, user=User.object_list[-1],
                            area=1000, rooms_count=5, built_year=1378, region=reg1,
                            address='some address..', initial_price=150,
                            monthly_price=5.5, discountable=False, convertable=False)

    store_sell = StoreSell(user=User.object_list, area=400, rooms_count=0,
                           built_year=1387, region=reg1, address='some address...',
                           price_per_meter=50, discountable=False, convertable=True)

    store_rent = StoreRent(user=User.object_list, area=400, rooms_count=0,
                           built_year=1387, region=reg1, address='some address...',
                           initial_price=150, monthly_price=5.5, discountable=False,
                           convertable=False)
    print("#" * 20, "\t samples created \t", "#" * 20)