import numpy as np
import pandas as pd
import numpy
import plotly.graph_objects as go
from array import array
import csv


class OutreachApp(object):

    def __init__(self, combine, strength, vertical, quickness, agility, speed):
        self.combine = combine
        self.strength = strength
        self.vertical = vertical
        self.quickness = quickness
        self.agility = agility
        self.speed = speed
        self.userdata = {'combine': combine, 'strength': strength, 'vertical': vertical,
                         'quickness': quickness, 'agility': agility, 'speed': speed}


def calc_percentile(strength, vertical, quickness, agility, speed):
    # this is the hardcoded strength array --> we will need to convert strength column csv data to populate this array
    # float array

    list_st = array('f', [8, 17, 16, 10, 7, 7, 3, 13, 0.5, 7, 10, 13, 5, 5, 15, 12, 5, 1])
    total_stud = len(list_st)  # the total num of students is the number of scores, alternatively the number of rows-1
    sorted(list_st)  # array sorted in ascending order
    position = sorted(list_st).index(strength)  # locates the strength score input by the user in the array --> this is
    # equivalent to num values below variable
    decimal = position / total_stud
    st_percentile = decimal * 100
    # return percentile
    # this needs to get passed to plot the first value of radar chart

    list_v = array('f', [27.5, 35.5, 28.5, 26.5, 29, 25, 29.5, 32, 26.5, 31.5, 32, 32, 25.5, 32.5, 33, 34.5, 24.5, 30])
    total_stud = len(list_v)  # the total num of students is the number of scores, alternatively the number of rows-1
    sorted(list_v)  # array sorted in ascending order
    position = sorted(list_v).index(vertical)  # locates the score input by the user in the array
    decimal = position / total_stud
    v_percentile = decimal * 100
    # return percentile

    list_q = array('f',
                   [2.75, 2.69, 3.02, 3.29, 3.2, 3.19, 3.01, 2.91, 0, 0, 0, 3.19, 2.96, 3.2, 3.14, 3.03, 2.99, 2.86])
    total_stud = len(list_q)  # the total num of students is the number of scores, alternatively the number of rows-1
    sorted(list_q)  # array sorted in ascending order
    position = sorted(list_q).index(quickness)  # locates the score input by the user in the array
    decimal = position / total_stud
    q_percentile = decimal * 100

    list_a = array('f', [1, 2, 3, 4, 5])
    total_stud = len(list_a)  # the total num of students is the number of scores, alternatively the number of rows-1
    sorted(list_a)  # array sorted in ascending order
    position = sorted(list_a).index(agility)  # locates the score input by the user in the array
    decimal = position / total_stud
    a_percentile = decimal * 100

    list_sp = array('f',
                    [1, 2, 3, 4, 5])
    total_stud = len(list_sp)  # the total num of students is the number of scores, alternatively the number of rows-1
    sorted(list_sp)  # array sorted in descending order
    position = sorted(list_sp).index(speed)  # locates the score input by the user in the array
    decimal = position / total_stud  # applying percentile formula n = num values below score / total num values
    sp_percentile = decimal * 100

    final_arr = array('f', [st_percentile, v_percentile, q_percentile, a_percentile, sp_percentile])
    return final_arr


if __name__ == '__main__':
    this_outreach = OutreachApp(combine=0,
                                strength=0,
                                vertical=0,
                                quickness=0,
                                agility=0,
                                speed=0
                                )

    # create dataframe of results
    print("Enter student results to populate the dataframe")
    df_data = pd.DataFrame(columns=['Combine', 'Strength', 'Vertical', 'Quickness', 'Agility', 'Speed'])
    num_stu = int(input("how many student's are there?: "))
    i = 0
    while i < num_stu:
        df_data = df_data.apply({'Combine': float(input()), 'Strength': float(input()), 'Vertical': float(input()),
                                  'Quickness': float(input()), 'Agility': float(input()), 'Speed': float(input())},
                                ignore_index=True)
        i + 1
    print("Table of Student Results ", df_data, sep='\n')  # prints dataframe

    # get percentiles
    print("Now we can calculate percentiles of each combine result")

    # can input as many combine score sets as user desires until program is stopped
    while True:
        # get text input and convert to int
        combine = int(input("Enter your combine number: "))
        strength = float(input("Enter your strength score: "))
        vertical = float(input("Enter your vertical score: "))
        quickness = float(input("Enter your quickness score: "))
        agility = float(input("Enter your agility score: "))
        speed = float(input("Enter your speed score: "))

        # create title to display on graph using unique combine number
        title = 'Combine' + ' ' + str(combine)

        # set plot values
        plot_arr = np.array(calc_percentile(strength, vertical, quickness, agility, speed))
        # returns numpy array that's required for polar plot
        print(plot_arr)

        fig = go.Figure(data=go.Scatterpolar(r=plot_arr, theta=['Strength', 'Vertical',
                                                                'Quickness', 'Agility',
                                                                'Speed'], fill='toself'))
        # set plot layout
        fig.update_layout(polar=dict(
            radialaxis=dict(range=[0, 100],
                            visible=True
                            ),
        ), showlegend=False)
        fig.update_layout(title_text=title)
        fig.show()  # displays graph
