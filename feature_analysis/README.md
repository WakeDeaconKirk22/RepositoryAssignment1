# ## SIFT Feature Analysis 

Transparency : Portions of the code was generated with Copilot then modified by me and commented to show understanding 


## PART 1  Blob detection 

After visualizing the detected SIFT keypoints, i observed that larger circles were drawn around larger blobs while smaller circle were drawn around smaller features. I did find that some keypoints were missing in low contrast region where intensity changes were minimal. Also found random or incorrect keypoints. This shows SIFT DoG is good for scaled but it could be improved by a threshold .


Image:
<img width="315" height="409" alt="Part1" src="https://github.com/user-attachments/assets/f8945e86-c353-4e2c-b7bd-e60ed35233cc" />



## PART 2 Tuning 

This I found out what parameters such as contrast threshold,sigma and edge threshold did for blob detection and also the correct ranges for each of these. Contrast threshold filters out weak features in low contrast regions a lower value (0.1) detects more keypoints while higher value detects fewer. edge threshold filters out edge like feature. A higher value allows more edge like features to be detected while a lower value(5) suppresses them. Sigma controls the amount of gaussian blur applied to the image at the first octabe. This affects the scale at which features are detected. Overall the paramets control how the SIFT filters improving from the issues of part 1 such as keypoints missing or errors in keypoints.

Image:
<img width="315" height="409" alt="Part2" src="https://github.com/user-attachments/assets/c162c8b1-0527-4f4c-aa00-97796f93416f" />


## PART 3 Descriptors 

In this I learned that a descriptor is like footprint of an image region. It summarizes brightness changes in different directions aroundd a point. So when being compared to different images it can be recognized by it similar features because it saves relative orientation distrubutions. With analyzing histogram we can see how texture and orientation pattern are encoded numerically. 

Chat gpt explained that a 128 dimensional is a 16x16 patch with a 4x4 subregions that computes a 8 bin histogram. Each value in this vector show how strong a certain orientation is in a particular part of the patch. 


Chat Gpt provided this as an example of what an SIFT descriptor may look like: 
 [0.0, 0.1, 0.3, 0.6, 0.8, 0.2, 0.0, 0.0, 
 0.2, 0.5, 0.7, 0.6, 0.3, 0.1, 0.0, 0.0, 
 ...
 0.1, 0.4, 0.7, 0.5, 0.2, 0.0, 0.0, 0.0]

This describe the image region around a keypoint. This is where gradient direction and magnitude of all pixels and measured it is then grouped into 8 bins based on it orientation. The high values in 90 degrees suggest strong vertical edges, 0 degreesindicate horizontal edges while a mix of bins suggest corner or textured regions. 

With my histogram it shows a part of the 4x4 subregions along with the height of the bars and how promient certain edge directions are. The histogram has multiple high values in each bin which suggests this might be a textured region. 



Image: 

<img width="389" height="409" alt="Part3 1" src="https://github.com/user-attachments/assets/7d208663-a4a8-4d22-82a5-2c0681fe30d0" />

Histogram:

<img width="790" height="788" alt="SIFTHisto" src="https://github.com/user-attachments/assets/bc3d5e2c-f20c-4129-9e22-eda3b9fa5c34" />


# PART 4 Feature Matching

For this i did a transformation with rotation around 30 and found 50 best matches. Using the transformed image and the orignal i detected SIFT keypints and computed their descriptors for both images. Then I employed BF matcher to find the best matches between descriptors from the original and transformed images. Through this I found that most matched keypoints correspond to the same physical features despite rotation being peformed. This showed how effective SIFT is. 




Image: 

<img width="515" height="350" alt="Part4" src="https://github.com/user-attachments/assets/5cf2dd4b-70ee-4409-a097-a8eaca3a7b99" />


