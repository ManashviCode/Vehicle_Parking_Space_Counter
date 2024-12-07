# Vehicle parking Space Detection

This project automatically detects empty parking spaces in a parking lot using surveillance camera footage. It works by extracting parking space coordinates, processing each space to determine if it's occupied or free, and displaying the results on the image.

 
## Example Results
![Result](https://github.com/user-attachments/assets/31418bc4-f2d4-4fef-b042-c3b4dfeb253d)

<p align="center">




## Problem Defination
- finding out the empty parking spaces in a car-parking-lot aotomatically from servillance camera.

## solution
- Extracting the parking lot coordinates form the image by car_park_coordinate_generator.py script.
- Then use this coordinates to processing every car parking space individualy.
- Implementing digital iamge processing techniques to find out the empty and occupied parking spaces.
- drawing the reults into the image. 

## Used The Concepts
- OOP concepts
- Opencv High Level GUI Programming
- Opencv Basic Image Processing
- Doc String
- Python Type Annotation



### Controlling with the project
- labelling   __car park__
    - you can click left  mouse button. It will draw the its order.
- removing the label __car park__
    - you will do same thing above with mouse middle button instead of clicking left mouse button.

- __Exit__ from the project
    - just click __q__ button on your keyboard. (When your Operating System Selected the project window)
- __Saving__ the results
    - just click __s__ button on your keyboard. (When your Operating System Selected the project window)

## Note 
- CarParkingPos  is a pickle file which stores the empty car parking positions.  The car park areas represented as rectangle and they stored with coordinate of  its top left point.
