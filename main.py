def count_batteries_by_health(present_capacities):



  counts = {
    "healthy":0,
    "exchange":0,
    "failed":0
  }
  for capacity in present_capacities:
    if capacity > 80:
      counts["healthy"] += 1
    elif capacity >= 65:
      counts["exchange"] += 1
    else:
      counts["failed"] += 1
  #Return the counts.
  return counts
def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  #create a list of present capacities.
  present_capacities = [115, 118, 80, 95, 91, 77]
  # call the count_batteries_by_health function and store the results in a variable.
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"]==2)
  assert(counts["exchange"]==3)
  assert(counts["failed"]==1)
  print("Done counting :)")
if __name__ == '__main__':
  test_bucketing_by_health()
