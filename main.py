import matplotlib.pyplot as plt
x=[7,23,4,1,-4,5]
y=[12,2,-4,0,4,-8]
size=[120,324,345,323,654,32]
# color=['b','y','c','g','r','w']
# color=['0.9','0.8','0.7','0.6','0.5','0.4']
# color=['#103811','#D43111','#D40A11','#D43311','#D43801','#D43810']
color=[(44/255,234/255,22/255),(100/255,204/255,30/255),(200/255,234/255,32/255),(0/255,23/255,222/255),(44/255,234/255,150/255),(4/255,23/255,150/255)]
marker='1'
plt.scatter(x,y,size,color,marker)

plt.show()