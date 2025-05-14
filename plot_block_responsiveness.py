from matplotlib import pyplot as plt

dataX = ["1","2","4","6","8","10"]

# Medical Block LLM
#dataPub = [3.19, 9.16, 17.91, 26.95, 37.05, 46.97]
#dataPriv = [0.03, 0.05, 0.31, 1.15, 1.83, 3.73]

# Agri Block LLM
dataPub = [3.14, 9.22, 21.41, 28.26, 34.54, 47.02]
dataPriv = [0.06, 0.16, 0.30, 0.84, 1.60, 1.88]

def plot_data(dataX, dataPub, dataPriv, name):
    plt.figure(dpi=500)
    plt.plot(dataX,dataPub,marker='s', ms=8, label="Public Blockchain", color="orange")
    plt.plot(dataX,dataPriv,marker='o', ms=8,label="Private Blockchain", color="blue")
    plt.xlabel("Number of IoT Devices")
    plt.ylabel("Average Response Time (s)")
    plt.legend()
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.tight_layout()
    plt.savefig(name)

#plot_data(dataX, dataCY, dataEY, 'responsiveness')
#plot_data(dataX, dataPub, dataPriv, 'med_block_resp')
plot_data(dataX, dataPub, dataPriv, 'agri_block_resp')
