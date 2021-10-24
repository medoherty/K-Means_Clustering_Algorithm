# import the packages used in the program.

import numpy as np
import matplotlib.pyplot as plt
import csv


# The read_csv function that reads the CSV file is defined. It opens and reads the CSV file and uses a comma as a
# delimiter to separate the values, which are saved as the read dataset. All the values from the start of the second
# column onwards in the read dataset are converted to a list called list_convert. The values in the second and third
# columns are converted to floats and all the converted values in the list_convert list are thereafter saved as a list
# called list1. This list is returned.

def read_csv(file):
    with open(file, 'r') as csvfile:
        read = csv.reader(csvfile, delimiter=',')
        list_convert = list(read)[1:]
        list1 = [[r[0], float(r[1]), float(r[2])] for r in list_convert]
        return list1

# The function that calculates the Euclidean distance is defined, which takes two data points as attributes. The x and
# y variables are determined by these data points and are converted to floats. These variables are used to calculate
# the distance between the x values and the y values, which are then added together and the square route is then taken
# to calculate the final distance, which is returned.


def euclidean_dist(a, b):
    x1 = float(a[1])
    x2 = float(b[0])
    y1 = float(a[2])
    y2 = float(b[1])
    x_distances_squared = (x1 - x2) ** 2
    y_distances_squared = (y1 - y2) ** 2
    distance = np.sqrt(x_distances_squared + y_distances_squared)
    return distance

# A function called labels is defined that will be used to label the x and y values according to which centroid they
# are closest to. The function takes the dataset list and the list of centroids as attributes. An empty list called
# labels is defined and initialised. A nested for loop is used to run the Euclidean distance function for every centroid
# in the list in order to calculate the distances between the data points and the centroids. These distances are
# appended to the point_distances list. Then the minimum distance is calculated for all the data points, and the index
# value of every minimum value is calculated, and these index values are appended to the labels list, which is returned.


def labels(dataset, centroids):
    labels = []

    for data_point in dataset:
        point_distances = []

        for centroid in centroids:
            point_distances.append(euclidean_dist(data_point, centroid))

        min_value = min(point_distances)

        min_index = point_distances.index(min_value)

        labels.append(min_index)

    return labels

# The function that initialises the clusters is defined, and takes the dataset list and user-defined number of clusters
# (k) attributes. A list called centroids is defined and initialised. In a for loop, a random integer variable is
# selected between a minimum of 0 and a maximum being the length of the dataset. This us achieved by using the randint
# function from numpy. The x and y values in the dataset with this index value are then appended to the centroid list,
# and this list is then appended to the centroids list. This is repeated for however many centroids were chosen. The
# centroids list is then returned.


def init_cluster(dataset, k):
    centroids = []

    for i in range(k):
        centroid = []
        a = np.random.randint(0, len(dataset))
        random_x = dataset[a][1]
        centroid.append(random_x)
        random_y = dataset[a][2]
        centroid.append(random_y)
        centroids.append(centroid)

    return centroids

# The mean function is defined with the dataset list, labels list and a variable i as attributes. Empty lists for the
# x and y values to be used in calculating the means of x and y are defined and initialised. A while loop and if
# statement are used to append all x and y values that have the same label value (i) to the mean_x_list and mean_y_list.
# This means that all values appended to these list are closest to the same centroid. The sum of the mean_x_list and
# mean_y_list are calculated and the mean of each list is calculated by dividing by the length of each list. This is
# done in a try block so that if the calculated mean is zero that value is ignored. The means of the x and y values are
# returned. This is repeated for all label values (i) until the mean of all x and y values belonging to each centroid
# has been calculated.


def mean(dataset, labels, i):
    mean_x_list = []
    mean_y_list = []

    r = 0
    while r < len(labels):

        if labels[r] == i:
            mean_x_list.append(dataset[r][1])
            mean_y_list.append(dataset[r][2])
        r += 1

    sum_x_list = sum(mean_x_list)
    sum_y_list = sum(mean_y_list)

    try:
        mean_x = sum_x_list / len(mean_x_list)
        mean_y = sum_y_list / len(mean_y_list)

    except ZeroDivisionError:
        mean_x = 0
        mean_y = 0

    return mean_x, mean_y

# The function that plots the scatter plot is defined with the dataset list, number of centroids (k) and labels list
# attributes. An array called colours is created that contains all the colours to be used in the plot. In a similar way
# to the above mean function, the x and y values that have the same label (same cluster) are appended to the data_x and
# data_y lists, and their corresponding country name is appended to the countries_cluster list. This is done for all
# values for whichever cluster they belong to.


def plot_chart(dataset, k, labels):

    colours = np.array(["Blue", "Red", "Yellow", "Green", "Purple", "Pink", "Orange", "Brown", "Black", "Grey"])

    for i in range(k):

        data_x = []
        data_y = []
        countries_cluster = []

        r = 0

        while r < len(labels):

            if labels[r] == i:
                data_x.append(dataset[r][1])
                data_y.append(dataset[r][2])
                countries_cluster.append(dataset[r][0])
            r += 1

            # The results after running the algorithm are printed to the screen. The mean function is called in order
            # to calculate the mean birth rate and life expectancy.

        print("Number of countries belonging to cluster " + str(i + 1) + " = " + str(len(data_x)))

        print("Countries belonging to cluster " + str(i + 1) + " : \n" + str(countries_cluster))

        mean_x, mean_y = mean(dataset, labels, i)

        print("Mean birth rate for cluster " + str(i + 1) + " = " + str(mean_x))

        print("Mean life expectancy for cluster " + str(i + 1) + " = " + str(mean_y) + "\n")

        # The x and y values are plotted, with those belonging to the same label plotted in the same colour. The
        # centroids (means of x and y values with the same label) are then plotted in black. The title and labels of the
        # x and y axis are specified. The plot is then displayed.

        plt.scatter(data_x, data_y, c=colours[i], s=10, label=("Cluster " + str(i + 1)))

        plt.scatter(mean_x, mean_y, c="Black", marker='X', s=50)

        plt.xlabel('Birth Rate')
        plt.ylabel('Life Expectancy')

    plt.title('K-means Algorithm Scatter Plot')

    plt.legend()

    plt.show()

    return 0

# The function that runs the k-means algorithm is defined. It takes the dataset list, number of centroids (k) and
# number of iterations as attributes. It runs the function that initialises the clusters in order to get the first
# centroids and stores them in the centroids list. For every iteration, the mean function is called and the mean is
# calculated for all clusters and saved as new centroids in the centroids list. The labels function is also run in
# order to specify which x and y values belong to which centroid. The function that plots the data is then run. The
# centroids are returned.


def k_means_algorithm(dataset, k, iterations):
    centroids = init_cluster(dataset, k)

    for i in range(iterations):
        labels1 = labels(dataset, centroids)

        for j in range(k):
            centroids[j] = mean(dataset, labels1, j)

    labels1 = labels(dataset, centroids)
    plot_chart(dataset, k, labels1)

    return centroids

# The user is asked for input in order to determine which file (dataset) to use, the number of desired clusters and
# the number of iterations to run. the k_means_algorithm is then run and the centroids are stored in the centroids
# list.


file = input("Please enter the file name you want to use - data1953.csv, data2008.csv or dataBoth.csv: \n")
dataset1 = read_csv(file)

k = int(input("Please enter the number of clusters you want: "))

iterations = int(input("Please enter the number of iterations that the algorithm must run: "))

centroids = k_means_algorithm(dataset1, k, iterations)
