import matplotlib.pyplot as plt

# x=plt.subplots(1,2)
# print(type(x))
# print(len(x))
# print(x)
s,ax=plt.subplots(2,2)
print(ax)
print(ax[0])
ax[0][0].plot(0.5,0.5)
ax[0][1].text(0.5,0.5,'text 1')
ax[1][0].plot(0.5,0.5)
ax[1][0].text(0.5,0.5,'text 2')
ax[0][0].scatter(0.5,0.5,c='r')
ax[1][1].scatter(1,0.5,c='g')
plt.show()