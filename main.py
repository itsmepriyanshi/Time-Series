import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from data_preparation import load_data, prepare_univariate_data, prepare_bivariate_data
from model_training import train_arima_model, train_arimax_model, auto_arima_search
from model_evaluation import evaluate_arima_model, evaluate_classification_model
from visualizations import plot_time_series, decompose_and_plot
from utils import setup_logging, log_error, log_info

def main():
    setup_logging()
    log_info("Starting main execution")
    
    try:
        data = load_data('data/AAPL.csv')
        log_info("Data loaded successfully")
        
        univariate_data = prepare_univariate_data(data)
        bivariate_data = prepare_bivariate_data(data)
        log_info("Data preparation completed")
        
        # Example usage of functions
        plot_time_series(univariate_data['AAPL'], 'Apple Stock Price')
        decompose_and_plot(univariate_data['AAPL'])
        log_info("Visualization completed")
        
        arima_model = train_arima_model(univariate_data['AAPL'], order=(1, 1, 1))
        log_info("ARIMA model training completed")
        
        # Assuming 'TXN' is another column in the data
        arimax_model = train_arimax_model(bivariate_data['AAPL'], bivariate_data['TXN'], order=(1, 1, 1))
        log_info("ARIMAX model training completed")
        
        # Evaluation and logging
        _, _, mae = evaluate_arima_model(arima_model, univariate_data['AAPL'])
        log_info(f'ARIMA Model MAE: {mae}')
        
    except Exception as e:
        log_error(f'An error occurred: {str(e)}')
        raise

if __name__ == "__main__":
    main()