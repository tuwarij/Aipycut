import cv2
from concurrent.futures import ThreadPoolExecutor

def preprocess_frame(frame):
    """
    Detect faces in the frame, resize the detected face if it's large enough.
    
    Parameters:
    - frame: The image frame in which to detect faces.
    
    Returns:
    - The resized face if a valid face is detected, otherwise None.
    """
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=4, minSize=(100, 100))

    if len(faces) == 0:
        return None

    x, y, w, h = faces[0]
    face_bgr = frame[y:y+h, x:x+w]
    
    if w >= (frame.shape[1] / 3.5) and h >= (frame.shape[0] / 3.5):
        resized_face_bgr = cv2.resize(face_bgr, (100, 100), interpolation=cv2.INTER_AREA)
        return resized_face_bgr
    
    return None

def preprocess_frames_in_parallel(frames, num_threads=None):
    """
    Process frames in parallel to detect and resize faces.
    
    Parameters:
    - frames: List of image frames to be processed.
    - num_threads: Number of threads to use for parallel processing.
    
    Returns:
    - List of preprocessed frames with faces resized.
    """
    if num_threads is None:
        num_threads = min(32, len(frames))  # Default to 32 threads or the number of frames

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        preprocessed_frames = list(executor.map(preprocess_frame, frames))

    return [frame for frame in preprocessed_frames if frame is not None]
