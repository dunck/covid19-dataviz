# Duncan, 10/04/2020

import requests as req
import pandas as pd
import matplotlib.pyplot as plt

def get_df():
    return pd.read_json('https://api.covid19api.com/country/australia/status/confirmed')

def main():
    df = get_df()
    
    qld_cases = df[df["City"]=="Queensland"]

    plt.scatter(qld_cases["Date"],qld_cases["Cases"])
    plt.show()

if __name__ == "__main__":
    main()