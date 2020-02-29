from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from timeit import default_timer as timer
le = preprocessing.LabelEncoder()
start = timer()
weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

weather_encoded = le.fit_transform(weather)
temp_encoded = le.fit_transform(temp)
play_encoded = le.fit_transform(play)
print(weather_encoded)
print(temp_encoded)

feature = list(zip(weather_encoded, temp_encoded))

model = GaussianNB()
model.fit(feature, play_encoded)

predictid = model.predict([[1, 1]])


print(timer() - start)

print(predictid)