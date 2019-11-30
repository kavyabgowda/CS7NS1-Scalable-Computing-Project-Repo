Image captcha GitHub repo - https://www.github.com/amrishAK/imageCaptcha.git
Audio captcha GitHub repo - https://www.github.com/amrishAK/audioCaptcha.git


Image Captcha current accuracy - 71%

Steps taken in preprocessing to improve the model accuracy:
	1. Auto contrasting (cutoff = 10)
	2. Enhancing the sharpness of the image 
	3. Converting the image to greyscale
	4. Binary threasholding
	5. Otsu threasholding

Image Captcha Model Training Pattern:

Number of Images	Epoch	Accuracy
    20000		  2	  12%
    20000		  2	  40%
    40000		  2	  51%
    40000		  4	  66%
    40000		  6	  71.175%
    40000		  4	  74% 
Model should be tweaked or brute forced to increase accuracy beyond this point.



Audio Captcha current accuracy - 

Steps taken in preprocessing to improve the model accuracy:

	1. Pre-processing as audio:	
		a) Low pass filter (cutoff frequency = 0.1 Hz)
		b) Discreet fourier transform (DFT) using librosa.stft 
		c) Converting amplitude into decibels using librosa.amplitude_to_db
		d) Plottig audio as a spectogram in greyscale (dimensions - 128 x 64)
	
	4. Pre-processing as image:
		a) Auto-contrasting (cutoff = 10)
		

Audio Captcha Model Training Method:

Number of Audio files	Epoch	Accuracy
      20000		  2	  12%
      20000		  2	  40%
      40000		  2	  50.10%
      40000		  4	  66%
      40000		  6	  71.187%


Contributors:
1. Amrish Kulasekaran (19327600)
2. Jagadish Rammurthy (19300933)
3. Yeshwanth Rajareddy (19301303)
4. Abishek Vaithylingam (18339763)
5. Shubhanghi Kukreti (19308174)
6. Deepthi Rajappan (19307848)
7. Manasi Palkar (19314065)
7. Kavya Bhadre Gowda (19316050)
8. Pooja Ganesh Teje (19300746)
9. Tanvi Bagla (19300699)


