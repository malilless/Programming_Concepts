import pandas as pd
import yfinance as yf

INITIAL_MONEY = 100000

# Завдання 1-2: збір і організація даних
apple = yf.Ticker("AAPL")

start_date = "2022-01-01"
end_date = "2024-01-01"

data = apple.history(start=start_date, end=end_date)[["Open", "High", "Low", "Close", "Volume"]]
data["MA_30_days"] = data["Close"].rolling(window=30).mean()
data["MA_100_days"] = data["Close"].rolling(window=100).mean()

# Завдання 3: розробка моделі
MA_30_days_today = data["MA_30_days"]
MA_100_days_today = data["MA_100_days"]
MA_30_days_yesterday = data["MA_30_days"].shift(1)
MA_100_days_yesterday = data["MA_100_days"].shift(1)

# Завдання 4: генерація сигналу
data["Decision"] = (
    ((MA_30_days_today > MA_100_days_today) & (MA_30_days_yesterday < MA_100_days_yesterday)).astype(int) -
    ((MA_30_days_today < MA_100_days_today) & (MA_30_days_yesterday > MA_100_days_yesterday)).astype(int)
)
# data["Next_decision"] = data["Decision"].shift(-1)
print("Decision-making DataFrame:")
print(data[(data["Decision"] != 0) | ((data["Decision"].shift(-1) == 1) | (data["Decision"].shift(-1) == -1))])

# Завдання 5: розрахунок ефективності моделі
decision_frame = data[data["Decision"] != 0]
money = INITIAL_MONEY
stocks = 0
for index, row in decision_frame.iterrows():
    print(f"Today is {index.strftime('%A, %d %B %Y')}.")
    print(f"Current balance: {money:.2f} money, {int(stocks)} stocks.")
    if row["Decision"] == 1:
        stocks_affordable = money // row["Open"]
        print(f"Bying {int(stocks_affordable)} stocks.")
        stocks += stocks_affordable
        money -= stocks_affordable * row["Open"]
        continue
    if row["Decision"] == -1: 
        print(f"Selling all {int(stocks)} stocks.")
        money += stocks * row["Open"]
        stocks = 0

last_price = data.iloc[-1]["Close"]
print(f"Total operations made: {len(decision_frame)}.\nOperations result:")
print(f"Money: {money:.2f}, stocks: {int(stocks)}, last stock price: {last_price:.2f}.")
total = last_price * stocks + money
print(f"Total: {total:.2f}.")
profit = total - INITIAL_MONEY
print(f"Profit: {profit:.2f}.")
if profit <= 0:
    print("Seems like we are not so good in stocks trading... 😢")