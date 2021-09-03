import pandas as pd

def lambda_handler(event, context):
    d = {'test1': [1,2], 'test2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.1')
