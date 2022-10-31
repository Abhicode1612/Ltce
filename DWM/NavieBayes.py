# pip install -U scikit-learn

from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB

weather =['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy'] 
temp =['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild'] 
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

le = preprocessing.LabelEncoder()

weather_encoded = le.fit_transform(weather)
temp_encoded = le.fit_transform(temp)
play_encoded = le.fit_transform(play)

features = [tup for tup in zip(weather_encoded, temp_encoded)]
print(features)

model = GaussianNB()

model.fit(features,play)

predicted = model.predict([[0, 2]])
print("Predicted value: ", predicted)