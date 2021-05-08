import matplotlib.pyplot as plt


if __name__ == "__main__":
    with open('../Simulation/height1.out', 'r') as file1:
        lines = file1.read()
        height_list = lines.split("\n")
        del height_list[len(height_list)-1]
        height_list = list(map(float, height_list))

        x_list = list(range(len(height_list)))

        # json_list1 = []
        # for each in json_file1.readlines():
        #     json_data = json.loads(each)
        #     json_list1.append(json_data)

        # json_list2 = []
        # for each in json_file2.readlines():
        #     json_data = json.loads(each)
        #     json_list2.append(json_data)

        # x = list(range(1, 51))
        # y1 = []
        # y2 = []

        # for each in json_list1:
        #     y1.append(each['target']-12)

        # for each in json_list2:
        #     y2.append(each['target'])

        # y1 = y1[:len(x)]
        # y2 = y2[:len(x)]

        # print("x = ", x)
        # print("y1 = ", y1)
        # print("y2 = ", y2)

        # max_indx1 = np.argmax(y1)  # max value index
        # max_indx2 = np.argmax(y2)  # max value index

        # # l1 = plt.plot(x, y1,'bo',label='Min_Support', zorder = 10, alpha = 0.6)
        plt.plot(x_list,height_list,'bo-')

        # l2 = plt.plot(x, y2, 'r+', label='Reducing_Support',
        #               zorder=11, alpha=0.6)
        # plt.plot(x, y2, 'r+-', zorder=11)

        # # plt.scatter(max_indx1+1, y1[max_indx1], 70, marker='x', color = 'black', zorder = 20)
        # # plt.annotate(r'Min_Support: ['+str(max_indx1)+', '+str("%.4f"%y1[max_indx1])+']',
        # #             xy=(max_indx1+1, y1[max_indx1]), xycoords='data', xytext=(+10, +35),
        # #             textcoords='offset points', fontsize=9, arrowprops=dict(arrowstyle="->",
        # #             connectionstyle="arc3,rad=.2"))

        # plt.scatter(max_indx2+1, y2[max_indx2], 70,
        #             marker='x', color='black', zorder=20)
        # plt.annotate(r'Reducing_Support: ['+str(max_indx2)+', '+str("%.4f" % y2[max_indx2])+']',
        #              xy=(max_indx2+1, y2[max_indx2]), xycoords='data', xytext=(0, +70),
        #              textcoords='offset points', fontsize=9, arrowprops=dict(arrowstyle="->",
        #                                                                      connectionstyle="arc3,rad=.2"))

        # t = 10
        # plt.plot([t, t], [0, 50], color='black', linewidth=2.5, linestyle="--")

        # t = 20
        # plt.plot([t, t], [0, 50], color='black', linewidth=2.5, linestyle="--")

        # t = 30
        # plt.plot([t, t], [0, 50], color='black', linewidth=2.5, linestyle="--")

        # plt.title('Reducing-support')
        # plt.xlabel('Number of iterations')
        # plt.ylabel('Fitness')
        # plt.legend()
        plt.show()
