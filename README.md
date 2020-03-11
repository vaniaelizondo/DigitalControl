# Digital Control Loop Simulator

This is a project I developed for my Digital Control course made in Python 3. The libraries I used were *tkinter*, *matplotlib.pyplot* and *numpy*. 
The scope of the project was to simulate a control system which can operate both manually and automatically. A control system regulates the behavior of other devices using control loops. The following diagram shows how the system operates.
![System Diagram](/images/SystemDiagram.png)

In order for the project to work, the following should be considered:
* Python version >= 3 installed 
* Install matplotlib, tkinter and numpy libraries
* Run the file as "python3 system.py"
* An interface with the name "Control system simulation" and a windows were the output will be graphed will be opened. 
* Select either the "Manual" or "Automatic" button to choose the system operation mode. 
* Give the value of mk (input) if the "Manual" mode is selected
* Give the value of Rk (reference) if the "Automatic" mode is selected
* Select either the "Zero order" or "First order" button to choose the system order.
* Give the values of the coefficients a1, a2, a3, a4, b0, b1, b2, b3, b4 and d if "Zero order" is selected. The following shows the equation used to compute the result.
![Zero Order Equation](/images/ZOH.png)
* Give the values of K, Tau y Theta if "First order" is selected.
* Select either the "PID" or "General Eq." button to choose the type of controller that will be applied to the system if the automatic mode is selected. 
* Give the values of Kp, TauI y TauD si se selecciona "PID". 
* Give the values of the coefficients alpha1, alpha2, alpha3, alpha4, beta0, beta1, beta2, beta3, beta4 if "General Eq." is selected. The following image shows the equation used to compute the result.
![General Equation](/images/GeneralEquation.png)
* Give the value of T (sampling time). **Do not leave this field empty**.
* Write the disturbances magnitudes if wanted.
* Click on "Start" to start the simulation.
* Click the "Apply" button below "Input disturbance" or "Output disturbance" at any time if disturbances are added to the output function c[k]. 
* Do not close the graphics window. 
* To end the simulation, click on the "Finish" button. 
