'''
853. Find Most Occurring IP Address in Log File (Easy) -- Goldman Sachs

Write a function that processes a log file and identifies the most frequently occurring IP address.
Each line includes an IP address followed by other unrelated data, separated by hyphens.

Example 1:
Input:
111.33.44.55-hello-787-test
111.33.44.55-hello-787-test
112.53.47.45-reemag-787-teskkkt
Output: 111.33.44.55

Example 2:
Input:
192.168.1.1-info-123-data
10.0.0.1-update-124-info
192.168.1.1-info-123-data
192.168.1.1-info-123-data
Output: 192.168.1.1

HashMap -- O(n) time, O(n) space
Split each line on the first hyphen to extract the IP, count frequencies with a hashmap, return the max.
'''

#Time Complexity: O(n)
#Space Complexity: O(n)
def most_frequent_ip(log_lines):
    hash_map = {}
    for line in log_lines:
        ip = line.split('-')[0]
        if ip in hash_map:
            hash_map[ip] = hash_map[ip] + 1
        else:
            hash_map[ip] = 1

    result = ""
    max_count = 0
    for ip, count in hash_map.items():
        if count > max_count:
            max_count = count
            result = ip
    return result
