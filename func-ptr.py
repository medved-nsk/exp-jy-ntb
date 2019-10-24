# Simple function
def greeting(name):
        print('Halo,', name)

        # Class with pointer to function
        class Greeter:
                def __init__(self, a_greeting):
                            self.a_greeting = a_greeting
                                    
g = Greeter(greeting)
g.a_greeting('Joe')

# List of instances
greeters = [
        { 'g': Greeter(greeting), 'name': 'Gans' }
]

greeters[0]['g'].a_greeting(greeters[0]['name'])
