def generate_positions(prices):
    """
    Generate the following signals:
     - Long 30 share of stock when the price is above 50 dollars
     - Short 10 shares when it's below 20 dollars
    
    Parameters
    ----------
    prices : DataFrame
        Prices for each ticker and date
    
    Returns
    -------
    final_positions : DataFrame
        Final positions for each ticker and date
    """
    # TODO: Implement Function
    ####Señal
    signal_30 = prices > 50
    signal_10 = prices < 20
    ###as numpy numeric
    signal_30 = signal_30.astype(np.int)
    signal_10 = signal_10.astype(np.int)
    ####shortorlong
    pos_one = 30 * signal_30
    pos_three = -10 * signal_10
    #### pos
    final_positions = pos_one + pos_three

    
    return final_positions
