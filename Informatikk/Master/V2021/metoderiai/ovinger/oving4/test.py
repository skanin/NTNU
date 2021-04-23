import pandas as pd

train = pd.read_csv('titanic/train.csv')
test = pd.read_csv('titanic/test.csv')

# print(len(sorted(train['Age'].unique())))
# print(train[train['Age'] == 0.17])

# print(train[train['Sex'] == 'male'])
# print(train[train['Sex'] == 'female'])

res = pd.read_csv('aima-data/restaurant.csv')

def foo(key, value):
    return len(res.loc[res[key] == value])

def bar(key, value):
    return len(res.loc[(res[key] == value) & (res['WillWait'] == 'Yes')]), len(res.loc[(res[key] == value) & (res['WillWait'] == 'No')])

# for key in res.columns:
#     if key == 'WillWait':
#         continue
#     df = res.groupby('WillWait')[key].value_counts()
#     print(df)
#     for value in res[key].unique():
#         print(df[df[key] == value])
#     print()
#     print('--------------------------------------------------------------------------------')

# df = res.groupby('WillWait')['Patrons'].value_counts()#.unstack(fill_value=0).stack()
# print(df)

# train1 = train.groupby('Survived')['Embarked'].value_counts().unstack(fill_value=0).stack()
# print(train1)

# for sex in ['female']:
#     for clas in [3,1,2]:
#         for em in ['S', 'C', 'Q']:
#             print(f'{sex} - {clas} - {em}')
#             print(train[(train['Sex'] == sex) & (train['Pclass'] == clas) & (train['Embarked'] == em)]['Survived'].value_counts())
# pd.set_option('display.max_columns', None)
# print(res[(res['Patrons'] == 'Full') & (res['Hungry'] == 'Yes')])

# print(train[(train['Sex'] == 'female') & (train['SibSp'] <= 0)]['Survived'].value_counts())
# print(train[train['SibSp'] <= 0])
# print(test[(test['Sex'] == 'female') & (test['SibSp'] < 5) & (test['Parch'] < 4) & (test['Pclass'] == 1) & (test['Embarked'] == 'C')]['Survived'].value_counts())

# print(train[(train['Age'] <= 3) & (train['SibSp'] <= 5) & (train['Pclass'] == 2) & (train['Sex'] == 'male') & (train['Parch'] <= 1)]['Survived'].value_counts())

print(train[train['Age'].isna()]['Age'])