le = LabelEncoder()
encode_cols = [
    'Gender', 'Country', 'self_employed', 'family_history', 'treatment', 
    'work_interfere', 'no_employees', 'remote_work', 'tech_company', 
    'benefits', 'care_options', 'wellness_program', 'seek_help', 
    'anonymity', 'leave', 'mental_health_consequence', 
    'phys_health_consequence', 'coworkers', 'supervisor', 
    'mental_health_interview', 'phys_health_interview', 
    'mental_vs_physical', 'obs_consequence'
]

for column in encode_cols:
    df[column] = le.fit_transform(df[column])

x = df.drop('treatment', axis = 1)
x.head()

y = df[['treatment']]
y.head()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

model = LogisticRegression(random_state = 0)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
y_pred

print("Training Accuracy :", model.score(x_train, y_train))
print("Testing Accuracy :", model.score(x_test, y_test))

print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
pd.DataFrame(cm, index = ['Actual No', 'Actual Yes'], columns = ['Predicted No', 'Predicted Yes'])

plt.figure(figsize = (8,6))
sns.heatmap(cm, annot = True, fmt = 'd', cmap = 'Blues')
plt.title("Confusion Matrix")
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()