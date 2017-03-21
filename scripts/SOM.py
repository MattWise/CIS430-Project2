from __future__ import division

import Orange

DATA_FILE=r'../data/dataOccupancyPreprocessed.csv'

som=Orange.projection.som.SOMLearner(map_shape=(8, 8), initialize=Orange.projection.som.InitializeRandom)
data=Orange.data.Table(DATA_FILE)
map = som(data)