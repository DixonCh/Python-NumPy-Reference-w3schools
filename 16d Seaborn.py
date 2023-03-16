'''Seaborn:

Visualize Distributions With Seaborn:

Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.

Install Seaborn.

If you have Python and PIP already installed on a system, install it using this command:

C:\Users\Your Name>pip install seaborn

If you use Jupyter, install Seaborn using this command:

C:\Users\Your Name>!pip install seaborn

Distplots:

Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the 
array.

'''
Import Matplotlib
import the pyplot object of the Matplotlib module in your code using following code
import matplotlib.pyplot as plt
Import Seaborn
import the seaborn in your code using following code
import seaborn as sns
Plotting a Displot

Example
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()

Plotting a Distplot Without the Histogram:
  
Example:
  
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()
