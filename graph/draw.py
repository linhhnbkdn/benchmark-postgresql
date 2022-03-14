import os
import json

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
history = os.path.join(os.path.dirname(__file__), 'history.log')
with open(history, 'r') as f:
    lines = f.readlines()

lines = [line.replace('\n', '') for line in lines]

min_list = []
max_list = []
mean_list = []
total_list = []
num_of_req = []

for line in lines:
    line = json.loads(line)
    total_list.append(float(line['total']))
    num_of_req.append(line['num_of_req'])
    min_list.append(line['min'])
    mean_list.append(line['mean'])
    max_list.append(line['max'])

print(num_of_req)
plt.plot(num_of_req, total_list, linewidth=2, label='total')
plt.xlim(0, max(num_of_req))
plt.xlabel('Number of requests')
plt.ylabel('Time (s)')
plt.ylim(0, max(total_list))
# plt.show()
plt.savefig('graph.png')