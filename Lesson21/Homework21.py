from datetime import datetime

key = "Key TSTFEED0300|7E3E|0400"
filtered_lines = []
timestamps = []

with open("hblog.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    if key in line:
        filtered_lines.append(line)

        timestamp_index = line.find("Timestamp ")
        if timestamp_index != -1:
            time_str = line[timestamp_index + 10 : timestamp_index + 18]
            time_obj = datetime.strptime(time_str, "%H:%M:%S")
            timestamps.append(time_obj)

with open("hb_test.log", "w") as log_file:
    for i in range(len(timestamps) - 1):
        t1 = timestamps[i]
        t2 = timestamps[i + 1]
        diff = (t1 - t2).total_seconds()

        if 31 < diff < 33:
            log_file.write(f"{t1.time()} WARNING: heartbeat = {diff} sec\n")
        elif diff >= 33:
            log_file.write(f"{t1.time()} ERROR: heartbeat = {diff} sec\n")