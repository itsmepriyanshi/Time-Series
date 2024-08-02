from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima

def train_arima_model(data, order):
    model = ARIMA(data, order=order)
    return model.fit()

def train_arimax_model(data, exog, order):
    model = ARIMA(data, exog=exog, order=order)
    return model.fit()

def auto_arima_search(data, exog=None):
    return auto_arima(data, exogenous=exog, seasonal=False, trace=True)