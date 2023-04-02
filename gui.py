import tkinter as tk
import pandas as pd

# Load the submission file
submission = pd.read_csv("C:\\Users\\bhavy\\Downloads\\cluster_labels.csv")
def predict_res(id):
    id = int(id)
    return "Cluster "+str(submission.iloc[id][1])

# Define a function to get the prediction value for a given ID
def get_prediction():
    # Get the ID from the input field
    id = int(id_input.get())

    # Get the prediction value for the corresponding ID
    prediction = predict_res(id)

    # Update the output label with the prediction value
    output_label.config(text=f'Prediction value for ID is {id} : {prediction}')


# Create the main window
root = tk.Tk()
root.title('Unsupervised Clustering Prediction')

# Create input field and label
id_label = tk.Label(root, text='Enter ID:')
id_label.pack()
id_input = tk.Entry(root)
id_input.pack()

# Create button to get prediction value
get_prediction_button = tk.Button(root, text='Get Prediction', command=get_prediction)
get_prediction_button.pack()

# Create output label
output_label = tk.Label(root, text='')
output_label.pack()

# Start the main loop
root.mainloop()