# Bash Log Analyzer Task (TerminalBench Sample)

# Description
A deterministic Bash CLI task where the agent must fix the log analyzer to correctly report top IP counts.

# Usage

Build:

sh
sudo docker-compose build

sudo docker-compose run --rm task
---- 
Expected Output
4 10.0.0.1
3 10.0.0.2
3 10.0.0.3
