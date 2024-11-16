# Scene 13

Scene 13 recorded in the Solve4X dataset with 3 process instances.

Start: 2024-03-25 11:31:32  
End: 11:44:01 (0:12:29.845000)

This scene covers the following 3 process instances:


- [ID039](#id039): Asset disbursement to clients
- [ID040](#id040): Asset disbursement to clients
- [ID041](#id041): Defective asset return for repair

The scene was systematically planned prior to recording. Any deviations in behavior are intentional. 
The overall `itam.ocelxml` event log remains consistent with what is captured on camera and annotated in the video logs. 

## Resource Overview

| Resource | Entity   |
|----------|----------|
| Humans   | A2, C7, C8, C2  |
| Assets   | L6, T3, P2, M3, L3, L1  |



## ID039

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:31:40.487 | 11:31:45.010 | Enter room    | C7 |  | door |
| 2  | 11:31:45.010 | 11:32:58.398 | Chat    | A2, C7 |  |  |
| 3  | 11:33:06.101 | 11:33:22.149 | Pick asset from warehouse    | A2 | L16 | laptop_shelf |
| 4  | 11:33:22.695 | 11:33:49.136 | Check asset quality    | A2 | L16 | it_working_desk |
| 5  | 11:33:55.333 | 11:34:12.246 | Pick asset from warehouse    | A2 | T3 | keyboard_cupboard |
| 6  | 11:34:14.977 | 11:34:25.926 | Pick asset from warehouse    | A2 | P2 | mouse_cupboard |
| 7  | 11:34:27.636 | 11:34:31.077 | Check asset quality    | A2 | T3 | it_working_desk |
| 8  | 11:34:31.908 | 11:34:42.324 | Check asset quality    | A2 | P2 | it_working_desk |
| 9  | 11:34:44.943 | 11:35:13.138 | Check-Out asset to user    | A2 | L16 | it_working_desk |
| 10  | 11:35:14.801 | 11:35:31.309 | Move asset to storage    | A2 | L16 | laptop_shelf |
| 11  | 11:35:32.481 | 11:35:45.725 | Pick asset from warehouse    | A2 | L6 | laptop_shelf |
| 12  | 11:35:46.878 | 11:36:42.259 | Check-Out asset to user    | A2 | L6, T3, P2 | it_working_desk |
| 13  | 11:36:58.414 | 11:37:10.046 | Handover asset to user    | A2, C7 | L6, T3, P2 | it_working_desk |
| 14  | 11:37:18.444 | 11:37:22.824 | Leave room    | C7 | L6, T3, P2 | door |

## ID040

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:37:51.310 | 11:37:58.019 | Enter room    |  |  | door |
| 2  | 11:37:58.019 | 11:38:09.055 | Leave room    |  |  | door |
| 3  | 11:38:47.094 | 11:38:56.387 | Enter room    | C8 |  | door |
| 4  | 11:39:05.372 | 11:39:14.860 | Pick asset from warehouse    | A2 | M3 | monitor_storage |
| 5  | 11:39:15.635 | 11:39:29.127 | Check asset quality    | A2 | M3 | it_working_desk |
| 6  | 11:39:32.876 | 11:40:05.271 | Check-Out asset to user    | A2 | M3 | it_working_desk |
| 7  | 11:40:06.277 | 11:40:11.745 | Handover asset to user    | A2, C8 | M3 | it_working_desk |
| 8  | 11:40:14.978 | 11:40:20.920 | Leave room    | C8 | M3 | door |

## ID041

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:40:27.237 | 11:40:31.825 | Enter room    | C2 | L3 | door |
| 2  | 11:40:33.024 | 11:40:45.143 | Describe quality issue    | A2, C2 | L3 | it_working_desk |
| 3  | 11:40:45.143 | 11:41:16.286 | Check asset quality    | A2 | L3 | it_working_desk |
| 4  | 11:41:23.281 | 11:41:50.854 | Check-In asset for repair    | A2 | L3 | it_working_desk |
| 5  | 11:41:57.343 | 11:42:04.395 | Move asset to repair desk    | A2 | L3 | repair_desk |
| 6  | 11:42:07.923 | 11:42:15.347 | Pick asset from warehouse    | A2 | L1 | laptop_shelf |
| 7  | 11:42:15.347 | 11:42:27.022 | Check asset quality    | A2 | L1 | it_working_desk |
| 8  | 11:42:27.022 | 11:43:03.136 | Check-Out asset to user    | A2 | L1 | it_working_desk |
| 9  | 11:43:08.169 | 11:43:11.842 | Handover asset to user    | A2, C2 | L1 |  |
| 10  | 11:43:08.169 | 11:43:18.265 | Leave room    | C2 | L1 | door |



## Scene Files

The files related to this scene are stored in `scene13/` as follows:

| Type                  | Filename                    |
|-----------------------|-----------------------------|
| Video                 | `scene13.mp4`      |
| Video Log             | `scene13_vid.json` |
| Joined Scene OCEL[^1] | `scene13_ocel.json` |
| Video OCEL            | `scene13_video_ocel.json` |
| Ambient Sensor OCEL   | `scene13_sensors_ocel.json` |
| Motion Tracking       | `scene13_mov.csv`|
| Web Task Mining       | `scene13_ui.csv` |
| Reed Switches         | `scene13_reed_switches.csv`  |
| Distance Sensor Laptop Shelf | `scene13_distance_sensor_laptop_shelf.csv`  |
| Room Temp and Humidity | `scene13_temp_hum_sensor_window.csv` |

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
      "duration_ts": 11553792,
      "duration": "752.200000",
      "bit_rate": "1607830",
      "bits_per_raw_sample": "8",
      "nb_frames": "22566",
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
    "filename": "scene13.mp4",
    "nb_streams": 1,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "752.200000",
    "size": "151449929",
    "bit_rate": "1610741",
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