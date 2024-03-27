# from obj_predictor import predictor
from obj_predictor.predictor import PredictorModel  # Importing the PredictorModel class from your predictor module
from obj_predictor.data import DataMaster
from pathlib import Path
import obj_predictor as op


model_path = Path("All_Data_Trainings\\all_data_2_14_mirrored_v8m\\weights\\best.pt")
input_video = Path("G:\\jacob\\practice_data_yolo\\short.mp4")

def main():
    predictor = PredictorModel(model_path)

    # predictor.predict_video(input_video, save_annot=True)

    dataHandler = DataMaster(model_path)

    labels_path = input_video.parent / "pred_labels"
    # dataHandler.smooth_annotations(input_dir=labels_path)
    op.data_processing.util.extract_all_frames("input_video")
    dataHandler.draw_annot_on_video( input_video, "smoothed.mp4", labels_path)

    

if __name__ == "__main__":
    main()