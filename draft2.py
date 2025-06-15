import pandas as pd
data = {
    "task": ["RS essay", "PC homework", "AW essay"],
    "deadline": ["26 June", "15 June", "16 June"],
    "status": ["not done", "not done", "in progress"]
}
df = pd.DataFrame(data)
print(df)