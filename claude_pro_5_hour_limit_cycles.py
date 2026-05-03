"""
5-Hour Cycle Tracker

Purpose
-------
This script tracks a repeating 5-hour cycle that started at a known
datetime (for example: 2026-05-03 12:00:00).

The script can be run at any time and it will:
1. Read the last known cycle start from a file.
2. Calculate how many 5-hour cycles have passed until the current time.
3. Determine:
   - the last completed cycle
   - the next upcoming cycle
   - the remaining time until the next cycle
4. Print a recommended working window:
   from (next_cycle - 1 hour) to (next_cycle + 1 hour).
5. Update the stored cycle start in the file if newer cycles have passed.
6. Wait for the user to press Enter before closing.

File
----
cycle_start.txt

The file stores the last known cycle start time in the format:
YYYY-MM-DD HH:MM:SS
"""

from datetime import datetime, timedelta
import os

FILE_NAME = "cycle_start.txt"
CYCLE_HOURS = 5


# ------------------------------------------------------------
# STEP 1: Load the starting cycle time
# ------------------------------------------------------------
if not os.path.exists(FILE_NAME):

    start_time = datetime(2026, 5, 3, 12, 0)

    with open(FILE_NAME, "w") as f:
        f.write(start_time.strftime("%Y-%m-%d %H:%M:%S"))

else:
    with open(FILE_NAME, "r") as f:
        start_time = datetime.strptime(
            f.read().strip(),
            "%Y-%m-%d %H:%M:%S"
        )


# ------------------------------------------------------------
# STEP 2: Get current time
# ------------------------------------------------------------
now = datetime.now()


# ------------------------------------------------------------
# STEP 3: Calculate cycle duration
# ------------------------------------------------------------
cycle_duration = timedelta(hours=CYCLE_HOURS)

elapsed = now - start_time

cycles_passed = elapsed // cycle_duration


# ------------------------------------------------------------
# STEP 4: Determine cycle boundaries
# ------------------------------------------------------------
last_cycle = start_time + cycles_passed * cycle_duration

next_cycle = last_cycle + cycle_duration

remaining = next_cycle - now


# ------------------------------------------------------------
# STEP 5: Calculate best working window
# ------------------------------------------------------------
best_start = next_cycle - timedelta(hours=1)
best_end = next_cycle + timedelta(hours=1)


# ------------------------------------------------------------
# STEP 6: Print results (clean formatting)
# ------------------------------------------------------------

remaining_str = str(remaining).split(".")[0]

print("\n===== Cycle Information =====")
print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Last cycle start:", last_cycle.strftime("%Y-%m-%d %H:%M:%S"))
print("Next cycle start:", next_cycle.strftime("%Y-%m-%d %H:%M:%S"))
print("Remaining time:", remaining_str)

print(
    f"\nBest Working Times is from "
    f"{best_start.strftime('%H:%M:%S')} "
    f"to {best_end.strftime('%H:%M:%S')}"
)
# ------------------------------------------------------------
# STEP 7: Update stored cycle start if needed
# ------------------------------------------------------------
if last_cycle > start_time:
    with open(FILE_NAME, "w") as f:
        f.write(last_cycle.strftime("%Y-%m-%d %H:%M:%S"))


# ------------------------------------------------------------
# STEP 8: Wait before closing
# ------------------------------------------------------------
input("\nPress ENTER to close the program...")
