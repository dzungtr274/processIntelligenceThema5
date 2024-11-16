# Scene 04

Scene 04 recorded in the Solve4X dataset with 3 process instances.

Start: 2024-03-25 09:19:59  
End: 09:23:19 (0:03:20.066000)

This scene covers the following 3 process instances:


- [ID010](#id010): New asset inventory
- [ID011](#id011): New asset inventory
- [ID012](#id012): Asset return

The scene was systematically planned prior to recording. Any deviations in behavior are intentional. 
The overall `itam.ocelxml` event log remains consistent with what is captured on camera and annotated in the video logs. 

## Resource Overview

| Resource | Entity   |
|----------|----------|
| Humans   | A1, C2  |
| Assets   | H1, H2, M1  |



## ID010

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:20:11.041 | 09:20:17.942 | Pick asset from self service desk    | A1 | H1 | self_service_storage |
| 2  | 09:20:17.302 | 09:20:21.468 | Unpack asset    | A1 | H1 | repair_desk |
| 3  | 09:20:21.802 | 09:20:30.036 | Test asset quality and functionality    | A1 | H1 | repair_desk |
| 4  | 09:20:31.519 | 09:20:38.088 | Install and configure asset    | A1 | H1 | repair_desk |
| 5  | 09:20:44.043 | 09:20:50.574 | Label asset    | A1 | H1 | repair_desk |
| 6  | 09:20:51.436 | 09:20:55.051 | Move asset to storage    | A1 | H1 | self_service_storage |

## ID011

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:20:17.942 | 09:20:56.621 | Pick asset from warehouse    | A1 | H2 | self_service_storage |
| 2  | 09:20:57.713 | 09:21:01.263 | Unpack asset    | A1 | H2 | repair_desk |
| 3  | 09:21:01.530 | 09:21:08.928 | Test asset quality and functionality    | A1 | H2 | repair_desk |
| 4  | 09:21:09.416 | 09:21:23.639 | Install and configure asset    | A1 | H2 | it_working_desk |
| 5  | 09:21:27.132 | 09:21:32.892 | Move asset to storage    | A1 | H2 | self_service_storage |

## ID012

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:22:11.509 | 09:22:16.061 | Enter room    | C2 |  | door |
| 2  | 09:22:17.272 | 09:22:28.107 | Handover asset to admin    | A1, C2 | M1 | it_working_desk |
| 3  | 09:22:28.520 | 09:22:42.186 | Check asset quality    | A1 | M1 | it_working_desk |
| 4  | 09:22:42.625 | 09:23:01.499 | Check-In asset to storage    | A1 | M1 | it_working_desk |
| 5  | 09:23:03.942 | 09:23:10.149 | Move asset to storage    | A1 | M1 | monitor_storage |
| 6  | 09:23:06.992 | 09:23:09.911 | Leave room    | C2 |  | door |



## Scene Files

The files related to this scene are stored in `scene04/` as follows:

| Type                  | Filename                    |
|-----------------------|-----------------------------|
| Video                 | `scene04.mp4`      |
| Video Log             | `scene04_vid.json` |
| Joined Scene OCEL[^1] | `scene04_ocel.json` |
| Video OCEL            | `scene04_video_ocel.json` |
| Ambient Sensor OCEL   | `scene04_sensors_ocel.json` |
| Motion Tracking       | `scene04_mov.csv`|
| Web Task Mining       | `scene04_ui.csv` |
| Reed Switches         | `scene04_reed_switches.csv`  |
| Distance Sensor Laptop Shelf | `scene04_distance_sensor_laptop_shelf.csv`  |
| Room Temp and Humidity | `scene04_temp_hum_sensor_window.csv` |

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
      "bit_rate": "1616893",
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
    "filename": "scene04.mp4",
    "nb_streams": 1,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "200.166667",
    "size": "40529499",
    "bit_rate": "1619830",
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