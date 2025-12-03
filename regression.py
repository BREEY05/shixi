import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 12

data = [[-0.5, 7.7], [1.8, 98.5], [0.9, 57.8], [0.4, 39.2], [-1.4, -15.7],
        [-1.4, -37.3], [-1.8, -49.1], [1.5, 75.6], [0.4, 34.0], [0.8, 62.3]]
data = np.array(data)
x = data[:, 0]  
y = data[:, 1]

x_tensor = torch.tensor(x, dtype=torch.float32).reshape(-1, 1)
y_tensor = torch.tensor(y, dtype=torch.float32) 

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.linear = nn.Linear(1, 1)
    
    def forward(self, x):
        x = self.linear(x)
        return x

model=MyModel()
lr=0.01 
criterion = nn.MSELoss() 
optm = torch.optim.SGD(model.parameters(), lr=lr)
epochs = 500 

model_params_history = []
loss_history = []
print("\n开始训练模型...")
for epoch in range(1, epochs + 1):
    model.train()
    y_pred=model(x_tensor)
    loss = criterion(y_pred.squeeze(-1), y_tensor)
    optm.zero_grad()
    loss.backward()
    optm.step() 

    if epoch % 10 == 0:
        w_current=model.linear.weight.data.numpy()[0][0]
        b_current=model.linear.bias.data.numpy()[0]
        loss_current = loss.item()
        model_params_history.append((epoch, w_current, b_current))
        loss_history.append((epoch, loss_current))
 
    if epoch % 50==0:
        print(f"第{epoch}轮训练，损失值: {loss.item():.4f}")
w=model.linear.weight.data.numpy()[0][0]  
b=model.linear.bias.data.numpy()[0]      

print(f"\n模型训练完成！")
print(f"学习到的权重:{w:.4f}")
print(f"学习到的偏置:{b:.4f}")
print(f"线性回归方程:y={w:.4f}x+{b:.4f}")

#左边
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(x, y, color='blue', s=100, alpha=0.7)
plt.title("散点图")
plt.xlabel("特征值")
plt.ylabel("标签值")
plt.grid(True,alpha=0.3)

# 右边
plt.subplot(1,2,2)
plt.scatter(x,y,color='blue',s=100,alpha=0.7)
plt.xlabel("特征值")
plt.ylabel("标签值")
plt.title("动态拟合过程",fontsize=14,fontweight='bold')
plt.grid(True,alpha=0.3)

final_loss = loss_history[-1][1]
# 变量顶部距离
title_distance = 0.99
plt.suptitle(f"Loss:{final_loss:.2f},权重w:{w:.2f},偏置b:{b:.2f}", 
             fontsize=14, fontweight='bold', y=title_distance)

x_line=np.linspace(min(x),max(x),100)
line,=plt.plot([],[],color='red',linewidth=2)

for i,(epoch,w_current,b_current) in enumerate(model_params_history):
    y_line = w_current * x_line + b_current
    line.set_data(x_line, y_line)
    color_intensity = i / len(model_params_history)
    line.set_color((color_intensity, 0, 1-color_intensity))
    plt.pause(0.1)



