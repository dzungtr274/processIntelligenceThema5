# Scene 09

Scene 09 recorded in the Solve4X dataset with 3 process instances.

Start: 2024-03-25 10:45:00  
End: 10:54:28 (0:09:28.200000)

This scene covers the following 3 process instances:


- [ID025](#id025): Asset disbursement to clients
- [ID026](#id026): Asset disbursement to clients
- [ID027](#id027): Asset disbursement to clients

The scene was systematically planned prior to recording. Any deviations in behavior are intentional. 
The overall `itam.ocelxml` event log remains consistent with what is captured on camera and annotated in the video logs. 

## Resource Overview

| Resource | Entity   |
|----------|----------|
| Humans   | A2, C3, C1, C2  |
| Assets   | L1, L2, T1, P1, L3  |



## ID025

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 10:45:08.459 | 10:45:14.157 | Enter room    | C3 |  | door |
| 2  | 10:45:19.503 | 10:45:50.374 | Chat    | A2, C3 |  | it_working_desk |
| 3  | 10:45:51.777 | 10:46:01.861 | Pick asset from warehouse    | A2 | L1 | laptop_shelf |
| 4  | 10:46:07.852 | 10:46:45.112 | Check asset quality    | A2 | L1 | it_working_desk |
| 5  | 10:46:45.736 | 10:47:36.295 | Check-Out asset to user    | A2 | L1 | it_working_desk |
| 6  | 10:47:39.218 | 10:47:42.150 | Handover asset to user    | A2, C3 | L1 | it_working_desk |
| 7  | 10:47:44.119 | 10:47:47.315 | Leave room    | A2 |  | door |

## ID026

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 10:48:12.481 | 10:48:17.792 | Enter room    | C1 |  | door |
| 2  | 10:48:18.988 | 10:49:09.840 | Chat    | A2, C1, C2 |  |  |
| 3  | 10:49:11.793 | 10:49:34.619 | Pick asset from warehouse    | A2 | T1, P1 | mouse_cupboard, keyboard_cupboard |
| 4  | 10:49:37.207 | 10:49:55.838 | Check asset quality    | A2 | T1, P1 | it_working_desk |
| 5  | 10:50:16.717 | 10:50:25.507 | Pick asset from warehouse    | A2 | L2 | laptop_shelf |
| 6  | 10:50:26.859 | 10:51:01.511 | Check asset quality    | A2 | L2 | it_working_desk |
| 7  | 10:51:05.466 | 10:52:17.597 | Check-Out asset to user    | A2 | L2, T1, P1 | it_working_desk |
| 8  | 10:52:23.278 | 10:52:29.622 | Handover asset to user    | A2, C1 | L2 | it_working_desk |
| 9  | 10:52:38.143 | 10:52:41.862 | Leave room    | C1 |  | door |

## ID027

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 10:48:16.657 | 10:48:21.458 | Enter room    | C2 |  | door |
| 2  | 10:52:37.563 | 10:52:41.893 | Chat    | A2, C2 |  | it_working_desk |
| 3  | 10:52:42.823 | 10:52:52.129 | Pick asset from warehouse    | A2 | L3 | laptop_shelf |
| 4  | 10:52:53.345 | 10:53:16.537 | Check asset quality    | A2 | L3 | it_working_desk |
| 5  | 10:53:22.152 | 10:53:41.160 | Check-Out asset to user    | A2 | L3 | it_working_desk |
| 6  | 10:53:41.949 | 10:53:44.887 | Handover asset to user    | A2, C2 | L3 | it_working_desk |
| 7  | 10:53:47.983 | 10:53:51.193 | Leave room    | C2 |  | door |



## Scene Files

The files related to this scene are stored in `scene09/` as follows:

| Type                  | Filename                    |
|-----------------------|-----------------------------|
| Video                 | `scene09.mp4`      |
| Video Log             | `scene09_vid.json` |
| Joined Scene OCEL[^1] | `scene09_ocel.json` |
| Video OCEL            | `scene09_video_ocel.json` |
| Ambient Sensor OCEL   | `scene09_sensors_ocel.json` |
| Motion Tracking       | `scene09_mov.csv`|
| Web Task Mining       | `scene09_ui.csv` |
| Reed Switches         | `scene09_reed_switches.csv`  |
| Distance Sensor Laptop Shelf | `scene09_distance_sensor_laptop_shelf.csv`  |
| Room Temp and Humidity | `scene09_temp_hum_sensor_window.csv` |

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
      "duration_ts": 8727552,
      "duration": "568.200000",
      "bit_rate": "1658996",
      "bits_per_raw_sample": "8",
      "nb_frames": "17046",
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
    "filename": "scene09.mp4",
    "nb_streams": 1,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "568.200000",
    "size": "118037196",
    "bit_rate": "1661910",
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