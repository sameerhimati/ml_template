ml_template/
├── .github/                      # GitHub Actions workflows, PR templates
│   └── workflows/                # CI/CD pipeline definitions
├── configs/                      # Configuration files
│   ├── model/                    # Model hyperparameters
│   └── training/                 # Training configuration
├── data/                         # Data directory (usually gitignored)
│   ├── raw/                      # Raw data
│   ├── processed/                # Processed data
│   └── external/                 # External data sources
├── experiments/                  # Experiment tracking and results
│   ├── logs/                     # Training logs
│   └── models/                   # Saved model checkpoints
├── notebooks/                    # Jupyter notebooks for exploration
├── src/                         # Source code
│   ├── __init__.py
│   ├── data/                    # Data processing code
│   │   ├── __init__.py
│   │   └── preprocessing.py
│   ├── models/                  # Model architectures
│   │   ├── __init__.py
│   │   └── model.py
│   ├── training/               # Training scripts
│   │   ├── __init__.py
│   │   └── trainer.py
│   └── utils/                  # Utility functions
│       ├── __init__.py
│       └── metrics.py
├── tests/                      # Test files
│   ├── __init__.py
│   ├── test_data.py
│   └── test_models.py
├── .gitignore                  # Git ignore file
├── README.md                   # Project documentation
├── environment.yml             # Conda environment definition
├── setup.py                    # Package installation
└── requirements.txt            # Dependencies for deployment