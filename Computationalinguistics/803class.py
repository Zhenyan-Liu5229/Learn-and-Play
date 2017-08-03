#2017.8.3
#clustering k-means
from scipy.cluster.vq import kmeans
import random
def open_file(path):
    file = open(path)
    lines = []
    for line in file:
        line = line.strip()
        line = float(line)
        lines.append(line)
    file.close()
    return lines

k_lines = open_file('D:\\code\\UBC\\k_VOT.txt')
g_lines = open_file('D:\\code\\UBC\\g_VOT.txt')

data = []
data.extend(k_lines)
data.extend(g_lines)

clusters, _ = kmeans(data,2) #_for useless variable
k_centroid = max(clusters)
g_centroid = min(clusters)

for j in range(11):
    value = random.uniform(10,16)
    k_distance = abs(value - k_centroid) #distance from centroid
    g_distance = abs(value - g_centroid)
    if k_distance < g_distance:
        print('This sound is probably a k')
    else:
        print('This sound is probably a g')
