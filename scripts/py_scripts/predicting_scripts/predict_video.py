#!/usr/bin/env python
import json
import argparse
import obj_predictor.predicting.predict as predict
import os
'''
Created by Jacob Rivera
Fall 2023

Last edit: 01/03/2024

Description:
    Will predict objects on a video given the info inside a json config file

'''





def main():
    parser = argparse.ArgumentParser(description="Predict objs in video.")
    parser.add_argument("--model_path", required=True, help="Path to YOLO model .pt file.")
    parser.add_argument("--video_input", required=True, help="Input video name and path.")
    parser.add_argument("--confidence", type=float, required=False, default=0.5, help="Confidence threshold for predictions.")
    parser.add_argument("--output_dir", type=str, required=False, default=None, help="Output directory for predicted files.")

    parser.add_argument("--save_annot", type=bool, required=False, default=False, help="flag to save text annotations.")
    parser.add_argument("--save_frames", type=bool, required=False, default=False, help="flag to save individual frames.")
    parser.add_argument("--save_yolo_vid", type=bool, required=False, default=True, help="flag to save predicted video.")
    parser.add_argument("--save_drawn_frames", type=bool, required=False, default=False, help="flag to save yolo drawn/annotated frames.")
    parser.add_argument("--normalize_annot", type=bool, required=False, default=False, help="flag to save annotations normalized or not.")

    args = parser.parse_args()

    model_path = args.model_path
    video_input = args.video_input
    confidence = args.confidence
    output_dir = args.output_dir
    if output_dir is None:
        output_dir = os.path.dirname(video_input)
    # add flag for normalized annot
    save_annot = args.save_annot
    save_frames = args.save_frames
    save_yolo_vid = args.save_yolo_vid
    save_drawn_frames = args.save_drawn_frames
    normalize_annot = args.normalize_annot

    predict.predict_video(model_path, video_input, output_dir, confidence, save_annot, save_frames, save_yolo_vid, save_drawn_frames, normalize_annot)

    return

if __name__ == "__main__":
    main()