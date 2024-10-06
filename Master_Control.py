import subprocess
import os

# Path to your scripts
data_acquisition_script = os.path.join(os.getcwd(), 'data_aquisition.py')
chart_creation_script = os.path.join(os.getcwd(), 'Chart_Creation.py')

# Function to run a script
def run_script(script_name):
    try:
        subprocess.run(['python3', script_name], check=True)
        print(f"{script_name} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_name}: {e}")

# Run data acquisition script first
run_script(data_acquisition_script)

# Then run chart creation script
run_script(chart_creation_script)
