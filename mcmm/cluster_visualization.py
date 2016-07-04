import clustering as cl
import numpy as np
from sklearn.datasets import make_classification
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class ClusterViz(object):
    '''
    Class serving as a wrapper for matplotlib corresponding with mcmm.clustering classes to provide
    visualiziation defaults.
    '''

    def __init__(self,cluster_object):
        self._cluster_object = cluster_object
        if not self._cluster_object.fitted:
            cluster_object.fit()

    def scatter(self,feature_indices=None,mark_centers = True,color_clusters=False,sample_rate=20):
        '''
        Produces a scatter plot of the data stored in the cluster object.
        Args:
            feature_indices: indices of the features which should be plotted.
                Possible Arguments:
                    A list containing 2 or 3 indices denoting the feature indices in the data which should
                    be incorporated to the plot,
                    None. Falls back to plotting all features of the data and produces an error if number of features is
                    not 2 or 3.
            mark_centers:
            color_clusters:
            sample_rate: int. Steps in which the underlying data is sampled, i.e. "20" corresponds to plotting of every
            20th observation from the data
        '''

        if feature_indices is None:
            n_features = self._cluster_object.data.shape[1]
            feature_indices = range(self._cluster_object.data.shape[1])
        elif type(feature_indices) is list:
            n_features = len(feature_indices)
        else:
            raise TypeError('feature_indices needs to be a list or None')

        if color_clusters:
            c_ = np.append(self._cluster_object.cluster_labels)
        else:
            c = 'grey'

        if n_features == 2:
            fig = plt.figure()
            x = self._cluster_object.data[::sample_rate,feature_indices[0]]
            y = self._cluster_object.data[::sample_rate,feature_indices[1]]
            plt.scatter(x,y,c=c)
            if mark_centers:
                x = self._cluster_object.cluster_centers[:,feature_indices[0]]
                y = self._cluster_object.cluster_centers[:,feature_indices[1]]
                plt.scatter(x,y,c='r',s=50)
        plt.show()

#-------------------------------
# cluster test visualizations
#-------------------------------
def kmeans_blobs_2d(n_samples,n_clusters,k,method='kmeans++',std=1):
    '''
    generates random dataset by sklearn.datasets.samplesgenerator.make_blobs
    and visualizes the mcmm.analysis.KMeans clustering algorithm via pyplot

        Args:
        n_samples: number of observations in dataset
        n_clusters: number of clusters in dataset
        k: number of cluster centers to be determined by k-means
        method: the KMeans method, i.e. 'forgy' or 'kmeans++'
        std: the cluster intern standard deviation of the generated dataset
    '''

    data = make_blobs(n_samples,2,n_clusters,cluster_std=std)[0]
    kmeans = cl.KMeans(data,k,method)
    cluster_centers = kmeans.cluster_centers
    cluster_labels = kmeans.cluster_labels

    plt.scatter(data[:, 0], data[:, 1],c=cluster_labels)
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='r', s=50)
    plt.show()


def kmeans_blobs_3d(n_samples,n_clusters,k,method='kmeans++',std=1):
    '''
    generates random dataset by sklearn.datasets.samplesgenerator.make_blobs
    and visualizes the mcmm.analysis.KMeans clustering algorithm via pyplot

        Args:
        n_samples: number of observations in dataset
        n_clusters: number of clusters in dataset
        k: number of cluster centers to be determined by k-means
        method: the KMeans method, i.e. 'forgy' or 'kmeans++'
        std: the cluster intern standard deviation of the generated dataset
    '''

    data = make_blobs(n_samples,3,n_clusters,cluster_std=std)[0]
    kmeans = cl.KMeans(data,k,method)
    cluster_centers = kmeans.cluster_centers
    cluster_labels = kmeans.cluster_labels

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(data[:, 0], data[:, 1],data[:,2],c=cluster_labels)
    ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1],cluster_centers[:,2], c='r', s=150,depthshade=False)
    plt.show()