import statistics

def moving_median(data, size):
  for i in range(len(data) - size + 1)
    window = data[i : i + size]
    
    yield statistics.median(window)
