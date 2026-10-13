import pickle
from pathlib import Path

# Path to repository root (report/ -> root)
ROOT: Path = Path(__file__).parent.parent

# Path to the pickled ML model
MODEL_PATH: Path = ROOT / "assets" / "model.pkl"


def load_model():
    """Load and return the pickled recruitment-risk ML model."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found at {MODEL_PATH}. "
            "Ensure assets/model.pkl is present."
        )
    with open(MODEL_PATH, "rb") as fh:
        return pickle.load(fh)
