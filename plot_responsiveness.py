from matplotlib import pyplot as plt

dataX = ["1","2","4","6","8","10"]
dataCY = [9.03, 17.06, 33.44, 50.15, 69.20, 89.02]
dataEY = [35.21, 34.56, 34.89, 36.67, 35.49, 35.75]

dataMCY = [9.98, 33.28, 45.54, 94.53, 107.19, 142.68]
dataMEY = [41.54, 50.31, 43.76, 48.08, 42.90, 48.92]


def plot_data(dataX, dataCY, dataEY, name):
    plt.figure(dpi=500)
    plt.plot(dataX,dataCY,marker='o', ms=8, label="Cloud-centric", color="green")
    plt.plot(dataX,dataEY,marker='^', ms=8,label="Edge-based", color="darkviolet")
    plt.xlabel("Number of IoT Devices")
    plt.ylabel("Average Response Time (s)")
    plt.legend()
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.tight_layout()
    plt.savefig(name)

#plot_data(dataX, dataCY, dataEY, 'responsiveness')
plot_data(dataX, dataMCY, dataMEY, 'med_resp')
