from random import choice
from user import User
from region import Region
from estate import Apartment, House, Store
from advertisement import ApartmentSell, HouseSell, ApartmentRent, HouseRent

FIRST_NAME = ['Zahra', 'Alireza', 'Fatemeh']
LAST_NAME = ['Razavi', 'Jamshidi', 'Malayeri']
PHONE_NUMBER = ['09124567685', '09125783957', '09125780375', '09126893469', '09126849768']
if __name__ == "__main__":
    for mobile in PHONE_NUMBER:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    for user in User.object_list:
        print(f'{user.id}, {user.fullname}')

    reg1 = Region('reg1')

    apt1 = Apartment(has_elevator=True, has_parking=True, floor=5,
                     user=User.object_list[0], area=400, rooms_count=4,
                     built_year=1380, region=reg1, address='some address')
    # apt1.show_description()

    house = House(has_yard=True, floors_count=2, user=User.object_list[-1],
                  area=800, rooms_count=5, built_year=1378, region=reg1,
                  address='some address..')
    # house.show_description()

    store = Store(user=User.object_list, area=400, rooms_count=0,
                  built_year=1387, region=reg1, address='some address...')
    # store.show_description()

    apartment_sell = ApartmentSell(has_elevator=True, has_parking=True, floor=5,
                                   user=User.object_list[0], area=400, rooms_count=4,
                                   built_year=1380, region=reg1, address='some address',
                                   price_per_meter=10, discountable=True, convertable=True)
    apartment_sell.show_detail()
    apartment_sell.show_description()

    house_sell = HouseSell(has_yard=True, floors_count=2, user=User.object_list[-1],
                           area=800, rooms_count=5, built_year=1378, region=reg1,
                           address='some address..', price_per_meter=20, discountable=False, convertable=True)
    house_sell.show_detail()
    house_sell.show_description()

    # print(ApartmentSell.object_list)
    # print(HouseSell.object_list)
    # print(User.object_list)

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

    # print(house_rent.manager.search(area=800))
    # print(ApartmentRent.manager.search(region=reg1))
    print(HouseRent.manager.search(area__max=800, area__min=600))
