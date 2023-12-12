# Python

# Script Name:                  Ops Challenge: Psutil
# Author:                       Kevin Hoang
# Date of latest revision:      12/09/2023
# Purpose:                      Python script with Psutil to fetch system information.
# Execution:                    OpsChallenge11.py
# Resources:                    https://github.com/KevinVanHoang/seattle-ops-301d10/tree/main/class-11/challenges
#                               https://psutil.readthedocs.io/en/latest/#id1
#                               https://christopherdoucette.medium.com/5-python-libraries-for-cyber-security-8f34f5f1e3b8
#                               https://www.geeksforgeeks.org/psutil-module-in-python/
#                               https://chat.openai.com/share/68e12ced-21c0-4742-8d09-29d9802e9d0e

import psutil

# Get CPU times
cpu_times = psutil.cpu_times()

# Print the CPU times
print(f"User Time: {cpu_times.user}")
print(f"System Time: {cpu_times.system}")
print(f"Idle Time: {cpu_times.idle}")

# Time spent waiting for I/O to complete
io_wait_time = cpu_times.iowait
print(f"Time spent waiting for I/O to complete: {io_wait_time}")

# Time spent for servicing hardware interrupts
irq_time = cpu_times.irq
print(f"Time spent for servicing hardware interrupts: {irq_time}")

# Time spent for servicing software interrupts
softirq_time = cpu_times.softirq
print(f"Time spent for servicing software interrupts: {softirq_time}")

# Time spent by other operating systems running in a virtualized environment
steal_time = cpu_times.steal
print(f"Time spent by other operating systems running in a virtualized environment: {steal_time}")

# Time spent running a virtual CPU for guest operating systems
guest_time = cpu_times.guest
print(f"Time spent running a virtual CPU for guest operating systems: {guest_time}")

# Time spent by normal processes executing in user mode
normal_user_time = cpu_times.user - irq_time - softirq_time
print(f"Time spent by normal processes executing in user mode: {normal_user_time}")

# Time spent by priority processes executing in user mode
# Note: The exact interpretation of "priority processes" may depend on the context of your system.
# For demonstration purposes, assuming priority processes are those with higher user time.
priority_user_time = cpu_times.user - normal_user_time
print(f"Time spent by priority processes executing in user mode: {priority_user_time}")

# Alternatively, you can get a summary
cpu_summary = psutil.cpu_times_percent()
print(f"CPU Usage Percentages: {cpu_summary}")
