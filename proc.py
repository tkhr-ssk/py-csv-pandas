import argparse
import pandas as pd
import numpy as np


def proc_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()


def main():
    print('input={}'.format(args.input))

    df = pd.read_csv(args.input, na_values='-')
    df = df.fillna(0).astype(np.int64, errors='ignore')

    print(df.columns)
    print(df)
    print(df.groupby(['西暦（年）']).sum().astype(np.int64))


if __name__ == '__main__':
    proc_args()
    main()
