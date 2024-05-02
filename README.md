# FinalProject
computer vision final project - object detection
## Motivation   
We chose the topic of object detection and motion detection for a surveillance camera primarily to explore the daily activities of a cat. Our aim is to gain insight s into their behaviors and movements throughout the day. For instance, the camera can identify if the cat is moving or staying still, For example, we can know if it is near its bowl or sleeping at different times. Corresponding labels and boxes can be generated with the input video. Subsequently, logs of the cat activity can be generated. We also implement a creative function that combining the power of deep learning unlocks the ability to get 3D models from a single image.   
The team expects to acquire substantial knowledge about background subtraction, handling noise, 3D Reconstruction, skills related to motion and object detection and hands-on experience in video processing.   
## Approach   
In this project, we implemented background subtraction, motion and object detection and 3D Reconstruction. Then we compared performance by different approaches.    

Background subtraction:   
We read and wrote frames from the video, then  computed the HDR image as an average of irradiance estimates from LDR images. In this task, we also improved our algorithm with a GMM-based background subtractor. Finally, we combined these frames and exported them as a mp4 format.    

Motion and Object detection:   
	
3D Reconstruction:    
We used Deep learning and Open3D software to implement this task. Firstly, we got the prediction from the model and prepared the depth image of open3d. We took the depth data and used it to make a point cloud of the space those images show. Then it took us from traditional image processing into the more advanced world of 3D modeling and visualization. We also kept tweaking numbers and modified algorithms. Therefore we improved the quality of the mesh. Finally, we  exported the grid and the OBJ file that can be shown to users.    

## Results   
Background subtraction:   

Motion and Object detection:   

3D Reconstruction: https://youtu.be/zLCXLwzasq8   
    
## Implementation details:  
In the project, we used python as the programming language. We used Matplotlib and numpy to implement the code, and used IPython.display to display video. We mainly use 3rd party libraries in the 3D Reconstruction task. For example, the environment requires PyTorch, Pillow, Transformers, and Open3D.    
Source: Key idea is from coursera 7.2 https://www.coursera.org/learn/cs-445/lecture/PfSFy/lesson-7-2-3-3d-reconstruction   
## Challenge / innovation:    
In our project,  the aim is to achieve 3D reconstruction using a single image, mimicking how humans perceive depth despite having two eyes. There was the challenge of addressing filtering out noise, estimating normals, and scraping out anomalies. We tried to use one model to generate the 3d object,  but we found it was loose and without boundaries. Therefore, we kept tweaking numbers and modified algorithms. Then we improved the quality of the mesh.   
In the following image, we can see there is a signature improvement between the original 3d object and the final version.    
#### Original version:
<img width="1440" alt="Screenshot 2024-05-02 at 14 19 41" src="https://github.com/uiuc-CS445/FinalProject/assets/42729082/aacc5dea-8f1f-40bd-a981-cd6a3af176ff">    

<img width="1440" alt="Screenshot 2024-05-02 at 14 19 01" src="https://github.com/uiuc-CS445/FinalProject/assets/42729082/98850ca0-c2fc-4c79-8758-18bcaf59c31c">    

#### Final Version:   

<img width="714" alt="Screenshot 2024-05-02 at 14 20 50" src="https://github.com/uiuc-CS445/FinalProject/assets/42729082/862a4be9-b7f9-4c12-94ae-febf215fc0b2">
<img width="1244" alt="Screenshot 2024-05-02 at 14 20 18" src="https://github.com/uiuc-CS445/FinalProject/assets/42729082/a83dd724-4867-4cde-8035-56a29c508f36">
<img width="1440" alt="Screenshot 2024-05-02 at 14 20 05" src="https://github.com/uiuc-CS445/FinalProject/assets/42729082/df1a2828-0eb5-438d-968d-a3401c35f7b6">



