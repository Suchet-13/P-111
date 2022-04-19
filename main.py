import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return(mean)

mean_list = []
for i in range(0,100):
  set_of_means = random_set_of_mean(30)
  mean_list.append(set_of_means)


def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist = False)
    fig.show()

first_stdev_start, first_stdev_end = mean-std_deviation, mean+std_deviation
second_stdev_start, second_stdev_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_stdev_start, third_stdev_end = mean-(3*std_deviation), mean+(3*std_deviation)
print("std1: ",first_stdev_start, first_stdev_end)
print("std2: ",second_stdev_start, second_stdev_end)
print("std3:",third_stdev_start, third_stdev_end)

fig = ff.create_distplot([mean_list],["student marks"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start], y=[0,0.17], mode="lines", name="std deviation 1 start"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end], y=[0,0.17], mode="lines", name="std deviation 1 end"))
fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start], y=[0,0.17], mode="lines", name="std deviation 2 start"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end], y=[0,0.17], mode="lines", name="std deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start], y=[0,0.17], mode="lines", name="std deviation 3 start"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end], y=[0,0.17], mode="lines", name="std deviation 3 end"))
fig.show()