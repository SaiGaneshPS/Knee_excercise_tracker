# Knee_excercise_tracker

## Description of program :
The following program keeps track of the number of reps a person performs with their knee excercise. A rep starts when the amount of bendedness of the knee is about 140 degrees and the rep only stops when the knee is set straight (angle = 0 degrees).

### Angle Calculation :
For this particular excercise we need to track the following areas :
1. Hip joint
2. Knee joint
3. Ankle joint

This is done using **MediaPipe** library which provides us with the landmark points of each and every joint. Out of which we need the coordinates of the hip,knee and ankle. 

![image](https://user-images.githubusercontent.com/60283852/175483300-8266f917-f7d1-43f9-9fb6-5446056f2ec3.png)

We will be finding the angle between three points (For the left leg, it would be **23, 25 and 27**) 

## Features of program :

1. The program can check for dummy or random frames in the input video and can remove them from the output video.
2. An 8 second timer is used for a complete rep, this timer can be adjusted by the user according to their wish.
3. Considers the knee shown closest towards the camera.

The output video can be found in the below link :
[Output Video](https://drive.google.com/file/d/1_lnyndeg1wzp4zYsSRCfSjWE4_yOBdOm/view?usp=sharing)
