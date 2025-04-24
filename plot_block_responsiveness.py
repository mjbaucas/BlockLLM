from matplotlib import pyplot as plt

dataX = ["1","2","4","6","8","10"]
dataPub = [3.19, 9.16, 17.91, 26.95, 37.05, 46.97]
dataPriv = [0.03, 0.05, 0.31, 1.15, 1.83, 3.73]



def plot_data(dataX, dataPub, dataPriv, name):
    plt.figure(dpi=500)
    plt.plot(dataX,dataPub,marker='o', ms=8, label="Public Blockchain", color="red")
    plt.plot(dataX,dataPriv,marker='^', ms=8,label="Private Blockchain", color="darkcyan")
    plt.xlabel("Number of IoT Devices")
    plt.ylabel("Average Response Time (s)")
    plt.legend()
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.tight_layout()
    plt.savefig(name)

#plot_data(dataX, dataCY, dataEY, 'responsiveness')
plot_data(dataX, dataPub, dataPriv, 'block_resp')
