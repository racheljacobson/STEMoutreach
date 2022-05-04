from array import array

import numpy as np
import plotly.graph_objects as go


class OutreachApp(object):

    def __init__(self, combine, strength, vertical, agility, quickness, speed):
        self.combine = combine
        self.strength = strength
        self.vertical = vertical
        self.agility = agility
        self.quickness = quickness
        self.speed = speed
        self.userdata = {'combine': combine, 'strength': strength, 'vertical': vertical,
                         'agility': agility, 'quickness': quickness, 'speed': speed}


def calc_percentile(list_st, list_v, list_a, list_q, list_sp, strength, vertical, agility, quickness, speed):
    # strength test

    total_stud = len(list_st)  # the total num of students is the number of scores, alternatively the number of rows-1
    sorted(list_st)  # array sorted in ascending order
    position = sorted(list_st).index(strength)  # locates the strength score input by the user in the array --> this is
    # equivalent to num values below variable
    decimal = position / total_stud
    strength_percentile = decimal * 100
    # return percentile
    # this needs to get passed to plot the first value of radar chart

    # vertical test
    total_stud = len(list_v)
    sorted(list_v)
    position = sorted(list_v).index(vertical)
    decimal = position / total_stud
    vertical_percentile = decimal * 100

    # agility test

    total_stud = len(list_a)
    sorted(list_a)
    position = sorted(list_a).index(agility)
    decimal = position / total_stud
    agility_percentile = decimal * 100

    # quickness test

    total_stud = len(list_q)
    sorted(list_q)
    position = sorted(list_q).index(quickness)
    decimal = position / total_stud
    quick_percentile = decimal * 100

    # speed test

    total_stud = len(list_sp)
    sorted(list_sp)
    position = sorted(list_sp).index(speed)
    decimal = position / total_stud
    speed_percentile = decimal * 100

    final_arr = array('f', [strength_percentile, vertical_percentile, agility_percentile, quick_percentile,
                            speed_percentile])
    return final_arr


if __name__ == '__main__':
    this_outreach = OutreachApp(combine=0,
                                strength=0,
                                vertical=0,
                                agility=0,
                                quickness=0,
                                speed=0
                                )

    # get percentiles
    # number of elements as input
    n = int(input("Enter total number of users : "))

    # strength test
    # creating an empty list
    list_st = []
    print("enter all strength scores")
    # iterating till the range
    for i in range(0, n):
        ele = float(input())

        list_st.append(ele)  # adding the element

    print(list_st)

    # vertical test
    list_v = []
    print("enter all vertical scores")
    # iterating till the range
    for j in range(0, n):
        ele = float(input())

        list_v.append(ele)  # adding the element

    print(list_v)

    # agility test
    list_a = []
    print("enter all agility scores")
    # iterating til the range
    for k in range(0, n):
        ele = float(input())
        list_a.append(ele)  # adding the element
    print(list_a)

    # quickness test
    list_q = []
    print("enter all quickness scores")
    # iterating till the range
    for l in range(0, n):
        ele = float(input())
        list_q.append(ele)  # adding the element

    print(list_q)

    # speed test
    list_sp = []
    print("enter all speed scores")
    # iterating till the range
    for m in range(0, n):
        ele = float(input())
        list_sp.append(ele)  # adding the element

    print(list_sp)

    print("Now we can calculate percentiles of each combine athlete result")

    # can input as many combine score sets as user desires until program is stopped
    while True:
        # get text input and convert to int

        combine = int(input("Enter your combine number: "))
        x = combine-1 #value used to find position in arrays
        strength = float(list_st[x])
        vertical = float(list_v[x])
        agility = float(list_a[x])
        quickness = float(list_q[x])
        speed = float(list_sp[x])

        # create title to display on graph using unique combine number
        title = 'Combine Athlete Number ' + ' ' + str(combine)

        # set plot values
        plot_arr = np.array(
            calc_percentile(list_st, list_v, list_a, list_q, list_sp, strength, vertical, agility, quickness, speed))
        # returns numpy array that's required for polar plot
        print(plot_arr)

        fig = go.Figure(data=go.Scatterpolar(r=plot_arr, theta=['Strength', 'Vertical',
                                                                'Agility', 'Quickness',
                                                                'Speed'], fill='toself'))
        # set plot layout
        fig.update_layout(polar=dict(
            radialaxis=dict(range=[0, 100],
                            visible=True
                            ),
        ), showlegend=False)
        fig.update_layout(title_text=title)
        fig.show()  # displays graph