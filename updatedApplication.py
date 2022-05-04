import numpy as np
import pandas as pd
import numpy
import plotly.graph_objects as go
from array import array
import csv


class OutreachApp(object):

    def __init__(self, combine, strength, vertical, quickness, speed, agility):
        self.combine = combine
        self.strength = strength
        self.vertical = vertical
        self.quickness = quickness
        self.speed = speed
        self.agility = agility
        self.userdata = {'combine': combine, 'strength': strength, 'vertical': vertical,
                         'quickness': quickness, 'speed': speed, 'agility': agility}


def calc_percentile(strength, vertical, quickness, speed, agility):

    # number of students to represent number of rows in data matrix
    n = int(input("Enter total number of students : "))

    #populate strength array
    list_st = [] # creating an empty list
    print("enter all strength scores")
    # iterating till the range
    for i in range(0, n):
        ele = float(input())

        list_st.append(ele)  # adding the element

    print(list_st)

    #create array of vertical scores
    list_v = []
    print("enter all vertical scores")
    # iterating till the range
    for j in range(0, n):
        ele = float(input())

        list_v.append(ele)  # adding the element

    print(list_v)

    #populate array for quickness scores
    list_q = []
    print("enter all quickness scores")
    # iterating till the range
    for k in range(0, n):
        ele = float(input())

        list_q.append(ele)  # adding the element

    print(list_q)

    #populate array for speed scores
    list_sp = []
    print("enter all speed scores")
    # iterating till the range
    for l in range(0, n):
        ele = float(input())

        list_sp.append(ele)  # adding the element

    print(list_sp)

    #populate array for agility scores
    list_a = []
    print("enter all agility scores")
    # iterating till the range
    for m in range(0, n):
        ele = float(input())

        list_a.append(ele)  # adding the element

    print(list_a)


    #strength test
    total_stud = len(list_st)  # the total num of students is the number of scores, alternatively the number of rows-1
    sorted(list_st)  # array sorted in ascending order
    position = sorted(list_st).index(strength)  # locates the strength score input by the user in the array --> this is
    # equivalent to num values below variable
    decimal = position / total_stud
    st_percentile = decimal * 100
    # return percentile
    # this needs to get passed to plot the first value of radar chart


    #vertical test
    total_stud = len(list_v)
    sorted(list_v)
    position = sorted(list_v).index(vertical)
    decimal = position / total_stud
    v_percentile = decimal * 100
    # return percentile1



    #quickness test
    total_stud = len(list_q)
    sorted(list_q)
    position = sorted(list_q).index(quickness)
    decimal = position / total_stud
    q_percentile = decimal * 100




    #speed test
    total_stud = len(list_sp)
    sorted(list_sp)
    position = sorted(list_sp).index(speed)
    decimal = position / total_stud
    sp_percentile = decimal * 100

    #agility test
    total_stud = len(list_a)
    sorted(list_a)
    position = sorted(list_a).index(agility)
    decimal = position / total_stud
    a_percentile = decimal * 100

    final_arr = array('f', [st_percentile, v_percentile, q_percentile, sp_percentile, a_percentile])
    return final_arr


if __name__ == '__main__':
    this_outreach = OutreachApp(combine=0,
                                strength=0,
                                vertical=0,
                                quickness=0,
                                speed=0,
                                agility=0
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
        agility = float(input("Enter your speed score: "))

        # create title to display on graph using unique combine number
        title = 'Combine' + ' ' + str(combine)

        # set plot values
        plot_arr = np.array(calc_percentile(strength, vertical, quickness, speed, agility))
        # returns numpy array that's required for polar plot
        print(plot_arr)

        fig = go.Figure(data=go.Scatterpolar(r=plot_arr, theta=['Strength', 'Vertical',
                                                                'Quickness',
                                                                'Speed', 'Agility'], fill='toself'))
        # set plot layout
        fig.update_layout(polar=dict(
            radialaxis=dict(range=[0, 100],
                            visible=True
                            ),
        ), showlegend=False)
        fig.update_layout(title_text=title)
        fig.show()  # displays graph
