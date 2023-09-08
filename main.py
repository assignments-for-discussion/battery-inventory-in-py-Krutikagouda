def count_batteries_by_health(present_capacities):
    healthy_count = 0
    exchange_count = 0
    failed_count = 0

    for capacity in present_capacities:
        rated_capacity = 120  # Assume all batteries have a rated capacity of 120 Ah
        soh = (capacity / rated_capacity) * 100

        if soh > 80:
            healthy_count += 1
        elif 65 <= soh <= 80:
            exchange_count += 1
        else:
            failed_count += 1

    return {
        "healthy": healthy_count,
        "exchange": exchange_count,
        "failed": failed_count
    }

def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [115, 118, 80, 95, 91, 77]
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1
    print("Done counting :)")

if __name__ == '__main__':
    test_bucketing_by_health()

