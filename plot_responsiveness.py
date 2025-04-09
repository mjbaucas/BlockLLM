from matplotlib import pyplot as plt

dataX = ["1","2","4","6","8","10"]
dataCY = [9.03, 17.06, 33.44, 50.15, 69.20, 89.02]
dataEY = [35.21, 34.56, 34.89, 36.67, 35.49, 35.75]


def plot_data(dataX, dataCY, dataEY):
    plt.figure(0)
    plt.plot(dataX,dataCY,marker='s',label="Cloud-centric", color="red")
    plt.plot(dataX,dataEY,marker='o',label="Edge-based", color="blue")
    plt.xlabel("Number of IoT Devices")
    plt.ylabel("Average Response Time (s)")
    plt.legend()
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.savefig('responsiveness.png')

plot_data(dataX, dataCY, dataEY)

