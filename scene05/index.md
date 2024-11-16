# Scene 05

Scene 05 recorded in the Solve4X dataset with 2 process instances.

Start: 2024-03-25 09:24:15  
End: 09:27:35 (0:03:20.066000)

This scene covers the following 2 process instances:


- [ID013](#id013): Asset repair
- [ID014](#id014): Self-service asset check-out

The scene was systematically planned prior to recording. Any deviations in behavior are intentional. 
The overall `itam.ocelxml` event log remains consistent with what is captured on camera and annotated in the video logs. 

## Resource Overview

| Resource | Entity   |
|----------|----------|
| Humans   | A1, C4  |
| Assets   | L1, K3  |



## ID013

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:24:18.350 | 09:24:25.216 | Open window    | A1 |  | window |
| 2  | 09:24:31.990 | 09:24:36.077 | other, see notes    | A1 |  | repair_desk |
| 3  | 09:24:38.892 | 09:26:27.940 | Carry out repair    | A1 | L1 | repair_desk |
| 4  | 09:26:27.940 | 09:26:52.165 | Check asset quality    | A1 | L1 | repair_desk |
| 5  | 09:27:02.837 | 09:27:14.238 | Update asset status in the system    | A1 | L1 | repair_desk |
| 6  | 09:27:15.677 | 09:27:22.475 | Move asset to storage    | A1 | L1 | laptop_shelf |

## ID014

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:26:10.000 | 09:26:16.496 | Enter room    | C4 |  | door |
| 2  | 09:26:16.597 | 09:26:19.155 | Chat    | A1, C4 |  |  |
| 3  | 09:26:17.417 | 09:26:17.417 | Pick asset from self service desk    | C4 | K3 | self_service_storage |
| 4  | 09:26:23.937 | 09:26:29.508 | Leave room    | C4 |  | door |



## Scene Files

The files related to this scene are stored in `scene05/` as follows:

| Type                  | Filename                    |
|-----------------------|-----------------------------|
| Video                 | `scene05.mp4`      |
| Video Log             | `scene05_vid.json` |
| Joined Scene OCEL[^1] | `scene05_ocel.json` |
| Video OCEL            | `scene05_video_ocel.json` |
| Ambient Sensor OCEL   | `scene05_sensors_ocel.json` |
| Motion Tracking       | `scene05_mov.csv`|
| Web Task Mining       | `scene05_ui.csv` |
| Reed Switches         | `scene05_reed_switches.csv`  |
| Distance Sensor Laptop Shelf | `scene05_distance_sensor_laptop_shelf.csv`  |
| Room Temp and Humidity | `scene05_temp_hum_sensor_window.csv` |

### Video file metrics

```json
{
  "streams": [
    {
      "index": 0,
      "codec_name": "h264",
      "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
      "profile": "High",
      "codec_type": "video",
      "codec_tag_string": "avc1",
      "codec_tag": "0x31637661",
      "width": 1280,
      "height": 1440,
      "coded_width": 1280,
      "coded_height": 1440,
      "closed_captions": 0,
      "film_grain": 0,
      "has_b_frames": 2,
      "sample_aspect_ratio": "1:1",
      "display_aspect_ratio": "8:9",
      "pix_fmt": "yuv420p",
      "level": 40,
      "chroma_location": "left",
      "field_order": "progressive",
      "refs": 1,
      "is_avc": "true",
      "nal_length_size": "4",
      "id": "0x1",
      "r_frame_rate": "30/1",
      "avg_frame_rate": "30/1",
      "time_base": "1/15360",
      "start_pts": 0,
      "start_time": "0.000000",
      "duration_ts": 3074560,
      "duration": "200.166667",
      "bit_rate": "1630983",
      "bits_per_raw_sample": "8",
      "nb_frames": "6005",
      "extradata_size": 47,
      "disposition": {
        "default": 1,
        "dub": 0,
        "original": 0,
        "comment": 0,
        "lyrics": 0,
        "karaoke": 0,
        "forced": 0,
        "hearing_impaired": 0,
        "visual_impaired": 0,
        "clean_effects": 0,
        "attached_pic": 0,
        "timed_thumbnails": 0,
        "non_diegetic": 0,
        "captions": 0,
        "descriptions": 0,
        "metadata": 0,
        "dependent": 0,
        "still_image": 0
      },
      "tags": {
        "language": "und",
        "handler_name": "VideoHandler",
        "vendor_id": "[0][0][0][0]",
        "encoder": "Lavc60.31.102 libx264"
      }
    }
  ],
  "format": {
    "filename": "scene05.mp4",
    "nb_streams": 1,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "200.166667",
    "size": "40882017",
    "bit_rate": "1633919",
    "probe_score": 100,
    "tags": {
      "major_brand": "isom",
      "minor_version": "512",
      "compatible_brands": "isomiso2avc1mp41",
      "encoder": "Lavf60.16.100"
    }
  }
}
```

[^1]: OCEL is a standard designed to facilitate the exchange of object-centric event data across various case notions. 
The [OCEL website](www.ocel-standard.org) gives further information. 