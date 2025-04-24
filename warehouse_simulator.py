import os
import subprocess
import json
from datetime import datetime
import re

def save_robot_path(output, instance_code):
	# Parse the output to extract robot movements
	lines = output.split('\n')
	robot_paths = {}
	
	# Find the line containing the answer and combine with next line
	answer_line = None
	for i, line in enumerate(lines):
		if 'Answer:' in line and i + 1 < len(lines):
			print(f"Found Answer line: {line}")  # Debug print
			print(f"Next line: {lines[i+1]}")  # Debug print
			answer_line = line + " " + lines[i+1]
			break
	
	if not answer_line:
		print("No Answer line found in output")
		print("Output content:")
		print(output)
		return
	
	# Extract all occurs statements
	occurs_pattern = r'occurs\(object\(robot,(\d+)\),([^,]+),(\d+)\)'
	matches = list(re.finditer(occurs_pattern, answer_line))
	
	print(f"Found {len(matches)} matches")  # Debug print
	
	for match in matches:
		robot_id = match.group(1)
		action = match.group(2)
		time = match.group(3)
		
		print(f"Processing match: robot={robot_id}, action={action}, time={time}")  # Debug print
		
		if robot_id not in robot_paths:
			robot_paths[robot_id] = []
		
		robot_paths[robot_id].append({
			'time': int(time),
			'action': action
		})
	
	if not robot_paths:
		print("No robot paths found in the output")
		return
	
	# Sort paths by time for each robot
	for robot in robot_paths:
		robot_paths[robot].sort(key=lambda x: x['time'])
	
	# Create output directory if it doesn't exist
	if not os.path.exists('robot_paths'):
		os.makedirs('robot_paths')
	
	# Generate filename with timestamp
	timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
	filename = f'robot_paths/instance_{instance_code}_{timestamp}.json'
	
	# Save to JSON file
	with open(filename, 'w') as f:
		json.dump(robot_paths, f, indent=2)
	
	print(f"\nRobot paths saved to: {filename}")

flag = False
time = 10
instance_code = 1
 
while not flag:
	print()
	print(' |','code'.ljust(5), ' | ', 'Instance File'.ljust(8), "  |")
	print(' |:','-'*3, ':|:', '-'*15,':|')
	for i in range(1,6):
		print(' |', str(i).ljust(5), ' | ', 'inst'+str(i)+'.asp'.ljust(8), "  |")
	print()

	instance_code = input('Please enter the code for the instance file: ')
	if (instance_code.isdigit()) and (int(instance_code) in range(1,6)):
		flag = True
	else:
		print()
		print("-"*10, "ERROR", "-"*10)
		print("Please Enter a valid code")

print("\n\n")
print("-"*10, "RUNNING", "-"*10)
print("\n\n")

while flag:
	out = subprocess.Popen(['clingo', 'warehouse_logic.asp', os.path.join('simpleInstances','inst'+str(instance_code)+'.asp'), '-c', 'n='+str(time)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout,stderr = out.communicate()
	output = stdout.decode("utf-8")
	
	if 'UNSATISFIABLE' in output.split():
		time = time + 2
	else:
		flag = False
		print(output)
		# Save the robot paths
		save_robot_path(output, instance_code)