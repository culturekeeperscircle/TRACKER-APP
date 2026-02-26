"""Structured logging for the pipeline."""
import logging
import os
from datetime import datetime
from pathlib import Path


def setup_logger(name='tckc_pipeline'):
    log_dir = Path(os.path.dirname(__file__)) / '..' / 'logs'
    log_dir.mkdir(exist_ok=True)

    log_file = log_dir / f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # File handler
    fh = logging.FileHandler(log_file)
    fh.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s'))
    logger.addHandler(fh)

    # Console handler (for GitHub Actions output)
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
    logger.addHandler(ch)

    return logger
