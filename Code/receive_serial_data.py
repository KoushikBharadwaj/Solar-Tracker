import serial
import time
import matplotlib.pyplot as plt

# Establish serial connection (change the port and baud rate as needed)
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's serial port

# Initialize lists to store data
ldr1_values = []
ldr2_values = []
servo_angles = []
timestamps = []

# Setup for plotting and text display
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot setup for LDR readings
ax1.set_title('LDR Readings')
ax1.set_xlabel('Time')
ax1.set_ylabel('Value')
ax1.grid(True)

# Plot setup for Servo angle
ax2.set_title('Servo Angle')
ax2.set_xlabel('Time')
ax2.set_ylabel('Angle')
ax2.grid(True)

# Display text setup
text_disp = ax1.text(0.02, 0.95, '', transform=ax1.transAxes, verticalalignment='top')

# Main loop to read and plot data
try:
    while True:
        if ser.in_waiting > 0:
            # Read data from Arduino
            data = ser.readline().decode().strip()
            
            # Parse the data
            if data.startswith('LDR1:'):
                parts = data.split(',')
                ldr1_value = int(parts[0].split(':')[1])
                ldr2_value = int(parts[1].split(':')[1])
                angle_value = int(parts[2].split(':')[1])
                timestamp = time.time()  # Timestamp for x-axis
                
                # Append data to lists
                ldr1_values.append(ldr1_value)
                ldr2_values.append(ldr2_value)
                servo_angles.append(angle_value)
                timestamps.append(timestamp)
                
                # Update plot
                ax1.plot(timestamps, ldr1_values, label='LDR1', color='b')
                ax1.plot(timestamps, ldr2_values, label='LDR2', color='g')
                ax2.plot(timestamps, servo_angles, label='Servo Angle', color='r')
                
                # Update text display
                text_disp.set_text(f"LDR1: {ldr1_value}\nLDR2: {ldr2_value}\nAngle: {angle_value}")
                
                # Adjust plot limits for better visualization (optional)
                ax1.set_xlim(max(0, timestamp - 10), timestamp + 1)  # Adjust x-axis limit to show last 10 seconds
                ax2.set_xlim(max(0, timestamp - 10), timestamp + 1)
                
                # Draw the plot
                fig.tight_layout()
                plt.pause(0.01)
        
except KeyboardInterrupt:
    print("Program interrupted. Exiting...")

finally:
    ser.close()  # Close serial port
    print("Serial connection closed.")
