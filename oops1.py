class employee:
    def __init__(self):
        self.id = 123
        self.salary = 10000
        self.designation = 'SDE'

    def travel(self, destintion):
        print(f"Employee is travelling to {destintion}")

sam = employee()
sam.travel('New York')
print(type(sam))