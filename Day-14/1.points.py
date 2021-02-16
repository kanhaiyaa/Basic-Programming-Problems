def fruits(values):

  results = dict()

  for point in values:

    results[point] = point[0]*2 + point[1]*3

  return results

fruits( [(2,3), (4,3), (4,7)] )