import numpy as pd
import pandas as pd
from tensorflow import keras
import numpy as np

model= keras.models.load_model('model.h5')

def predict(df):
    real_data= np.array(df[["High","Low","Open","Volume","Adj Close"]])
    real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1],1))
    predictions = model.predict(real_data)
    return predictions.flatten().tolist()