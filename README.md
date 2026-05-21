# Speak-See — Lip Reading from Video

## What Is This?

A **lip-reading** project — given a silent video of someone speaking, the goal is to predict the words being said. Uses deep learning (TensorFlow).

## Project Status: **Incomplete / Scaffold Only**

The data loading and preprocessing pipeline is built, but the **model architecture, training loop, evaluation, and inference are not implemented yet.**

---

## Project Structure

```
speaksee/
├── Speak-See.ipynb              # Main notebook (data pipeline only)
├── create_sample_data.py         # Generates synthetic test data
├── requirements.txt              # Python dependencies
├── README.md                     # This file
├── IMAGES/
│   ├── InputPreprocessing.png    # Diagram: preprocessing pipeline
│   └── ModelDiag.png             # Diagram: planned model architecture
├── data/
│   ├── s1/bbal6n.mpg             # Sample video (synthetic random noise)
│   ├── s1/bbal6n.pkl             # Pre-cached frames (pickle)
│   └── alignments/s1/bbal6n.align  # Word timestamps
└── venv/                         # Python virtual environment
```

---

## What the Notebook Does (Cells 1–24)

### 1. Imports & Setup
TensorFlow, OpenCV, NumPy, matplotlib. Configures CPU memory growth.

### 2. Video Loading — `load_video()`
Reads a video and extracts mouth frames:
- First tries a pre-cached `.pkl` pickle file (fast path)
- Falls back to OpenCV: reads each frame, converts to **grayscale**, **crops to the mouth region** (rows 190–236 × cols 80–220 → **46×140 pixels**), then **normalizes** (z-score)
- Final fallback: generates **75 random noise frames** (46×140)

### 3. Vocabulary
40 character tokens:
```
['', 'a', 'b', ..., 'z', "'", '?', '!', '1', '2', ..., '9', ' ']
```
Two Keras `StringLookup` layers:
- `char_to_num`: text → integer indices
- `num_to_char`: indices → text

### 4. Alignment Loading — `load_alignments()`
Reads `.align` files with format `start_time end_time word`. Skips `sil` (silence) tokens, inserts spaces between words, encodes to integer indices.

Known bug: `TypeError: object of type 'numpy.int64' has no len()` — alignments currently return empty.

### 5. Data Loader — `load_data()`
Combines video + alignment loading. Returns `(frames_array, alignments_array)`.

### 6. TF Data Pipeline
Builds:
```
list_files('*.mpg') → shuffle → map(load_data) → padded_batch(batch=2) → prefetch
```
Splits into train/test (400/remaining). Only 1 video file exists, so test set is empty.

### 7. Visualization
Displays grayscale mouth crops (46×140) from the pipeline.

### 8. Decode
Converts alignment integer indices back to readable text.

---

## The Two Images

- **InputPreprocessing.png**: Shows the preprocessing pipeline — raw video frame → grayscale → crop mouth region (190:236, 80:220) → normalize → ready for model.
- **ModelDiag.png**: Likely shows the **planned model architecture** (CNN + RNN + CTC), which is the standard approach for lip-reading but was **never implemented**.

---

## Target Dataset: GRID Corpus

The `data/s1/` (speaker 1) directory, `.align` file format, and constrained vocabulary match the **GRID corpus** — a standard audiovisual dataset for lip-reading with 34 speakers × 1000 sentences each from a limited grammar.

---

## Current Tech Stack

| Library | Version | Role |
|---|---|---|
| TensorFlow | 2.16.2 | Deep learning framework |
| OpenCV | 4.8.1 | Video I/O, frame processing |
| NumPy | 1.26.4 | Array ops, normalization |
| Matplotlib | 3.8.4 | Visualization |
| imageio | 2.34.1 | Additional video support |
| Jupyter | 1.0.0 | Notebook environment |

---

## What's Missing (Needs Implementation)

| Component | Status |
|---|---|
| Video loading & preprocessing | ✅ Done |
| Alignment/transcription loading | ✅ Done (buggy) |
| Vocabulary & encoding | ✅ Done |
| TF Data pipeline | ✅ Done |
| **Model architecture (CNN + RNN + CTC)** | ❌ Not implemented |
| **Training loop** | ❌ Not implemented |
| **Evaluation / metrics** | ❌ Not implemented |
| **Inference / prediction** | ❌ Not implemented |
| **Real dataset download** | ❌ Only synthetic noise |
| **Bug fix (alignments empty)** | ❌ Needs fixing |
