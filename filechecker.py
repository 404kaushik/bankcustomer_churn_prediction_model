import pickle

# Replace 'your_file.pkl' with the path to your .pkl file
file_path = 'knn_model.pkl'

# Load the .pkl file
with open(file_path, 'rb') as file:
    data = pickle.load(file)

# Print the loaded data
print(data)
