import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

data = pd.read_csv("mental_health.csv")
data.head()

data.isna().sum()

data.info()

plt.figure(figsize=(10, 6))
df['Country'].value_counts().head(10).plot.bar()
plt.title('Top 10 Countries by Respondents')
plt.xlabel('Country')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(12, 8))
sns.countplot(data=df, x='Gender', hue='mental_health_consequence')
plt.title('Mental Health Consequences by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Mental Health Consequence')
plt.show()

plt.figure(figsize=(12, 8))
sns.countplot(data=df, x='Gender', hue='seek_help')
plt.title('Seek Help by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Seek Help')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Age', hue='treatment')
plt.title('Age vs Treatment')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()