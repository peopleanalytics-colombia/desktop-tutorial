import quiz_tests


def csv_to_close(csv_filepath, field_names):
    price_df = pd.read_csv(csv_filepath, names = field_names)
    close = price_df.pivot(index='date', columns='ticker', values='close')
    return close


quiz_tests.test_csv_to_close(csv_to_close)