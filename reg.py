import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('Housing.csv')

X = df[['area', 'bedrooms', 'bathrooms', 'stories', 'parking']]
y=df['price']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(X,y)
y_pred=model.predict(X_test)
r2=r2_score(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)

print('House Price Predictor')
print('Model trained successfully on Housing.csv\n')
print(f"R-squared score (Model fit): {r2*100:.1f}%")
print(f"Mean absolute error: ${mae:,.2f}\n")

while True:
    user_in=input("Enter area,bedrooms, bathrooms, stories and parking seperated by commas or 'q' to quit:")
    if user_in.lower()=='q':
        print('end of program')
        break
    data=user_in.split(',')
    area_val=float(data[0])
    bed_val=float(data[1])
    bath_val=float(data[2])
    story_val=float(data[3])
    park_val=float(data[4])

    predicton=model.predict([[area_val,bed_val,bath_val,story_val,park_val]])[0]
    print(f"PREDICTED HOUSE PRICE: ${predicton:,.2f}\n")