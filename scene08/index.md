# Scene 08

Scene 08 recorded in the Solve4X dataset with 3 process instances.

Start: 2024-03-25 09:49:03  
End: 09:56:11 (0:07:07.366000)

This scene covers the following 3 process instances:


- [ID022](#id022): Defective asset return for repair
- [ID023](#id023): Defective asset return for repair
- [ID024](#id024): Asset return

The scene was systematically planned prior to recording. Any deviations in behavior are intentional. 
The overall `itam.ocelxml` event log remains consistent with what is captured on camera and annotated in the video logs. 

## Resource Overview

| Resource | Entity   |
|----------|----------|
| Humans   | A1, C6, C5  |
| Assets   | H4, K1, K2, L2, P3  |



## ID022

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:49:43.193 | 09:49:48.937 | Enter room    | C6 |  | door |
| 2  | 09:49:58.530 | 09:50:13.239 | Describe quality issue    | A1, C6 | H4 | it_working_desk |
| 3  | 09:50:13.598 | 09:51:01.584 | Check asset quality    | A1 | H4 | it_working_desk |
| 4  | 09:51:04.113 | 09:51:30.427 | Chat    | A1, C6 | H4 | it_working_desk |
| 5  | 09:51:30.952 | 09:51:33.877 | Handover asset to user    | A1, C6 | H4 | it_working_desk |
| 6  | 09:51:35.833 | 09:51:39.295 | Leave room    | C6 |  | door |

## ID023

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:49:43.193 | 09:49:48.937 | Enter room    | C5 |  | door |
| 2  | 09:51:35.964 | 09:51:45.536 | Describe quality issue    | A1, C5 | K1 | it_working_desk |
| 3  | 09:51:47.252 | 09:52:22.500 | Check asset quality    | A1 | K1 | it_working_desk |
| 4  | 09:52:28.907 | 09:52:33.979 | Move asset to repair desk    | A1 | K1 | repair_desk |
| 5  | 09:52:36.121 | 09:52:40.936 | Pick asset from warehouse    | A1 | K2 | self_service_storage |
| 6  | 09:52:44.285 | 09:53:04.935 | Check asset quality    | A1 | K2 |  |
| 7  | 09:53:05.968 | 09:53:07.812 | Handover asset to user    | A1, C5 | K2 | it_working_desk |
| 8  | 09:53:15.096 | 09:53:18.943 | Leave room    | C5 |  | door |

## ID024

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:54:06.053 | 09:54:11.650 | Enter room    | C6 |  | door |
| 2  | 09:54:29.135 | 09:54:30.204 | Handover asset to admin    | A1, C6 | L2, P3 | it_working_desk |
| 3  | 09:54:33.020 | 09:54:49.271 | Check asset quality    | A1 |  | it_working_desk |
| 4  | 09:54:49.151 | 09:54:52.803 | Move asset to storage    | A1 |  | laptop_shelf |
| 5  | 09:54:54.747 | 09:55:06.210 | Check asset quality    | A1 | L2, P3 | it_working_desk |
| 6  | 09:55:09.789 | 09:55:28.562 | Check-In asset to storage    | A1 | L2 | it_working_desk |
| 7  | 09:55:29.949 | 09:55:37.117 | Move asset to storage    | A1 | L2 | laptop_shelf |
| 8  | 09:55:40.181 | 09:55:43.092 | Leave room    | C6 |  | door |



## Scene Files

The files related to this scene are stored in `scene08/` as follows:

| Type                  | Filename                    |
|-----------------------|-----------------------------|
| Video                 | `scene08.mp4`      |
| Video Log             | `scene08_vid.json` |
| Joined Scene OCEL[^1] | `scene08_ocel.json` |
| Video OCEL            | `scene08_video_ocel.json` |
| Ambient Sensor OCEL   | `scene08_sensors_ocel.json` |
| Motion Tracking       | `scene08_mov.csv`|
| Web Task Mining       | `scene08_ui.csv` |
| Reed Switches         | `scene08_reed_switches.csv`  |
| Distance Sensor Laptop Shelf | `scene08_distance_sensor_laptop_shelf.csv`  |
| Room Temp and Humidity | `scene08_temp_hum_sensor_window.csv` |

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
      "duration_ts": 6564352,
      "duration": "427.366667",
      "bit_rate": "1479357",
      "bits_per_raw_sample": "8",
      "nb_frames": "12821",
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
    "filename": "scene08.mp4",
    "nb_streams": 1,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "427.366667",
    "size": "79184192",
    "bit_rate": "1482271",
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