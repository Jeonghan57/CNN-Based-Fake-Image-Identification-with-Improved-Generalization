# CNN-Based-Fake-Image-Identification-with-Improved-Generalization

![image](https://user-images.githubusercontent.com/77098071/147531256-bd056309-484f-4e43-9e2c-01a75252adb7.png)

__IVC(Image & Vision Computing) Lab / Pukyong Nat'l Univ Electronic Engineering / Busan, Republic of Korea__   
Jeonghan Lee, Hanhoon Park(Major Professor)

* Paper(Korean) : J. Lee and, H. Park, "CNN-Based Fake Image Identification with Improved Generalization," Journal of Korea Multimedia Society, 2021, 24.12: 1624-1631.

Abstract : With the continued devleopment of image processing technology, we live in a time when it is difficult to visually discriminate processed (or tampered) images from real images. However, as the risk of fake images being misused for crime increases, the importance of image forensic science for identifying fake images is emerging. Currently, various deep learning-based identifiers have been studied, but there are still many problems to be used in real situations. Due to the inherent characteristics of deep learning that strongly relies on given training data, it is very vulnerable to evaluating data that has never been viewed. Therefore, we try to find a way to improve generalization ability of deep learning-based fake image identifiers. First, images with various contents were added to the training dataset to resolve the over-fitting problem that the identifier can only classify real and fake images with specific contents but fails for those with other contents. Next, color spaces other than RGB were exploited. That is, fake image identification was attempted on color spaces not considered when creating fake images, such as HSV and YCbCr. Finally, dropout, which is commonly used for generalization of neural networks, was used. Through experimental results, it has been confirmed that the combination of the approaches significantly can greatly improve the accuracy and generalization ability of deep learning-based identifiers in identifying fake images that have never been seen before.

## Settings
### Dataset
* Category : LSUN - cat, church_outdoor, train, airplane, bus, cow, bridge, bedroom, classroom, restaurant, sheep
* Real/Fake ?????? Train set 25K???/ Test set 2K??? ?????????????????? ?????? </br> -> Mix Train set??? 25K??? ?????? ????????? Train set ??????. Test set??? Single Category?????? ??????.
* Sheep ??????????????? ?????? Mixing Process??? ???????????? ?????? ?????? Unseen Test set?????? ??????.
* Image size : 256X256
* GAN : ProGAN

### Feature Extraction
* CNN Model : Pelee with HPF
* Color Space : RGB, HSV, YCbCr
* Dropout : N/A , 0.2, 0.5

### Spec
* epoch = 50, batch_size = 64, learning_rate = 0.001, optimizer = Adam

## Result
### Experiment 1 : Accuracy of identifying fake images according to the number of image categories
![image](https://user-images.githubusercontent.com/77098071/147534578-1210d2cd-7452-4d62-bf6c-e722756b995a.png)
[Tab 1] Fake image identification rates of Pelee+HPF depending on the number of image categories used in the training step
 <br/> <br/>
![image](https://user-images.githubusercontent.com/77098071/147535084-d9c0e675-0685-4df5-b645-b82d7725c093.png) <br/>
[Fig 1] Change in fake image identification rates for the images that are not included in the image categories used in the training step as the number of image categories used in the training step increases
<br/> <br/> <br/>
### Experiment 2 : Accuracy of identifying fake images according to color space
![image](https://user-images.githubusercontent.com/77098071/147535369-29c53d78-4ae4-451c-9f9b-7887777c1038.png)
[Tab 2] Fake image identification rates of Pelee+HPF when the image color space was changed to HSV
<br/><br/>
![image](https://user-images.githubusercontent.com/77098071/147535459-45cafd1d-ad50-4648-887c-1ce6689a745a.png)
[Tab 3] Fake image identification rates of Pelee+HPF when the image color space was changed to YCbCr
<br/><br/>
![image](https://user-images.githubusercontent.com/77098071/147535534-00f0bdbe-cbf8-4228-904e-8d12bb7a5d4b.png) <br/>
[Fig 2] Change in fake image identification rates for the images that are not included in the image categories used in the training step when using different color spaces
<br/><br/><br/>
### Experiment 3 : Accuracy of identifying fake images according to dropout ratio
![image](https://user-images.githubusercontent.com/77098071/147536279-7f3918f3-f3e4-4b74-ac81-6293fd51087d.png)
[Tab 4] Fake image identification rates of Pelee+HPF with a dropout ratio of 0.2
<br/><br/>
![image](https://user-images.githubusercontent.com/77098071/147536412-8835dbda-20be-4d15-8ee8-f63578a6f18b.png)
[Tab 5] Fake image identification rates of Pelee+HPF with a dropout ratio of 0.5
<br/><br/>
![image](https://user-images.githubusercontent.com/77098071/147536490-f20067b4-c2b9-4e1c-a754-d4ba866b58ed.png) <br/>
[Fig 3] Change in fake image identification rates for the images that are not included in the image categories used in the training step when using different dropout ratios
<br/><br/><br/>
### Experiment 4 : The optimal combination for improving generalization ability and comparison of performance with Xception
![image](https://user-images.githubusercontent.com/77098071/147536817-b8c6dfb3-0cc4-4ad6-92a7-add52d2dd7f0.png)
[Tab 6] Fake image identification rates of Pelee+HPF with the RGB to HSV color conversion and a dropout of 0.2
<br/><br/>
![image](https://user-images.githubusercontent.com/77098071/147537549-075d9229-8407-4ceb-8816-7d58683d438a.png)
[Tab 7] Fake image identification rates of Xception
<br/><br/>
![image](https://user-images.githubusercontent.com/77098071/147537740-83c617a3-21ca-4322-9e86-74a0475a0646.png) <br/>
[Fig 4] Change in fake image identification rates of combinations of generalization methods, and comparison with Xception
<br/><br/><br/>

## Conclusion
* ??????(Train)??? ????????? ????????? ???????????? ???(?????? ?????????)??? ??????????????? ????????? ???????????? ?????? ????????????(???????????? ?????????)??? ?????? ?????? ???????????? ??????
* HSV??? YCbCr??? ??? ?????? ??????(Convert)?????? ????????????(Dropout)??? ?????????????????? ????????? ??????(Generalization Performance)??? ?????? 
<br/> -> but, ?????? ????????? ?????? ???????????? ????????? HSV??? ??? ?????? ????????? ???????????? ????????? ???????????? ????????? ???????????? ???(?????? ?????????)??? ????????? ?????? ?????? ?????????
* ??? ??????????????? ?????? ????????? ????????? Pelee??? ???????????????, __Xception??? ????????? ?????? ????????? ????????? ????????? ????????? ??????????????? ?????? ????????? ?????? ???????????? ??????__
<br/><br/><br/>

__This content is inspired by the documents below :__
1. T. Karras, S. Laine, M. Aittala, J. Hellsten, J. Lehtinen, and T. Aila, "Analyzing and Improving the Image Quality of StyleGAN," *Proceeding of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pp. 8110=8119, 2020.
2. C. Ledig, L. Theis, F. Huszar, J. Caballero, A. Cunningham, A. Acosta, and W. Shi, "Photo-Realistic Single Image SUper-Resolution Using a Generative Adversarial Network," *Proceeding of the IEEE Conference on Computer Vision and Pattern Recognition*, pp. 4681-4690, 2017.
3. J.Y. Zhu, T. Park, P. Isola, and A.A. Efros, "Unparied Image_to_Image Translation Using Cycle-Consistent Adversarial Networks," *Proceeding of the IEEE International Conference on Computer Vision*, pp. 2223-2232, 2017.
4. H. Mo, B. Chen, And W. Luo, "Fake Faces Identification via Convolutional Neural Network," *Proceeding of the 6th ACM Workshep on Indformation Hiding and Multimedia Security*, pp. 43- 47, 2018.
5. N.T. Do, I.S. Na, and S.H. Kim, "Forensics Face Detection from GANs Using Convolutional Neural Network," *Proceeding of International Symposium on Information Technology Convergence*, 2018.
6. I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, and Y. Bengio, "Generative Adversarial Nets," *Advances in Neural Information Processing Systems*, 27, 2014.
7. T. Karras, T. Aila, S. Laine, and J. Lehtinen, "Progressive Growing of GANs for Improved Quality, Stability, and Variation," arXiv preprint arXiv:1710.10196, 2017.
8. F. Marra, D. Gragnaniello, L. Verdoliva, and G. Poggi, "Do GANs Leave Artificial Fingerprints?," *Proceeding of IEEE Conference on Multimedia Information Processing and Retrieval*, pp. 506-511, 2019.
9. N. Yu, L.S. Davis, and M. Fritz, ???Attributing Fake Images to GANs: Learning and Analyzing GAN fingerprints,??? *Proceeding of the IEEE/CVF International Conference on Computer Vision*, pp. 7556-7566, 2019.
10. L. Verdoliva, ???Media Forensics and Deepfakes: an Overview,??? *IEEE Journal of Selected Topics in Signal Processing*, Vol. 14, No. 5, 910-932, 2020.
11. D. Cozzolino, J. Thies, A. Rossler, C. Riess, M. Nie??ner, and L. Verdoliva, ???Forensictransfer: Weakly-Supervised Domain Adaptation for Forgery Detection,??? arXiv preprint arXiv:1812.02510, 2018.
12. M. Du, S. Pentyala, Y. Li, and X. Hu, ???Towards Generalizable Forgery Detection with Locality-Aware Autoencoder,??? arXiv preprint arXiv:1909.05999, 2019.
13. H. Li, B. Li, S. Tan, and J. Huang, ???Detection of Deep Network Generated Images Using Disparities in Color Components,??? arXiv preprint arXiv:1808.07276, 2018.
14. F. Chollet, ???Xception: Deep Learning with Depthwise Separable Convolutions,??? *Proceeding of the IEEE Conference on Computer Vision and Pattern Recognition*, pp. 1251-1258, 2017.
15. F. Yu, A. Seff, Y. Zhang, S. Song, T. Funkhouser, and J. Xiao, ???LSUN: Construction of a Large-scale Image Dataset using Deep Learning with Humans in the Loop,??? arXiv preprint arXiv:1506.03365, 2015.
16. R.J. Wang, X. Li, and C.X. Ling, ???Pelee: A Real-Time Object Detection System on Mobile Devices,??? arXiv preprint arXiv:1804.06882, 2018.
17. S. Kang and H. Park, ???Hierarchical CNN-Based Senary Classification of Steganographic Algorithms,??? Journal of Korea Multimedia Society, Vol. 24, No. 4, pp. 550-557, 2021.
