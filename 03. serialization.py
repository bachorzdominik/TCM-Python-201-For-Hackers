import pickle
import os

hackers = {"neut": 1, "goehot": 100, "neo": 1000}

for key, value in hackers.items():
    print(key, value)
print()

seralized = pickle.dumps(hackers)
print(seralized)
print()

deserialized = pickle.loads(seralized)
print(deserialized)
print()

if not os.path.exists('files'):
    os.makedirs('files')

if not os.path.exists('files/hackers.pickle'):
    try:
        with open('files/hackers.pickle', 'wb') as handle:
            pickle.dump(hackers, handle)
    except Exception as e:
        print(e)
        print('Error writing file')
else:
    try:
        with open('files/hackers.pickle', 'rb') as handle:
            hackers_v1 = pickle.load(handle)
            print(hackers_v1)
            print()
            for key, value in hackers_v1.items():
                print(key, value)
    except Exception as e:
        print(e)
        print('Error reading file')
