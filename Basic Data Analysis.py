print(data.describe())

grouped = data.groupby('categorical_column')['numerical_column'].mean()
print(grouped)
