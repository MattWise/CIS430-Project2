from __future__ import division,print_function

import Orange

import sil

DATA_FILE=r'../data/dataOccupancyPreprocessed.csv'
MAP_SHAPE=(8,8)

data=Orange.data.Table(DATA_FILE)

def iterate_over_map_shape(map_shape=MAP_SHAPE):
    if len(map_shape)==1:
        for i in range(map_shape[0]):
            yield i
    elif len(map_shape)==2:
        for i in range(map_shape[0]):
            for j in range(map_shape[1]):
                yield i,j

def make_net(map_shape=MAP_SHAPE, topology=0, neighbourhood=0, learning_rate=0.05, radius_ini=3, radius_fin=1, epochs=1000):
    # http://orange.readthedocs.io/en/latest/reference/rst/Orange.projection.som.html#Orange.projection.som.Solver

    som = Orange.projection.som.SOMLearner(map_shape=map_shape,
                                           topology=topology,
                                           neighbourhood=neighbourhood,
                                           learning_rate=learning_rate,
                                           radius_ini=radius_ini,
                                           radius_fin=radius_fin,
                                           epochs=epochs,
                                           initialize=Orange.projection.som.InitializeRandom)

    mp = som(data,progress_callback=print)
    print("Finished")

if __name__ == '__main__':
    # make_net(epochs=20)
    # print(data.domain)
    for i in data[:3]:
        print(i)