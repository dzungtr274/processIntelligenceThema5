# Scene 07

Scene 07 recorded in the Solve4X dataset with 3 process instances.

Start: 2024-03-25 09:39:03  
End: 09:45:43 (0:06:40)

This scene covers the following 3 process instances:


- [ID019](#id019): New asset inventory
- [ID020](#id020): New asset inventory
- [ID021](#id021): Asset disbursement to clients

The scene was systematically planned prior to recording. Any deviations in behavior are intentional. 
The overall `itam.ocelxml` event log remains consistent with what is captured on camera and annotated in the video logs. 

## Resource Overview

| Resource | Entity   |
|----------|----------|
| Humans   | A1, C8  |
| Assets   | K2, H3, L5  |



## ID019

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:39:50.000 | 09:39:57.000 | Pick asset from self service desk    | A1 | K2 | self_service_storage |
| 2  | 09:39:59.000 | 09:40:15.000 | Unpack asset    | A1 | K2 | repair_desk |
| 3  | 09:40:15.000 | 09:40:53.000 | Test asset quality and functionality    | A1 | K2 | it_working_desk |
| 4  | 09:40:38.000 | 09:40:53.000 | Install and configure asset    | A1 | K2 | repair_desk |
| 5  | 09:40:54.000 | 09:41:20.000 | Create system entry for asset    | A1 | K2 | it_working_desk |
| 6  | 09:41:22.000 | 09:41:28.000 | Move asset to storage    | A1 | K2 | self_service_storage |

## ID020

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:39:49.808 | 09:39:57.581 | Pick asset from self service desk    | A1 | H3 | self_service_storage |
| 2  | 09:41:42.546 | 09:41:50.546 | Unpack asset    | A1 | H3 | repair_desk |
| 3  | 09:41:54.546 | 09:42:19.546 | Test asset quality and functionality    | A1 | H3 | it_working_desk |
| 4  | 09:42:24.546 | 09:43:00.546 | Create system entry for asset    | A1 | H3 | it_working_desk |
| 5  | 09:42:32.546 | 09:42:47.546 | Move asset to storage    | C8 | H3 | self_service_storage |

## ID021

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 09:42:16.382 | 09:42:24.382 | Enter room    | C8 |  | door |
| 2  | 09:43:13.382 | 09:43:36.382 | Pick asset from warehouse    | A1 | L5 | laptop_shelf |
| 3  | 09:43:52.382 | 09:44:41.382 | Check asset quality    | A1 | L5 | it_working_desk |
| 4  | 09:45:09.382 | 09:45:12.382 | Handover asset to user    | A1, C8 | L5 | it_working_desk |
| 5  | 09:45:19.382 | 09:45:28.382 | Leave room    | C8 |  | door |



## Scene Files

The files related to this scene are stored in `scene07/` as follows:

| Type                  | Filename                    |
|-----------------------|-----------------------------|
| Video                 | `scene07.mp4`      |
| Video Log             | `scene07_vid.json` |
| Joined Scene OCEL[^1] | `scene07_ocel.json` |
| Video OCEL            | `scene07_video_ocel.json` |
| Ambient Sensor OCEL   | `scene07_sensors_ocel.json` |
| Motion Tracking       | `scene07_mov.csv`|
| Web Task Mining       | `scene07_ui.csv` |
| Reed Switches         | `scene07_reed_switches.csv`  |
| Distance Sensor Laptop Shelf | `scene07_distance_sensor_laptop_shelf.csv`  |
| Room Temp and Humidity | `scene07_temp_hum_sensor_window.csv` |

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
      "duration_ts": 6146560,
      "duration": "400.166667",
      "bit_rate": "1615387",
      "bits_per_raw_sample": "8",
      "nb_frames": "12005",
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
    "filename": "scene07.mp4",
    "nb_streams": 1,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "400.166667",
    "size": "80949011",
    "bit_rate": "1618305",
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