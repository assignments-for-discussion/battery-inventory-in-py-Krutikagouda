def count_batteries_by_health(present_capacities):
  """Counts the number of batteries in each health category.
  Args:
    present_capacities: A list of the present capacities of the batteries.
  Returns:
    A dictionary with the number of batteries in each health category.
  """
  healthy_count = 0
  exchange_count = 0
  failed_count = 0
  for soh in soh_list:
    if soh > 80:
      healthy_count += 1
    elif soh >= 65:
      exchange_count += 1
    else:
      failed_count += 1
  return {
    "healthy": healthy_count,
    "exchange": exchange_count,
    "failed": failed_count
  }
def test_bucketing_by_health():
  """Tests the count_batteries_by_health function."""
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 77]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")
if __name__ == '__main__':
  test_bucketing_by_health()
