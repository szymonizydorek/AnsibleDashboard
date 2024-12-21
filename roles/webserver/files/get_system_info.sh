#!/bin/bash
hostname=$(hostname)
cpu_load=$(uptime | awk '{ print $10 }')
disk_usage=$(df -h / | awk 'NR==2 {print $5}')
ram_usage=$(free -h | awk '/Mem:/ {print $3 "/" $2}')

echo "Hostname: $hostname"
echo "CPU Load: $cpu_load"
echo "Disk Usage: $disk_usage"
echo "RAM Usage: $ram_usage"
