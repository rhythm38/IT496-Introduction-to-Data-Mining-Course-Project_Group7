import uvicorn
import pickle
from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def index():
    return {'WELCOME TO ICC WORLDCUP PREDICTION!!'}

@app.get("/Top 6 Bowlers of INDIA!!")
def read_root():
    # Load the stored output from the pickle file
    with open('output3.pkl', 'rb') as output_file:
        stored_output = pickle.load(output_file)

    return stored_output

@app.get("/Prediction of 11 Players for INDIA!!")
def read_root():
    # Load the stored output from the pickle file
    with open('output4.pkl', 'rb') as output_file:
        stored_output = pickle.load(output_file)

    return stored_output


# Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)