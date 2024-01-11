import csv
import requests
import matplotlib.pyplot as plt
CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=15min&slice=year1month1&apikey=demo'

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
header = my_list[0]
data = my_list[1:]

times = [row[0] for row in data]
close_prices = [float(row[4]) for row in data]

change = [close_prices[i+1] - close_prices[i] for i in range(len(close_prices) - 1)]

# Plot the data
colors = ['g' if change[i] >= 0 else 'r' for i in range(len(change))]
for i in range(len(change)):
    plt.plot(times[i:i+2], close_prices[i:i+2], color=colors[i])
plt.xlabel('Time')
plt.ylabel('Close Price')
plt.title('IBM Stock Price')
plt.show()
