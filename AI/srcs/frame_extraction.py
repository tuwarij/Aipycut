import cv2
from concurrent.futures import ThreadPoolExecutor

def extract_frames_in_range(video_path, start_frame, end_frame, frame_step):
    """
    Extract frames from a video file within a specified range.

    Parameters:
    - video_path: Path to the video file.
    - start_frame: The starting frame index.
    - end_frame: The ending frame index.
    - frame_step: Interval between frames to extract.

    Returns:
    - List of frames extracted from the video.
    """
    video = cv2.VideoCapture(video_path)
    frames = []
    frame_index = 0
    success, frame = video.read()

    while success and frame_index <= end_frame:
        if frame_index >= start_frame and frame_index % frame_step == 0:
            frames.append(frame)
        frame_index += 1
        success, frame = video.read()

    video.release()
    return frames

def parallel_frame_extraction(video_path, num_workers=2, frame_step=10):
    """
    Extract frames from a video file in parallel using multiple threads.

    Parameters:
    - video_path: Path to the video file.
    - num_workers: Number of threads to use for parallel extraction.
    - frame_step: Interval between frames to extract.

    Returns:
    - List of frames extracted from the video.
    """
    # Get the total number of frames in the video
    video = cv2.VideoCapture(video_path)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video.release()

    # Calculate chunk size for each worker
    chunk_size = total_frames // num_workers
    tasks = []

    # Create thread pool and submit tasks
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        for i in range(num_workers):
            start_frame = i * chunk_size
            end_frame = (i + 1) * chunk_size if i != num_workers - 1 else total_frames
            tasks.append(executor.submit(extract_frames_in_range, video_path, start_frame, end_frame, frame_step))

        # Collect results from each thread
        all_frames = []
        for task in tasks:
            all_frames.extend(task.result())

    return all_frames
