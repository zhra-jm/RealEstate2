from advertisement import ApartmentSell, HouseSell, ApartmentRent, HouseRent, StoreSell, StoreRent
from sample import create_samples


class Handler:
    ADVERTISEMENT_TYPE = {
        1: ApartmentSell, 2: ApartmentRent,
        3: HouseSell, 4: HouseRent,
        5: StoreSell, 6: StoreRent
    }

    SWITCHES = {
        'r': 'get_report',
        's': 'show_all'
    }

    def show_all(self):
        for adv in self.ADVERTISEMENT_TYPE.values():
            for obj in adv.object_list:
                print(obj.show_detail())

    def get_report(self):
        for adv in self.ADVERTISEMENT_TYPE.values():
            print(adv, adv.manager.count())

    def run(self):
        print('hello world')
        for key in self.SWITCHES:
            print(f'press {key} for {self.SWITCHES[key]}')
            user_input = input('Enter your choice: ')
            switch = self.SWITCHES.get(user_input, None)
            if switch is None:
                print('invalid input')
                self.run()
            choice = getattr(self, switch, None)
            choice()
            self.run()


if __name__ == "__main__":
    create_samples()
    Handler().run()
