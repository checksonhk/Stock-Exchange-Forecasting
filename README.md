# Stock-Exchange-Forecasting
A few projects related to Stock Exchange

There are currently two projects on this repository.

* A Jupyter Notebook on comparing traditional time-series forecasting with newer Deep Learning models.

* A Q Learning approach to Day Trading 

### **How to run**
**To train a Deep Q agent**, run python run.py --mode train. There are also other parameters which you may find in the run.py script. After training, a trained model as well as the portfolio value history at every episode is saved.  

**To test the model performance**, run python run.py --mode test --weights <trained_model>, where <trained_model> points to the local model weights file.
