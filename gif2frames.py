from PIL import Image, ImageSequence
import os

def extract_frames(gif_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    with Image.open(gif_path) as gif:
        for i, frame in enumerate(ImageSequence.Iterator(gif)):
            frame = frame.convert("RGB")
            frame_path = os.path.join(output_folder, f"frame_{i:03d}.png")
            frame.save(frame_path)
            print(f"Saved {frame_path}")

if __name__ == "__main__":
    gif_path = "./evernight-honkai.gif"
    output_folder = "./evernight-honkai_frames/"
    extract_frames(gif_path, output_folder)
