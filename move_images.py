# Images in the NIH dataset is split in different folders such as images_001/images/... contains the first x number of images
# images_002/images/... contains the next x number of images and so on.
# all images that would be used by the model would be put into a single folder named as 'combined'
# particularly the images that would only be gathered have the following information:
# the radiograph is a Post-Anterior radiograph, 
# the radiograph has one finding only and not multiple findings.
import pandas as pd
import numpy as np
import os

csv_path = 'NIH/Data_Entry_2017_v2020.csv'

def clean_data():
    xray_data = pd.read_csv(csv_path)
    # Remove Findings with multiple labels
    xray_data = xray_data[xray_data['Finding Labels'].apply(lambda x: '|' not in x)]
    xray_data = xray_data.loc[xray_data['View Position'] == 'PA']
    return xray_data

if __name__ == '__main__':
    xray_data = clean_data()
    