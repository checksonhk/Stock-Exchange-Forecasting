import pickle
import matplotlib.pyplot as plt

plt.style.use('ggplot')


test = open("C:/Users/Jackson/Documents/Data Science/CryptoCurrencies/portfolio_val/201907092349-test.pickle","rb")
ex_test = pickle.load(test)
plt.plot(ex_test)
plt.show()

train = open("C:/Users/Jackson/Documents/Data Science/CryptoCurrencies/portfolio_val/201907092349-train.pickle","rb")
ex_train = pickle.load(train)
plt.plot(ex_train)
plt.show()




