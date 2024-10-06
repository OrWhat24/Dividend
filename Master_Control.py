import subprocess

# Run the data acquisition script
print("Running data acquisition for Dividend Kings...")
subprocess.run(['python3', 'data_aquisition.py'])

# Run the chart creation script
print("Creating charts for Dividend Kings...")
subprocess.run(['python3', 'Chart_Creation.py'])

print("All tasks completed!")
