class Stock:
    def __init__(self, name, noShare, sharePrice):
        self.name = name
        self.noShare = noShare
        self.sharePrice = sharePrice
    def __str__(self):
        return f"Stock details: \nStock name: {self.name}, Number of shares: {self.noShare}, Price of Each Share: {self.sharePrice}, Total share value: {(self.sharePrice * self.noShare)}"

def WriteStock():
    StockData = []
    Stocks = {}
    n = int(input("Enter total number of stocks: "))
    for i in range(n):
        stockName = input(f"Enter {i+1} stock name: ")
        numShare = int(input(f"Enter {i+1} number of shares: "))
        sharePrice = int(input(f"Enter {i+1} share price: "))
        Stocks = {"Stock Name" : stockName, "Number of Shares" : numShare, "Share Price" : sharePrice, "Total Share Value" : numShare*sharePrice}
        stock = Stock(stockName, numShare, sharePrice)
        print(stock)
        StockData.append(Stocks)

    for s in StockData:
        print(f"{s['Stock Name']}, {s['Number of Shares']}, {s['Share Price']}, {s['Total Share Value']}")


    with open("StockData.txt","a") as wfile:
        for s in StockData:
            wfile.write(f"{s['Stock Name']}, {s['Number of Shares']}, {s['Share Price']}, {s['Total Share Value']}\n")

def ReadStock():
    with open("StockData.txt") as rfile:
        for line in rfile:
            print(f'{line.rstrip().rsplit(",")[0]} | {line.rstrip().rsplit(",")[1]} | {line.rstrip().rsplit(",")[2]} | {line.rstrip().rsplit(",")[3]}')

choice = int(input("Enter 1 to write to file or 2 to read from the file: "))
if choice == 1: WriteStock()
else: ReadStock()