import webbrowser

print("Welcome to CryptoNow!")
print("Here you can get all crypto news, prices, trends and much more with just one click!")
print("Opening crypto sites in your browser...")
print("1 - Open Coingecko")
print("2 - Open Coinmarketcap")
print("3 - Open Decrypt")
print("4 - Open Cointelegraph")
print("5 - Open Cryptonews")

def menu():
    
    option = int(input("Select option: ")) 
    
    if option == 1:
        print("Loading Coingecko...")
        webbrowser.open('https://coingecko.com/')
    
    elif option == 2:
    
        print("Loading Coinmarketcap...")
        webbrowser.open('https://coinmarketcap.com/')
    
    elif option == 3:
        print("Loading Decrypt...")
        webbrowser.open('https://decrypt.co/')
        
    elif option == 4:
        print("Loading Cointelegraph...")
        webbrowser.open('https://cointelegraph.com/')
        
    elif option == 5:
        print("Loading Cryptonews...")
        webbrowser.open('https://cryptonews.com/')
    
    else:
        print("Select number between 1-5: ")
        
menu()
    


