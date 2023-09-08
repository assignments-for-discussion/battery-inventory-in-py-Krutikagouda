def count_batteries_by_health(present_capacities):
  """Counts the number of batteries in each health category.
  Args:
    present_capacities: A list of the present capacities of the batteries.
  Returns:
    A dictionary with the number of batteries in each health category.
  """
  # Initialize the counts for each health category.
  counts = {
      "healthy": 0,
      "exchange": 0,
      "failed": 0
  }
  # Iterate over the present capacities and increment the count for the
  # appropriate health category.
  for capacity in present_capacities:
    if capacity > 80:
      counts["healthy"] += 1
    elif capacity >= 65:
      counts["exchange"] += 1
    else:
      counts["failed"] += 1
  # Return the counts.
  return counts
def get_present_capacities():
  """Gets the present capacities of the batteries from the user.
  Returns:
    A list of the present capacities of the batteries.
  """
  # Prompt the user to enter the present capacities of the batteries.
  present_capacities = input("Enter the present capacities of the batteries, separated by commas: ").split(",")
  # Convert the present capacities to integers.
  present_capacities = [int(capacity) for capacity in present_capacities]
  # Return the present capacities.
  return present_capacities
def main():
  """Counts the number of batteries in each health category."""
  # Get the present capacities of the batteries from the user.
  present_capacities = get_present_capacities()
  # Count the number of batteries in each health category.
  counts = count_batteries_by_health(present_capacities)
  # Print the counts.
  print(counts)
if __name__ == "__main__":
  main()
