# FinalProject
Computer vision final project - background subtraction, handling noise, 3D Reconstruction, skills related to motion and object detection and hands-on experience in video processing   
In the project, we used python and requirement enviornment was wroted in utils.requirenments.txt
## Motivation   
We chose the topic of object detection and motion detection for a surveillance camera primarily to explore the daily activities of a cat. Our aim is to gain insights into their behaviors and movements throughout the day. For instance, the camera can identify the cat when the cat is moving in the camera's sight. Additionally, activities of the cat can be detected. For example, we can know if it is near its bowl to get food. Corresponding labels and boxes can be generated with the input video. We also implement a creative function that combining the power of deep learning unlocks the ability to get 3D models from a single image.
The team expects to acquire substantial knowledge about background subtraction, handling noise, 3D Reconstruction, skills related to motion and object detection and hands-on experience in video processing.

## Approach   
In this project, we implemented background subtraction, motion and object detection and 3D Reconstruction. Then we compared performance by different approaches.

Background subtraction:
We  read and wrote frames from the video, then started from basic background identification and removal to more advanced techniques to improve the outcome, for example, reducing noise, reducing the effect of shadows. The basic method is to use a method of gaussian blur and threshold with background subtraction, which would give the basic result of the foreground. To enhance the output with less noise and more connectivity of the foreground object, the erode and dilate technique is deployed. Further improvement is made by using KNN to improve the correctness of background, minimize shadow influence, take incoming then stayed still object as part of new background for example deformed sofa and also utilizing minor white object identification and removal. KNN learns the background alignment with new incoming frames.  Each approach’s result is attached at the Results section.


Motion and Object detection:
In this task, we focused on cat detection and eating food detection. We first continued from the background subtraction method to correctly identify the moving cat in the above example.
We read and wrote frames from the video and selected a background image. Then we put those frames into task 1 to get the background subtraction video. Based on task 1, iterated over each image file in the folder and checked the white regions with areas greater than or equal to the threshold. Therefore, we achieved the goal of object detection.
Similar to cat detection, we continued from background subtraction,  reading and writing frames into the video, converting BGR to RGB and getting the background subtraction video . Then we draw the mask with a bowl area, and check the white regions with areas greater than or equal to the threshold in the mask. Finally, we achieved the goal of eating detection. Similarly, results of this section are attached in the results section.
	
3D Reconstruction: 
We used Deep learning and Open3D software to implement this task. Firstly, we got the prediction from the model and prepared the depth image of open3d. We took the depth data and used it to make a point cloud of the space those images show. Then it took us from traditional image processing into the more advanced world of 3D modeling and visualization. We also kept tweaking numbers and modified algorithms. Therefore we improved the quality of the mesh. Finally, we  exported the grid and the OBJ file that can be shown to users. 

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
 
    
## Implementation details:  
In the project, we used python as the programming language. We used Matplotlib and numpy to implement the code, and used IPython.display to display video. We mainly use 3rd party libraries in the 3D Reconstruction task. For example, the environment requires PyTorch, Pillow, Transformers, and Open3D.    
Source: Key idea is from coursera 7.2 https://www.coursera.org/learn/cs-445/lecture/PfSFy/lesson-7-2-3-3d-reconstruction   
## Challenge / innovation:    
In our project the first section is using a hybrid way of implementing background subtraction and object detection. The implementation started off with a basic way of background subtraction and object identification. Then more complex techniques were used including morphological operations like erosion and dilation, neural network techniques like KNN and shadow removal. Correctness of background with this mixed techniques is greatly improved, minimizing shadow influence, taking incoming moving but then staying still object as part of new background like deformed sofa and also utilizing minor white object identification and removal. Hybriding these techniques greatly improved the correctness and  could handle a more complex environment, which makes this innovative.
In the second part of our project,  the aim is to achieve 3D reconstruction using a single image, mimicking how humans perceive depth despite having two eyes. There was the challenge of addressing filtering out noise, estimating normals, and scraping out anomalies. We tried to use one model to generate the 3d object,  but we found it was loose and without boundaries. Therefore, we kept tweaking numbers and modified algorithms. Then we improved the quality of the mesh.
In the following image, we can see there is a signature improvement between the original 3d object and the final version.

#### Original version:
<img width="1440" alt="Screenshot 2024-05-02 at 14 19 41" src="https://github.com/uiuc-CS445/FinalProject/assets/42729082/aacc5dea-8f1f-40bd-a981-cd6a3af176ff">    

<img width="1440" alt="Screenshot 2024-05-02 at 14 19 01" src="https://github.com/uiuc-CS445/FinalProject/assets/42729082/98850ca0-c2fc-4c79-8758-18bcaf59c31c">    

#### Final Version:   

<img width="714" alt="Screenshot 2024-05-02 at 14 20 50" src="https://github.com/uiuc-CS445/FinalProject/assets/42729082/862a4be9-b7f9-4c12-94ae-febf215fc0b2">
<img width="1244" alt="Screenshot 2024-05-02 at 14 20 18" src="https://github.com/uiuc-CS445/FinalProject/assets/42729082/a83dd724-4867-4cde-8035-56a29c508f36">
<img width="1440" alt="Screenshot 2024-05-02 at 14 20 05" src="https://github.com/uiuc-CS445/FinalProject/assets/42729082/df1a2828-0eb5-438d-968d-a3401c35f7b6">



