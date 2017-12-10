def hello():
    print('hello world')

def helloName(name=''):
    if (name):
        print('hello {}'.format(name))
    else:
        print('Name is missing.  What is your name?')
