import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import r_func
# sphinx_gallery_thumbnail_number = 2

trade = []
trade_name = ["2S_1D", "7UP_1D", "A_1D", "AAV_1D","ABICO_1D"]

for i in trade_name:
    trade.append(i+'.csv')

listt = []
count = 0

for i in trade:
    listt.append([])
    for j in trade:
        temp = r_func.r_value(i,j)
        listt[count].append(temp)
    count+=1

print(listt)

harvest = np.array(listt)


fig, ax = plt.subplots()
im = ax.imshow(harvest)

# We want to show all ticks...
ax.set_xticks(np.arange(len(trade_name)))
ax.set_yticks(np.arange(len(trade_name)))
# ... and label them with the respective list entries
ax.set_xticklabels(trade_name)
ax.set_yticklabels(trade_name)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(trade_name)):
    for j in range(len(trade_name)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Correlation Coefficient ")
fig.tight_layout()
plt.show()