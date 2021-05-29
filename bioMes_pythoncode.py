import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


#to run this code you have to change in source files \t to ; and , to .

FALT_CONST = 0.040

prop1 = []
prop2 = []

sum1 = 0
sum2 = 0


with open("dane/PROB1_1.txt", 'r') as file:
    prop1 = file.readline()
with open('dane/PROB2_1.txt', 'r') as file:
    prop2 = file.readline()

#dome data formating

propTab = prop1.split(sep = ';')
propTab_2 = prop2.split(sep = ';')

fig, ax = plt.subplots(2)
ax[0].plot([i for i in range(0,len(propTab))], propTab)
ax[1].plot([i for i in range(0,len(propTab_2))], propTab_2)


# for cacl integral in <>
for i in range(400,600):
    sum1 = sum1 + float(propTab_2[i]) - FALT_CONST
    
pr1 = (sum1/(sum1+sum2)) * 100
pr2 = (sum2/(sum1+sum2)) * 100


#ax.xaxis.set_major_locator(ticker.MultipleLocator(100))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(20))
for i in range(0,2):
    ax[i].yaxis.set_major_locator(ticker.MaxNLocator(10))
    ax[i].yaxis.set_minor_locator(ticker.MaxNLocator(40))

    ax[i].grid()
fig.suptitle('Mieszanina 1')
fig.savefig("test.png")
plt.show()

etanol = 8.27*13.74
prop = 12.57*1.04
c = etanol + prop 

c_etanol = (etanol/c)*100
c_prop = (prop/c)



