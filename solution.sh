#!/usr/bin/env bash
LOG_FILE="logs/access.log"


cut -d ' ' -f 1 "$LOG_FILE" \
| sort \
| uniq -c \
| sort -k1,1nr -k2,2 \
| head -3 \
| awk '{print $1, $2}'
