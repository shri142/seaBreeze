import pickle

with open('forcasting_model.pickle', 'rb') as file:
    loaded_code = pickle.load(file)

exec(loaded_code)