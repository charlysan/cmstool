import matplotlib.pyplot as plt
import mpld3
from mpld3._server import serve

#firstgraph
x = [1,2,3]
y = [2,3,4]
fig1 = plt.figure()
plt.xlabel("xlabel 1")
plt.ylabel("ylabel 1")
plt.title("Plot 1")
plt.legend()
plt.bar(x,y, label = 'label for bar', color = 'b')

#secondgraph 
x = [1,2,3]
y = [5,3,4]
fig2 =plt.figure()
plt.xlabel("xlabel 2")
plt.ylabel("ylabel 2")
plt.title("Plot 2")
plt.bar(x,y, color = 'r')

# create html for both graphs 
html1 = mpld3.fig_to_html(fig1)
html2 = mpld3.fig_to_html(fig2)
# serve joined html to browser
serve(html1+html2)
