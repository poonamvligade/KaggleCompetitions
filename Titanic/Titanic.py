 Titanic competition on Kaggle to predict survival of passangers onboard

#Read data in
import pandas as pd
raw_df=pd.read_csv("train.csv")
raw_df.head()


raw_df.count()

# Above count shows there are missing values in age, cabin and embarked.
# U need to replace the null values with the median age which is more robust to outliers than the mean.



raw_df['Age'].fillna(raw_df['Age'].median(), inplace=True)



raw_df.describe()  # numerical features of data



raw_df["Age"].head()
