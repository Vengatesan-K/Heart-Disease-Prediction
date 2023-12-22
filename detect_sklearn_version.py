import pickle
import sklearn
import warnings
from sklearn.exceptions import InconsistentVersionWarning

# Catch the InconsistentVersionWarning and print the original scikit-learn version
warnings.simplefilter("error", InconsistentVersionWarning)

try:
    model = pickle.load(open('randomforest_model.pkl', 'rb'))
except InconsistentVersionWarning as w:
    print(w.original_sklearn_version)
