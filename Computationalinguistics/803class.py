#2017.8.3
#clustering k-means
from scipy.cluster.vq import kmeans
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

clusters = kmeans(data,2)
print(clusters)
