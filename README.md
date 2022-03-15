# Roller coasters
The goal of this project was to find what shape a roller coaster has to have to provide a constant centripetal force on the rider.

### What is centripetal force?
For an object to move in a circle, it must have an inward force applied on it. 
This is called a "center-seeking" or centripetal force. 
For an object of mass **m** moving at a velocity **v** in a circular path of radius **r**, the force **F** required to maintain this motion is given by <img src="https://render.githubusercontent.com/render/math?math=F = \frac{mv^2}{r}">.

### What shape does the loop have to be?
Before a roller coaster goes down, it must first go up. 
A roller coaster of mass **m** at a height **H** will have a potential energy **U** of <img src="https://render.githubusercontent.com/render/math?math=U = mgH"> where **g** is the gravitational acceleration on earth (about 9.801 m/s^2).

Then, let the roller coaster fall down. 
If we write the height of the roller coaster as a function of time **h(t)**, the new potential energy is <img src="https://render.githubusercontent.com/render/math?math=U(t) = mgh(t)">. 
However, by conservation of energy, the kinetic energy **K** will be <img src="https://render.githubusercontent.com/render/math?math=K = U_i - U(t)">. 
Recalling that our initial potential energy is <img src="https://render.githubusercontent.com/render/math?math=U_i = mgH">, and the formula for the kinetic energy of our roller coaster moving at velocity **v** is <img src="https://render.githubusercontent.com/render/math?math=K = \frac{1}{2}mv^2">, we get <img src="https://render.githubusercontent.com/render/math?math=K(t) = mgH - mgh(t) = \frac{1}{2}mv^2">. 

Define time is 0 to be when the roller coaster is at the lowest point on the track. 
Here, <img src="https://render.githubusercontent.com/render/math?math=U(t) = 0">, so <img src="https://render.githubusercontent.com/render/math?math=K = mgH">. 
Let the radius of curvature at this lowest point on the track be **R**. 
Then the centripetal force at time 0 is <img src="https://render.githubusercontent.com/render/math?math=F_{centripetal}(0) = \frac{mv^2}{R}">. 
Since <img src="https://render.githubusercontent.com/render/math?math=K = \frac{1}{2}mv^2">, we can write <img src="https://render.githubusercontent.com/render/math?math=F_{centripetal}(0) = \frac{2K(0)}{R} = \frac{2mgH}{R}">. 
Let the radius of curvature be **r(t)** other places along the loop. 
Then, the centripetal force at other places along the loop is <img src="https://render.githubusercontent.com/render/math?math=F_{centripetal}(t) = \frac{2K(t)}{r(t)} = \frac{2[mgH - mgh(t)]}{r(t)}">. 
To maintain a constant centripetal force, we require <img src="https://render.githubusercontent.com/render/math?math=F_{centripetal}(0) = F_{centripetal}(t)">, so we get <img src="https://render.githubusercontent.com/render/math?math=\frac{2mgH}{R} = \frac{2[mgH - mgh(t)]}{r(t)}">. 
A little rearranging gives <img src="https://render.githubusercontent.com/render/math?math=r(t) = \frac{R[H - h(t)]}{H}">. 

Therefore, we have the radius of curvature as a function of height. 
This restriction is all we need to construct a loop given the initial **H** and **R** conditions. 

### Creating the loop
The program creates the loop by starting at the bottom (when radius of curvature is **R**) and ensure that at each step, <img src="https://render.githubusercontent.com/render/math?math=r = \frac{R[H - h]}{H}">. Here is a sample output where **H = 100** and **R = 50**:

