# Scene 10

Scene 10 recorded in the Solve4X dataset with 3 process instances.

Start: 2024-03-25 10:58:04  
End: 11:06:04 (0:08:00.066000)

This scene covers the following 3 process instances:


- [ID028](#id028): New asset inventory
- [ID029](#id029): New asset inventory
- [ID030](#id030): Asset repair

The scene was systematically planned prior to recording. Any deviations in behavior are intentional. 
The overall `itam.ocelxml` event log remains consistent with what is captured on camera and annotated in the video logs. 

## Resource Overview

| Resource | Entity   |
|----------|----------|
| Humans   | A2, A1  |
| Assets   | H5, H7, K1  |



## ID028

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 10:58:14.370 | 10:58:27.409 | Pick asset from self service desk    | A2 | H5 | self_service_storage |
| 2  | 10:58:30.297 | 10:58:35.734 | Unpack asset    | A2 | H5 | repair_desk |
| 3  | 10:58:36.787 | 10:58:48.015 | Test asset quality and functionality    | A2 | H5 | repair_desk |
| 4  | 10:58:49.757 | 10:59:03.575 | Install and configure asset    | A2 | H5 | repair_desk |
| 5  | 10:59:04.400 | 10:59:20.067 | Label asset    | A2 | H5 | repair_desk |
| 6  | 10:59:25.761 | 10:59:59.568 | Create system entry for asset    | A2 | H5 | it_working_desk |
| 7  | 11:00:00.334 | 11:00:08.588 | Move asset to storage    | A2 | H5 | self_service_storage |

## ID029

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:00:10.733 | 11:00:17.246 | Pick asset from warehouse    | A2 | H7 | self_service_storage |
| 2  | 11:00:23.234 | 11:00:28.778 | Unpack asset    | A2 | H7 | repair_desk |
| 3  | 11:00:31.772 | 11:00:56.255 | Create system entry for asset    | A2 | H7 | it_working_desk |
| 4  | 11:01:00.438 | 11:01:05.456 | Test asset quality and functionality    | A2 | H7 | repair_desk |
| 5  | 11:01:06.321 | 11:01:23.983 | Install and configure asset    | A2 | H7 | repair_desk |
| 6  | 11:01:24.342 | 11:01:28.334 | Label asset    | A2 | H7 | repair_desk |
| 7  | 11:01:32.232 | 11:01:35.817 | Move asset to storage    | A2 | H7 | self_service_storage |

## ID030

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:02:24.162 | 11:02:50.502 | Carry out repair    | A2 | K1 | repair_desk |
| 2  | 11:02:53.818 | 11:03:05.266 | Pick asset from warehouse    | A2 |  |  |
| 3  | 11:03:09.172 | 11:03:47.591 | Carry out repair    | A2 | K1 | repair_desk |
| 4  | 11:03:51.719 | 11:04:45.222 | Check asset quality    | A2 | K1 | it_working_desk |
| 5  | 11:04:46.494 | 11:05:23.849 | Update asset status in the system    | A2 | K1 | it_working_desk |
| 6  | 11:05:47.536 | 11:05:52.368 | Update asset status in the system    | A2 | K1 | it_working_desk |
| 7  | 11:05:54.789 | 11:06:01.427 | Move asset to storage    | A2 | K1 | self_service_storage |



## Scene Files

The files related to this scene are stored in `scene10/` as follows:

| Type                  | Filename                    |
|-----------------------|-----------------------------|
| Video                 | `scene10.mp4`      |
| Video Log             | `scene10_vid.json` |
| Joined Scene OCEL[^1] | `scene10_ocel.json` |
| Video OCEL            | `scene10_video_ocel.json` |
| Ambient Sensor OCEL   | `scene10_sensors_ocel.json` |
| Motion Tracking       | `scene10_mov.csv`|
| Web Task Mining       | `scene10_ui.csv` |
| Reed Switches         | `scene10_reed_switches.csv`  |
| Distance Sensor Laptop Shelf | `scene10_distance_sensor_laptop_shelf.csv`  |
| Room Temp and Humidity | `scene10_temp_hum_sensor_window.csv` |

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
      "duration_ts": 7375360,
      "duration": "480.166667",
      "bit_rate": "1487569",
      "bits_per_raw_sample": "8",
      "nb_frames": "14405",
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
    "filename": "scene10.mp4",
    "nb_streams": 1,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "480.166667",
    "size": "89460026",
    "bit_rate": "1490482",
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