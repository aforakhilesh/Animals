import pickle
import pandas as pd

# Makes a .pkl file which can be for loading data into the template
def main():
    File = 'reptiles.csv'
    DF = pd.read_csv(File)
    DF = DF.fillna('NaN')
    pickle.dump(DF, open('./123.pkl', 'wb'))

if __name__ == '__main__':
    main()