import yfinance as yf
import pandas as pd
import sklearn as sk

# Returns a list of 10 ticker symbols (strings)
def get_leaderboard():
    # NOTE: store in disk
    df = get_data()
    clean_data(df)
    model = create_model(df)
    top_10 = use_model(df, model)
    return []

# Retreives data from web
# Outputs a pandas dataframe
def get_data():
    # TODO
    raise NotImplementedError("Get data")

# Removes outliers and missing data
def clean_data(df):
    # TODO
    raise NotImplementedError("Clean data")

def create_model(df):
    wrangle_data(df)
    train, test = split_data(df)
    model = train_and_validate_model(train)
    test_model(test, model)
    return model

# Tidies data and converts columns into useful formats for model
def wrangle_data(df):
    # TODO
    raise NotImplementedError("Wrangle Data")

# Splits data into training and testing
# Returns train and test datasets
def split_data(df):
    # TODO
    raise NotImplementedError("Split Data")

# Splits data into training and testing
def train_and_validate_model(train):
    # TODO
    raise NotImplementedError("Train and validate")

# Tests the model and returns accuracy
def test_model(test, model):
    # TODO
    raise NotImplementedError("Test model")


def use_model(df, model):
    # TODO
    raise NotImplementedError("Use Model")



print(get_leaderboard())