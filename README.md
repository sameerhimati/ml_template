# ML Project Template

A minimal, extensible template for machine learning projects.

## Usage Options

### Option 1: Use as a GitHub Template

1. Click the "Use this template" button at the top of this repository
2. Name your new project and create repository
3. Clone your new repository
4. Set up your environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### Option 2: Install as a package
1. Install from GitHub:
   ```bash
   pip install git+https://github.com/sameerhimati/ml-template.git
   ```
2. Create a new project:
   ```bash
   create-ml-project my-new-project
   ```


## Project Structure

```
ml_template/
├── .github/                      # GitHub Actions workflows, PR templates
│   └── workflows/               # CI/CD pipeline definitions
├── configs/                     # Configuration files
│   ├── model/                  # Model hyperparameters
│   └── training/               # Training configuration
├── data/                       # Data directory (usually gitignored)
│   ├── raw/                    # Raw data
│   ├── processed/              # Processed data
│   └── external/               # External data sources
├── experiments/                # Experiment tracking and results
│   ├── logs/                   # Training logs
│   └── models/                 # Saved model checkpoints
├── notebooks/                  # Jupyter notebooks for exploration
├── src/                       # Source code
│   ├── __init__.py
│   ├── data/                  # Data processing code
│   │   ├── __init__.py
│   │   └── preprocessing.py
│   ├── models/                # Model architectures
│   │   ├── __init__.py
│   │   └── model.py
│   ├── training/             # Training scripts
│   │   ├── __init__.py
│   │   └── trainer.py
│   └── utils/                # Utility functions
│       ├── __init__.py
│       └── metrics.py
├── tests/                    # Test files
│   ├── __init__.py
│   ├── test_data.py
│   └── test_models.py
├── .gitignore               # Git ignore file
├── README.md               # Project documentation
├── environment.yml         # Conda environment definition
├── setup.py               # Package installation
└── requirements.txt       # Dependencies for deployment
```

## Usage

1. Data Processing:
   - Place raw data in `data/raw/`
   - Process data using scripts in `src/data/`

2. Model Development:
   - Implement models in `src/models/`
   - Training code goes in `src/training/`

3. Development:
   - Format code: `black src/ tests/`
   - Run tests: `python -m pytest tests/`

## Project Organization

- Use notebooks in `notebooks/` for exploration only
- Keep source code in `src/`
- Write tests in `tests/`
- Track experiments and results in `experiments/`
- Store configurations in `configs/`

## Dependencies

This project uses conda for dependency management. See `environment.yml` for the full list of dependencies.

## Contributing

1. Format code with black before committing
2. Ensure tests pass
3. Update documentation as needed