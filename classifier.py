##########################################################################################
## Scene Classification                                                                 ##
## Authors : Chris Andrew, Santhoshini Reddy, Nikath Yasmeen, Sai Hima, Sriya Ragini    ##
###################################################################                     ##
## Description: This project was developed as part of the DIP course at IIIT Sri City   ##
## All code is available for free usage for educational purposes                        ##
## Authors do not authorize commercial use of the source code                           ##
##########################################################################################

# The module performs classification using the Nearest Neghbour classifier on data given
# using 10 fold cross-validation.

################ Imports ################
import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier, FilteredClassifier, Evaluation
from weka.core.classes import Random
################ Global ################
jvm.start()
data_dir = "data/"
filename = "data_r_LDA.arff"
loader = Loader(classname="weka.core.converters.ArffLoader")
clsf = Classifier(classname="weka.classifiers.lazy.IBk")
fc = FilteredClassifier()

################ Source ################
# ------------------------------------

# ------------------------------------
data = loader.load_file(data_dir + filename)
data.class_is_last()
# ------------------------------------
fc.classifier = clsf
# ------------------------------------
evl = Evaluation(data)
evl.crossvalidate_model(fc, data, 10, Random(1))
# ------------------------------------
print(evl.percent_correct)
print(evl.summary())
print(evl.class_details())
# ------------------------------------
jvm.stop()
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
