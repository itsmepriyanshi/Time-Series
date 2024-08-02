from sklearn.metrics import mean_absolute_error, precision_score

def evaluate_arima_model(model, test_data):
    forecast = model.get_forecast(len(test_data))
    ypred = forecast.predicted_mean
    conf_int = forecast.conf_int(alpha=0.05)
    mae = mean_absolute_error(test_data, ypred)
    return ypred, conf_int, mae

def evaluate_classification_model(model, test_data, features):
    preds = model.predict(test_data[features])
    precision = precision_score(test_data['Target'], preds)
    return preds, precision