from datetime import datetime
import time

def logger(func):
    def wrapper(*args, **kwargs):
        print('-'*50)
        print('> Execution started {}'.format(datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
        func(*args, **kwargs)
        print('> Execution ended {}'.format(datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
        print('-'*50)

    return wrapper

@logger
def demo_function(sleep_time):
    print('Excecuting task!')
    time.sleep(sleep_time)
    print('Task completed!')


# diffrent way to call the function

demo_function(1)
demo_function(2)

# or

logger(demo_function(3))
