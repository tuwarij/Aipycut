import cv2
import matplotlib.pyplot as plt
from AI.srcs.frame_extraction import parallel_frame_extraction
from AI.srcs.preprocessing import preprocess_frames_in_parallel
from AI.srcs.emotion_prediction import load_emotion_model, predict_emotions, aggregate_predictions

def emotion_detection(video_path, model_path="AI/model/my_model_74percent_ordered.h5"):
    # Configuration
    video_path = video_path
    model_path = model_path
    Label = ['Surprised', 'Fear', 'Disgusted', 'Happy', 'Sad', 'Anger', 'Neutral']
    frame_step = 10

    # Extract frames from the video
    # print("Start extracting video")
    frames = parallel_frame_extraction(video_path, frame_step=frame_step)
    # print(f"Extracted {len(frames)} frames")

    # Preprocess frames in parallel
    # print("Start preprocessing frames")
    preprocessed_frames = preprocess_frames_in_parallel(frames)
    # print(f"Preprocessed {len(preprocessed_frames)} frames")

    # Load the pre-trained emotion model
    # print("Load emotion model")
    model = load_emotion_model(model_path)

    # Predict emotions
    # print("Predicting emotions")
    emotions = predict_emotions(preprocessed_frames, model)
    # print(f"Emotions: {emotions}")

    # Aggregate and order emotions by frequency
    # print("Aggregating and ordering emotions")
    ordered_labels = aggregate_predictions(emotions, Label)
    # print(f"Ordered labels by frequency: {ordered_labels}")

    # Visualize the preprocessed frames
    # if len(preprocessed_frames) > 0:
    #     print("Displaying preprocessed faces")
    #     for i, frame in enumerate(preprocessed_frames):
    #         rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         plt.figure(figsize=(5, 5))
    #         plt.imshow(rgb_image)
    #         plt.title(f"Preprocessed Face {i+1}")
    #         plt.axis('off')
    #         plt.show()

    return ordered_labels