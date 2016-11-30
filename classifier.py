import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier, FilteredClassifier, Evaluation
from weka.core.classes import Random

jvm.start()
data_dir = "data/"
filename = "data_r_LDA.arff"

loader = Loader(classname="weka.core.converters.ArffLoader")
data = loader.load_file(data_dir + filename)
data.class_is_last()

clsf = Classifier(classname="weka.classifiers.lazy.IBk")

fc = FilteredClassifier()
fc.classifier = clsf

evl = Evaluation(data)
evl.crossvalidate_model(fc, data, 10, Random(1))

print(evl.percent_correct)
print(evl.summary())
print(evl.class_details())

jvm.stop()
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
