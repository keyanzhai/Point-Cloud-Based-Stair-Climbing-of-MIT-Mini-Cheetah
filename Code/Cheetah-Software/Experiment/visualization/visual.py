import matplotlib.pyplot as plt


if __name__ == "__main__":
    with open('../Simulation/New_Algorithm/new1cm.out', 'r') as file1:
        with open('../Simulation/Original_Algorithm/old1cm.out', 'r') as file2:
            lines1 = file1.read()
            lines2 = file2.read()

            height_list1 = lines1.split("\n")
            height_list2 = lines2.split("\n")

            del height_list1[len(height_list1)-1]
            del height_list2[len(height_list2)-1]

            height_list1 = list(map(float, height_list1))
            height_list2 = list(map(float, height_list2))
            diff = height_list1[0] - height_list2[0]

            for i in range(len(height_list2)):
                height_list2[i] += diff

            x_list1 = list(range(len(height_list1)))
            x_list2 = list(range(len(height_list2)))

            plt.plot(x_list1,height_list1,'ro-',label='vision')
            plt.plot(x_list2,height_list2,'bo-',label='blind',alpha=0.36)

            plt.title('Simulation of Stair Climbing (stair height = 1 cm)')
            plt.xlabel('time iterations')
            plt.ylabel('Height (mm)')
            plt.legend()
            plt.show()
