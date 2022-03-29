import numpy as np
import pandas as pd
import numpy
import plotly.graph_objects as go
from array import array
import csv


class OutreachApp(object):

    def __init__(self, combine, strength, vertical, quickness, speed):
        self.combine = combine
        self.strength = strength
        self.vertical = vertical
        self.quickness = quickness
        self.speed = speed
        self.userdata = {'combine': combine, 'strength': strength, 'vertical': vertical,
                         'quickness': quickness, 'speed': speed}


def calc_percentile(strength, vertical, quickness, speed):

    # number of elements as input
    n = int(input("Enter total number of students : "))

    #strength test
    # creating an empty list
    list_st = []
    print("enter all strength scores")
    # iterating till the range
    for i in range(0, n):
        ele = float(input())

        list_st.append(ele)  # adding the element

    print(list_st)

    total_stud = len(list_st)  # the total num of students is the number of scores, alternatively the number of rows-1
    sorted(list_st)  # array sorted in ascending order
    position = sorted(list_st).index(strength)  # locates the strength score input by the user in the array --> this is
    # equivalent to num values below variable
    decimal = position / total_stud
    percentile = decimal * 100
    # return percentile
    # this needs to get passed to plot the first value of radar chart


    #vertical test
    list_v = []
    print("enter all vertical scores")
    # iterating till the range
    for j in range(0, n):
        ele = float(input())

        list_v.append(ele)  # adding the element

    print(list_v)

    total_stud = len(list_v)
    sorted(list_v)
    position = sorted(list_v).index(vertical)
    decimal = position / total_stud
    percentile1 = decimal * 100
    # return percentile1



    #quickness test
    list_q = []
    print("enter all quickness scores")
    # iterating till the range
    for k in range(0, n):
        ele = float(input())

        list_q.append(ele)  # adding the element

    print(list_q)

    total_stud = len(list_q)
    sorted(list_q)
    position = sorted(list_q).index(quickness)
    decimal = position / total_stud
    percentile2 = decimal * 100



    #speed test
    list_sp = []
    print("enter all speed scores")
    # iterating till the range
    for l in range(0, n):
        ele = float(input())

        list_sp.append(ele)  # adding the element

    print(list_sp)

    total_stud = len(list_sp)
    sorted(list_sp)
    position = sorted(list_sp).index(speed)
    decimal = position / total_stud
    percentile4 = decimal * 100

    final_arr = array('f', [percentile, percentile1, percentile2, percentile4])
    return final_arr


if __name__ == '__main__':
    this_outreach = OutreachApp(combine=0,
                                strength=0,
                                vertical=0,
                                quickness=0,
                                speed=0
                                )

    # get percentiles
    print("Now we can calculate percentiles of each combine result")

    # can input as many combine score sets as user desires until program is stopped
    while True:
        # get text input and convert to int
        combine = int(input("Enter your combine number: "))
        strength = float(input("Enter your strength score: "))
        vertical = float(input("Enter your vertical score: "))
        quickness = float(input("Enter your quickness score: "))
        speed = float(input("Enter your speed score: "))

        # create title to display on graph using unique combine number
        title = 'Combine' + ' ' + str(combine)

        # set plot values
        plot_arr = np.array(calc_percentile(strength, vertical, quickness, speed))
        # returns numpy array that's required for polar plot
        print(plot_arr)

        fig = go.Figure(data=go.Scatterpolar(r=plot_arr, theta=['Strength', 'Vertical',
                                                                'Quickness',
                                                                'Speed'], fill='toself'))
        # set plot layout
        fig.update_layout(polar=dict(
            radialaxis=dict(range=[0, 100],
                            visible=True
                            ),
        ), showlegend=False)
        fig.update_layout(title_text=title)
        fig.show()  # displays graph
