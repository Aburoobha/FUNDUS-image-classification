Image Classification using the FUNDUS dataset: https://www.kaggle.com/datasets/linchundan/fundusimage1000

After downloading, I'll explore the dataset to understand its structure and the types of images it contains. I have noticed from the first few images and concluded that the given images are in .jpg format

What I am going to do :
1) Preprocess the Data -> resize, normalization and split the dataset for training and testing
2) Build and Train a Model -> choose and train a model. (More likely to build CNN, but I explore some other)
3) Evaluation -> performance measure
4) Visualization ->Through the help of python/R
5) Consideration of other model or tuning the parameters of cnn model to increase the accuracy

### FUNDUS
The term "fundus" typically refers to the bottom or base of something. In medical contexts, it often specifically refers to the bottom or interior surface of an organ, such as the fundus of the eye or the fundus of the uterus.

### THE PROCESS or THE PROGRESS I COME THROUGH:
After downloading the dataset, I explore it. By analyzing them, I realised that they are catergorized based on 0-29 and sub - catergorized by .1 - .9. which is very new to me. I learned using 'os' library in my python allow to me to open or perform operation on directories of a folder.
Then forwarding to the preprocessing, I construct the part of code to change the pixel size of images to 128 x 128. Such that my model (CNN basically) could use that. I also add a part where images are normalized by scaling the pixel values to the range [0, 1]. Labels are then one-hot encoded, converting categorical labels into a binary matrix representation.

Then I splited the data into test and train. CNN model is developed and excuted for the preprocessed images. 1st execution, my test accuracy was 0.38923. It was moderate.  then I noticed my preprocessing of images was not done properly. and I need data augmentation too.

*An ImageDataGenerator is employed to augment the training images with transformations like rotation, width and height shifts, shear, zoom, and horizontal flip.*

I used the pre-trained VGG16 model from Keras along with my previous model to increace my accuracy. I added custom layers to the model.The model is compiled with an Adam optimizer, categorical cross-entropy loss (suitable for multi-class classification), and accuracy as the evaluation metric.The model is trained using the augmented training data and is evaluated on the test set at the end of each epoch to monitor its performance on unseen data. 

The final accuracy wit 1000 images of fundus is 0.68

From this task of classifying the fundus, I learned about data augmentation, python libraries, VGG16 pre trained model. 
