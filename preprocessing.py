df = data.drop(columns=['state', 'Timestamp', 'comments'])
df.head()

df['Age'] = df['Age'].replace({99999999999: np.nan, -29: np.nan, -1726: np.nan, -1: np.nan, 329: np.nan})
df['Age'] = df['Age'].fillna(method='ffill')
df['Age'] = df['Age'].astype(int)

brain_reset = {
    'Male': 'Male', 'M': 'Male', 'male': 'Male', 'Cis Male': 'Male', 'Male (CIS)': 'Male', 'Male ': 'Male', 'Man': 'Male', 'msle': 'Male', 'Mal': 'Male', 'maile': 'Male', 'Make': 'Male', 'Malr': 'Male',
    'Female': 'Female', 'female': 'Female', 'F': 'Female', 'woman': 'Female', 'femail': 'Female', 'Femake': 'Female', 'Cis Female': 'Female', 'Female ': 'Female', 'Female (cis)': 'Female', 'Female (trans)': 'Female',
    'm': 'Male', 'Male-ish': 'Male', 'Trans-female': 'Female', 'something kinda male?': 'Male', 'Woman': 'Female', 'f': 'Female', 'queer/she/they': 'Female', 'non-binary': 'Male', 'Nah': 'Female', 'All': 'Female', 'Enby': 'Male', 'fluid': 'Female', 'Genderqueer': 'Female', 'Androgyne': 'Male', 'Agender': 'Male', 'cis-female/femme': 'Female', 'Guy (-ish) ^_^': 'Male', 'male leaning androgynous': 'Male', 'Trans woman': 'Female', 'Neuter': 'Male', 'queer': 'Female', 'Mail': 'Male', 'cis male': 'Male', 'A little about you': 'Female', 'p': 'Female', 'Cis Man': 'Male', 'ostensibly male, unsure what that really means': 'Male'
}
df['Gender'] = df['Gender'].replace(brain_reset)

mode = df['self_employed'].mode()[0]
df['self_employed'].fillna(mode, inplace=True)

df['work_interfere'] = df['work_interfere'].ffill()

df['num_employees'] = df['no_employees'].str.extract('(\d+)')
df['num_employees'] = df['num_employees'].astype(int)
df.head()

df.drop(columns=['no_employees'])