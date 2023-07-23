import numpy as np
import matplotlib.pyplot as plt


def estimate_coef(x, y):
	# number of observations/points
	n = np.size(x)

	# mean of x and y vector
	m_x = np.mean(x)
	m_y = np.mean(y)

	# calculating cross-deviation and deviation about x
	SS_xy = np.sum(y*x) - n*m_y*m_x
	SS_xx = np.sum(x*x) - n*m_x*m_x

	# calculating regression coefficients
	b_1 = SS_xy / SS_xx
	b_0 = m_y - b_1*m_x

	return (b_0, b_1)

def plot_regression_line(x, y, b):
	# plotting the actual points as scatter plot
	plt.scatter(x, y, color = "m",
			marker = "o", s = 30)

	# predicted response vector
	y_pred = b[0] + b[1]*x

	# plotting the regression line
	plt.plot(x, y_pred, color = "g")

        # putting labels
	plt.xlabel('Fertilizer(lb.)')
	plt.ylabel('Yield(lb.)')
	plt.title("Scattergram")

	plot_errors(x,y,b, y_pred)

        #function to show plot
	#plt.show()

	plt.savefig('regression line with errors.png')
	plt.show(block=False)
	plt.pause(3)
	plt.close("all")


def plot_errors(x,y,b, y_pred):
    least_squares=0

    for i in range(len(x)):
        least_squares+=pow(y_pred[i]-y[i],2)
        plt.vlines(x = x[i], ymin = min(y_pred[i],y[i]), ymax = max(y_pred[i],y[i]),
           colors = 'purple',
           label = 'vline_multiple - full height')
        plt.text(x[i]-0.3, y[i]+0.3, "e"+str(i)+"="+str(round(abs(y_pred[i]-y[i]),3)))


    print("\n Least_squares=",least_squares)


def regression_line(x,y):
        corr_matrix = np.corrcoef(x,y)
        corr = corr_matrix[0,1]

        print("\n coefficient of corelation=",corr)
        R_sq = corr**2

        print("coefficient of determination=",R_sq)


# observations / data

#uygulama 1 data
x = np.array([20,40,80,30,20,10])
y = np.array([5000,7000,9000,12500,17500,25000])

"""
#uygulama 2 data
x = np.array([1,2,3,4,5])
y = np.array([1,1,2,2,4])

#uygulama 3 data
x = np.array([4,6,10,12])
y = np.array([3.0, 5.5, 6.5, 9.0])

#örnek 1 data
x = np.array([25,28,35,32,31,36,29,38,34,32]) #marks in economics 
y = np.array([43,46,49,41,36,32,31,30,33,39]) #marks in statistics
#estimate y for x=30

#örnek 2 data
x = np.array([158,166,163,165,167,170,167,172,177,181]) #heights of fathers
y = np.array([163,158,167,179,160,180,170,175,172,175]) #heights of sons
#estimate y for x=164

#örnek 3 data
x = np.array([61,68,68,64,65,70,63,62,64,67]) #heights in inches 
y = np.array([112,123,130,115,110,125,100,113,116,125]) #weights in lb
#estimate y for x=69
"""

# estimating coefficients
b = estimate_coef(x, y)
print("Estimated coefficients:\nb_0 = {} \
	\nb_1 = {}".format(b[0], b[1]))

print("\n Regression line:")
print("Y = ", '%.3f'%b[0], " + ", '%.3f'%b[1], "*X", sep="")



# plotting regression line
regression_line(x,y)
plot_regression_line(x, y, b)

# özel değer için regresyon fonksiyonunu çalıştırma
x = int(input('\n Enter the X value:'))
y=b[0]+(b[1]*x)
print('Estimated Y= ' , round(y,3))


# en son çıkan sonucu yorumlamayı unutmayalım!!!!
