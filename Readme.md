This is a Simple Spam Detection Project with an Interface. This project uses data from :
https://www.kaggle.com/datasets/shantanudhakadd/email-spam-detection-dataset-classification
You can download it to train your model.

The data is imbalanced and the model is trained using LogisticRegression.

The model trained is not shared on github but the model training script can be found in notebooks/1-san-data-model-exploration. Use the script and save the model at your desired destination(need to change in script). Install the requirements first.

- pip install -r requirements.txt

The main runner script can be found inside app/app.py

To run the app:

- cd app
- flask --app app.py run 

The flask app should run at port 5000 as default localhost.

If you want to change the host from default localhost, 

flask --app app.py run --host=0.0.0.0
