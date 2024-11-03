

"""
https://www.datacamp.com/tutorial/a-data-scientists-guide-to-signal-processing
https://github.com/AryaKoureshi/Signal-Processing-and-Analysis-of-EEG-Data-Using-Python
https://klyshko.github.io/teaching/2019-02-22-teaching
https://www.datacamp.com/tutorial/a-data-scientists-guide-to-signal-processing
https://github.com/jinglescode/python-signal-processing    
https://www.kaggle.com/code/faressayah/signal-processing-with-python
https://neuraldatascience.io/7-eeg/erp_filtering.html
https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html
https://pywavelets.readthedocs.io/en/latest/ref/index.html

https://github.com/kalpanmukherjee/python-eda-cheatsheet
https://learnpython.com/blog/python-exploratory-data-analysis-cheat-sheet/
https://www.kaggle.com/discussions/getting-started/481538

https://colab.research.google.com/github/jinglescode/python-signal-processing/blob/main/tutorials/Signal%20composition%20-%20time%2C%20sampling%20rate%20and%20frequency.ipynb
https://g0rella.github.io/gorella_mwn/python_visualization_for_data.html
https://g0rella.github.io/gorella_mwn/intro_statistics.html
https://g0rella.github.io/gorella_mwn/preprocessing_eeg.html
"""

# Install: pip install mne


import os
import os.path as op
import mne
import numpy as np
import pandas as pd
import scipy.io
from scipy import signal

if __name__ == "__main__":
    archivo_mat = scipy.io.loadmat("S1_A1_E1.mat")
    emg_signals = archivo_mat['emg']
    postura = archivo_mat['restimulus']
    repeticion = archivo_mat['rerepetition']
    sample_freq = 100
    emg_signals_T = emg_signals.T
    print(emg_signals_T.shape)


    # Crear información de los canales
    n_channels = emg_signals_T.shape[0]
    info = mne.create_info(ch_names=[f'sEMG{i+1}' for i in range(n_channels)], sfreq=sample_freq, ch_types='emg')
    raw = mne.io.RawArray(emg_signals_T, info)
    # raw.plot(scalings='auto', title='sEMG Data', show=True)
    raw.plot(scalings='auto', title='sEMG Data', show=True, block=True)


    

    
