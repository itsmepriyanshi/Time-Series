# Time Series Forecasting with ARIMA Model

This project demonstrates time series forecasting using ARIMA models for stock price prediction.

## Folder Structure

- `data/`: Contains the dataset `AAPL.csv`.
- `src/`: Source code modules.
  - `data_preparation.py`: Functions for loading and preparing data.
  - `model_training.py`: Functions for training ARIMA and ARIMAX models.
  - `model_evaluation.py`: Functions for evaluating model performance.
  - `visualization.py`: Functions for visualizing data and model results.
  - `utils.py`: Utility functions for logging and error handling.
- `tests/`: Unit tests for the modules.
- `logs/`: Log files.
- `requirements.txt`: List of project dependencies.
- `main.py`: Entry point of the application.

## How to Run

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the main script: `python main.py`.

## Dependencies

- pandas
- numpy
- matplotlib
- seaborn
- statsmodels
- pmdarima
- scikit-learn
