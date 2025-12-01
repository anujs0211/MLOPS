class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()
    def menu(self):
        user_input = input("""Welcome to chatbook!How would you like to proceed?
              1. Signup
              2. Signin
              3. write a post
              4. message a friend
              5. press any other key to exit""") 
        if user_input == '1':
            pass
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            print("Thank you for visiting chatbook!")
            exit()
sam = chatbook()