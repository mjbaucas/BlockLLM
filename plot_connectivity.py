from matplotlib import pyplot as plt

dataX = ["1","2","4","6","8","10"]
dataCY = [0, 2, 33.75, 208.5, 339.375, 436.5]
dataEY = [0, 0, 0 ,0 ,0 ,0]


def plot_data(dataX, dataCY, dataEY):
    plt.figure(0)
    plt.plot(dataX,dataCY,marker='s',label="Cloud-centric", color="red")
    plt.plot(dataX,dataEY,marker='o',label="Edge-based", color="blue")
    plt.xlabel("Number of IoT Devices")
    plt.ylabel("Average Number of Connection Resets")
    plt.legend()
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.savefig('connectivity.png')

plot_data(dataX, dataCY, dataEY)

