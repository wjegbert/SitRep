# SitRep
If you're like me, out of shape and stupid, then the agony of working out is only compounded by the fact that you have to count and remember numbers. Under the strain of physical activity, it's all too easy to forget which number comes after 6. That's why I created SitRep.

![logo](Logos/SITREPlogo.png)

This revolution in personal fitness leverages a cutting-edge computer vision library (OpenCV) and servicable Python code to track your face as you're doing sit-ups. Just put your laptop or webcam at your feet as you exercise, and the app will detect the number of times your face becomes visible, ie when your face is above your knees when doing a sit-up, it will count that as a repetition. A system bell will sound every time your face is detected, so you can be sure it is keeping the right count. I know what you're thinking: that seems like it will get really annoying really fast. But something you might not have considered: shut up.

![logo](Logos/SITREPlogo2.png)

## FAQs
Why does it take a few seconds for the program to start doing stuff?

There's a short convenience buffer when you start the program that allows you to get in position and prepare yourself mentally for the unnatural contortions your body is about to endure.

Why should I use this? 

Because you're too lazy to count, and you don't have any friends to spot you.

Do you have any updates planned?

The next version of this app will have a timeout feature where, if your face has not been detected within a certain amount of time, it will assume you are resting and will play .wav files of me calling you various abusive names.

I'm concerned about privacy. What measures do you take to ensure my data is secure and my webcam isn't being hijacked?

lol


![logo](Logos/Sitreplogo4.png)

## Installation
*On Windows*: Clone the repo and run the .py file. Make sure you have the latest version of OpenCV for Python 3 installed. If you don't, good luck with that. Also change the HAARPATH value to point to `data/haarcascades/haarcascade_frontalface_default.xml` in the Python module for OpenCV.


*On Mac and Linux*: lmao no.

![logo](Logos/Sitreplogo3.png)
