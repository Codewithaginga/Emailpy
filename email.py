print('check your email')
class Currency:

    @staticmethod
    def pound_to_shillings():

        dollar = int(input('Enter amount: '))

        kenya_shillings = dollar * 119

        print(f'{kenya_shillings:,} shillings')

    @staticmethod
    def euro_shillings():
        euro = float(input('Enter Amount: '))
        shilling = euro * 104.4
        print(f'{shilling:,} shillings')


c = Currency()
c.pound_to_shillings()



