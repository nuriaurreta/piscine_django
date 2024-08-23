class Intern:
    def __init__(self, Name = "My name? I'm nobody, an intern, I have no name."):
        self.Name = Name
    
    def __str__(self):
        return self.Name
    
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
    
    def work(self):
        raise Exception("I'm just an intern, I can't do that...")
    
    def make_coffee(self):
        my_coffee = self.Coffee()
        return my_coffee.__str__()
    
if __name__ == '__main__':
    
    def test_intern():
        intern1 = Intern()
        print("Intern 1 Name:", intern1)  # "My name? I'm nobody, an intern, I have no name."

        intern2 = Intern("Mark")
        print("Intern 2 Name:", intern2)  # "Mark"

        coffee = intern2.make_coffee()
        print("Coffee made by Mark:", coffee)  # "This is the worst coffee you ever tasted."

        try:
            intern1.work()
        except Exception as e:
            print("Exception caught:", e)  # "I'm just an intern, I can't do that..."

    test_intern()