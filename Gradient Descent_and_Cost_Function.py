import numpy as np

def func(x,y):
    m_current= y_current= 0
    iteration= 1000
    n= len(x)
    learning_rate= 0.01
    for i in range(iteration):
        y_pred= m_current * x + y_current
        cost= (1/n)* sum(values**2 for values in (y-y_pred))
        md= -(2/n)* sum(x*(y-y_pred))
        bd= -(2/n)* sum(y-y_pred)
        m_current= m_current - learning_rate * md
        y_current= y_current - learning_rate * bd
        print("m {}, b {}, iteration {}, cost {}".format(m_current, y_current, i, cost))



x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])

func(x,y)