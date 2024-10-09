import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import numpy as np
from tensorflow.keras.models import load_model  # type: ignore
from collections import Counter

def load_emotion_model(model_path):
    """
    Load the emotion detection model from a file.

    Parameters:
    - model_path: Path to the model file.

    Returns:
    - Loaded Keras model.
    """
    return load_model(model_path)

def predict_emotions(frames, model):
    """
    Predict emotions for a batch of frames using the given model.

    Parameters:
    - frames: List of preprocessed frames (images) as numpy arrays.
    - model: Loaded Keras model for emotion detection.

    Returns:
    - List of predicted emotion indices.
    """
    if frames:
        # Normalize frame data to the range [0, 1]
        batch = np.array(frames, dtype='float32') / 255
        # Predict emotions for each frame
        predictions = model.predict(batch)
        # Return the index of the highest probability for each frame
        return np.argmax(predictions, axis=1)
    return []

def aggregate_predictions(emotions, labels):
    """
    Aggregate emotion predictions and return them sorted by frequency.

    Parameters:
    - emotions: List of emotion indices predicted for each frame.
    - labels: List of emotion labels corresponding to indices.

    Returns:
    - List of labels sorted by their frequency of occurrence.
    """
    # Count occurrences of each emotion
    emotion_count = Counter(emotions)
    # Sort emotions by count in descending order
    sorted_emotions = [emotion for emotion, count in emotion_count.most_common(3)]
    # Map emotion indices to labels
    sorted_labels = [labels[emotion] for emotion in sorted_emotions]
    return sorted_labels
