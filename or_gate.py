'''
Implementation of OR gate using Linear Regression Model
Author : Varad Rane
'''
input_data=[[0,0],
            [0,1],
            [1,0],
            [1,1]]
output_data=[0,1,1,1]

w1=0.3
w2=0.4


lr=0.2

def threshold(x):
    if x>0.5:
        return 1
    else:
        return 0
    
epochs=10

for i in range(epochs):
    error=0
    for j in range(4):
        x1=input_data[j][0]
        x2=input_data[j][1]
        
        
        t=output_data[j]

        z = w1*x1 + w2*x2
        y = threshold(z)
        error = t - y

        w1 = w1 + x1 * lr * error 
        w2 = w2 + x2 * lr * error
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"Epoch: {i+1}| Iterarion : {j} | Input : {x1,x2}  | Output : {t} | Predicted: {y} Total Error: {error:.2f} | Weights: {w1,w2} | Changeinweights: {x1*lr*error,x2*lr*error}")



