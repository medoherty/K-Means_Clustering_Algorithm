# K-means_Algorithm
Custom implementation of the K-Means Clustering Algorithm

This project implements the K-means Clustering Algorithm. The user selects which data to use, and this is loaded from a csv file. The user then chooses how many clusters to use and the number of iterations. The initial centroids are randomly selected, but the subsequent ones are calculated using the mean of the x and y values of data points belonging to the relevant cluster.

The algorithm is implemented by calculating the Euclidean distance between two points, and this function is used to calculate the distance from every point to each centroid and then labelling every data point according to which centroid is the closest to it. The mean of all the x and y values of data points belonging to each centroid/cluster are then calculated to find the new centroids. This is done for however many iterations were chosen. The result is then visualised as a scatter plot. Each cluster is shown in a different colour, with each centroid marked with a black cross.
