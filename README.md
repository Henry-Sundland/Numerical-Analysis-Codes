# Numerical Analysis Codes
 Codes that apply numerical analysis to solve differential equations or do integrations.

 ~ List of python codes placed here ~

 1.) Euler's Method Example and Implementation









 ~ Description of the Codes ~

 1.) Euler's Method Example : Euler's method is a numerical integration technique used for solving ordinary differential equations (ODEs). It is a straightforward and explicit method that falls under the category of first-order methods. Euler's method approximates the solution of an ODE by using the slope (derived from the differential equation) to take small, discrete steps from an initial condition. It is particularly useful for solving initial value problems where the value of the solution is known at a specific point. Euler's method is simple to implement but can be inaccurate and unstable for stiff equations or when large step sizes are used, making it more suitable for problems where high precision is not critical or the step size can be kept sufficiently small. code numerically solves the ordinary differential equation dy/dt = -2y using Euler's method. It initializes the problem with the given initial condition y(0)=1, and iteratively computes the solution over a specified time interval with a defined step size. The results of Euler's method are then compared with the analytical solution y = exp(-2t) by plotting both the numerical and analytical solutions. This visual comparison demonstrates the accuracy of Euler's method in approximating the true solution of the differential equation.
