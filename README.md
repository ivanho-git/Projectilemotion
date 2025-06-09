🎯 Projectile Motion Simulator
A Python program that simulates the trajectory of a projectile using turtle graphics and plots kinetic energy over time using matplotlib. It combines physics and visual programming for a fun learning experience!

📌 Features
Animates projectile trajectory using Turtle graphics

Plots Kinetic Energy vs Time using Matplotlib

Based on user input for velocity and angle

Physics-based calculation using real-world formulas

Displays both motion path and energy variation

🧠 Physics Background
The projectile follows the equations:

Horizontal position:
x = v₀ * cos(θ) * t

Vertical position:
y = v₀ * sin(θ) * t - 0.5 * g * t²

Kinetic Energy:
KE = 0.5 * m * v² (calculated only for vertical motion component)

💻 Dependencies
Python 3.x

matplotlib

Install the dependency:

bash
Copy
Edit
pip install matplotlib
🚀 How to Run
Clone the repository or download the script.

Run the script using:

bash
Copy
Edit
python projectile_simulator.py
Enter:

Initial velocity (in m/s)

Angle of projection (in degrees)

The turtle window will display the trajectory, followed by a matplotlib graph of Kinetic Energy vs Time.

🔍 Sample Output
Turtle Window
Displays the path of the projectile in red.

Matplotlib Graph
Plots a curve showing how vertical kinetic energy changes over time.


🛠️ Customization Ideas
Add air resistance

Show total energy (kinetic + potential) over time

Include real-time animation

Add user-friendly GUI for input

📄 License
This project is licensed under the MIT License.

🙌 Contributions
Feel free to fork, modify, and submit pull requests! Whether you're improving the physics or making the visuals cooler — contributions are always welcome.

