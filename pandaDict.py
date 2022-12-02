import pandas as pd
account_info = pd.DataFrame({
    "name": ['Bob', 'Mary', 'Mita'],
    "account": [12345, 123524, 345623],
    "balance": [123, 3972, 7209]
})
# print(account_info)
# print(account_info[['name', 'balance']])

print(account_info.iloc[1])

print(account_info.iloc[0:2])

print(account_info.iloc[:])

print(account_info.iloc[1, 2])

account_info.iloc[1, 2] = 3975

print(account_info.iloc[1, 2])

# Accessing row and column in dataframe using iloc
print(account_info.iloc[account_info.index % 2 == 1])

# Accessing rows and columns in a DataFrame using loc
print(account_info.loc[1, 'balance'])

print(account_info.loc[0:1, ['name', 'balance']])

# print(account_info.loc[('Mary', 'mj100'), pd.IndexSlice[:, 'balance']])