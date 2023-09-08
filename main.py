def compute_soh(present_capacity, rated_capacity):
    """Compute the state-of-health (SoH) of a battery."""
    return (present_capacity / rated_capacity) * 100

def classify_batteries(present_capacities):
    """Classify batteries by SoH and count them in each category."""
    # Initialize counters for healthy, exchange, and failed batteries
    healthy_count = 0
    exchange_count = 0
    failed_count = 0

    # Rated capacity of a new battery
    rated_capacity = 120

    # Loop through each battery's present capacity
    for capacity in present_capacities:
        # Calculate the SoH percentage
        soh = compute_soh(capacity, rated_capacity)

        # Classify the battery based on SoH
        if soh > 80:
            healthy_count += 1
        elif 65 <= soh <= 80:
            exchange_count += 1
        else:
            failed_count += 1

    # Return the counts as a dictionary
    return {
        "healthy": healthy_count,
        "exchange": exchange_count,
        "failed": failed_count
    }

def test_bucketing_by_health():
    """Tests the classify_batteries function."""
    print("Classifying batteries by SoH...\n")
    present_capacities = [115, 118, 80, 95, 91, 77]
    counts = classify_batteries(present_capacities)
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1
    print("Healthy batteries:", counts["healthy"])
    print("Exchange batteries:", counts["exchange"])
    print("Failed batteries:", counts["failed"])
    print("Done classifying :)")


if __name__ == '__main__':
    test_bucketing_by_health()
