# FinalProject
Computer vision final project - background subtraction, handling noise, 3D Reconstruction, skills related to motion and object detection and hands-on experience in video processing   
   
## Organization   
Group Member: Shiqi Liu(shiqi6),Chaobo Cai (chaoboc2)   
   
## Motivation   
We chose the topic of object detection and motion detection for a surveillance camera primarily to explore the daily activities of a cat. Our aim is to gain insights into their behaviors and movements throughout the day. For instance, the camera can identify the cat when the cat is moving in the camera's sight. Additionally, activities of the cat can be detected. For example, we can know if it is near its bowl to get food. Corresponding labels and boxes can be generated with the input video. We also implement a creative function that combining the power of deep learning unlocks the ability to get 3D models from a single image.
The team expects to acquire substantial knowledge about background subtraction, handling noise, 3D Reconstruction, skills related to motion and object detection and hands-on experience in video processing.
   
## Setup   
In the project, we used python and requirement enviornment was wroted in utils.requirenments.txt
conda install pytorch::pytorch torchvision torchaudio -c pytorch //for mac
https://pytorch.org/get-started/locally/
pip install matplotlib
pip install transformers 
pip install pillow
pip install open3d

## Approach   
In this project, we implemented background subtraction, motion and object detection and 3D Reconstruction. Then we compared performance by different approaches.   
Background Subtraction: We removed the background from video frames using techniques like Gaussian blur and thresholding, then refined it with erosion, dilation, and KNN for better accuracy and noise reduction.   
Motion/Object Detection: We detected moving objects like cats and food by analyzing white regions in video frames, building on the background subtraction method.   
3D Reconstruction: We used deep learning and Open3D to create a 3D model from 2D image data, refining it for quality and exporting it for user viewing.    
 
    
## Implementation details:  
In the project, we used python as the programming language. We used Matplotlib and numpy to implement the code, cv2 processed image and its default KNN model for results improval and IPython.display to display video. We mainly use 3rd party libraries in the 3D Reconstruction task. For example, PyTorch for the deep learning package, Pillow, Transformers, and Open3D.    

## Results   
We have 3 samples of background subtraction, motion & object detection.   
Background subtraction:   
Original version(threshold background subtraction with gaussian blur) - sample 1: https://youtu.be/Qc7Utkhj5GI   
Original version(threshold background subtraction with gaussian blur and erode dilate) - sample 1: https://youtu.be/8UDBfktH8-g   
Improved version(with knn) - sample 1: https://youtu.be/BGnPxPXnDLU   
Improved version(with knn) - sample 2: https://youtu.be/AU1F6q-eKVw   
Improved version(with knn) - sample3:https://youtube.com/shorts/0P1rAAZ2vSI?feature=share   
Motion and Object detection:   
 	Sample 1: https://youtu.be/wdkrKZ0cOXA   
	Sample 2:https://youtu.be/DtsX5CG61c8   
	Sample 3:https://youtube.com/shorts/YBChinVjcJQ?feature=share   
	Check eating: https://youtube.com/shorts/QfQ8Z7vvk6I?feature=share   
   
3D Reconstruction: https://youtu.be/zLCXLwzasq8 
### File Structure:
In this project, we use Juypter and python.   
#### Reference: 
Key idea is from coursera 7.2 https://www.coursera.org/learn/cs-445/lecture/PfSFy/lesson-7-2-3-3d-reconstruction   
https://stackoverflow.com/questions/4902491/tips-for-background-subtraction-in-the-face-of-noise   
https://www.southampton.ac.uk/~msn/book/new_demo/gaussian/#:~:text=The%20Gaussian%20Smoothing%20Operator%20performs,how%20large%20the%20template%20is.   
https://docs.opencv.org/3.4/db/df6/tutorial_erosion_dilatation.html   
https://stackoverflow.com/questions/55853994/how-to-remove-shadows-from-a-video-that-has-static-background  
https://docs.opencv.org/4.x/db/d88/classcv_1_1BackgroundSubtractorKNN.html#details  
​​https://www.geeksforgeeks.org/transform-a-2d-image-into-a-3d-space-using-opencv/   
Install PyTorch environment: https://pytorch.org/get-started/locally/   
https://chat.openai.com/   




