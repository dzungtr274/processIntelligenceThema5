# Scene 15

Scene 15 recorded in the Solve4X dataset with 4 process instances.

Start: 2024-03-25 11:55:41  
End: 12:02:12 (0:06:31.600000)

This scene covers the following 4 process instances:


- [ID045](#id045): Asset disbursement to clients
- [ID046](#id046): Asset repair
- [ID047](#id047): Asset disbursement to clients
- [ID048](#id048): Asset return

The scene was systematically planned prior to recording. Any deviations in behavior are intentional. 
The overall `itam.ocelxml` event log remains consistent with what is captured on camera and annotated in the video logs. 

## Resource Overview

| Resource | Entity   |
|----------|----------|
| Humans   | A2, C3, C2, C7  |
| Assets   | M4, M6, P1, T2, L6  |



## ID045

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:55:47.116 | 11:55:51.258 | Enter room    | C3 |  | door |
| 2  | 11:56:02.809 | 11:56:09.340 | Pick asset from warehouse    | A2 | M4 | monitor_storage |
| 3  | 11:56:10.757 | 11:56:44.479 | Check asset quality    | A2 | M4 | it_working_desk |
| 4  | 11:56:49.286 | 11:56:54.718 | Pick asset from warehouse    | A2 | M6 | monitor_storage |
| 5  | 11:56:55.776 | 11:57:00.935 | Check asset quality    | A2 | M6 | it_working_desk |
| 6  | 11:57:10.402 | 11:57:43.244 | Check-Out asset to user    | A2 | M4, M6 | it_working_desk |
| 7  | 11:57:45.993 | 11:57:57.785 | Handover asset to user    | A2, C3 | M4, M6 | it_working_desk |
| 8  | 11:58:00.965 | 11:58:07.526 | Leave room    | C3 | M4, M6 | door |

## ID046

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:58:15.294 | 11:59:09.329 | Carry out repair    | A2 | P1 | repair_desk |
| 2  | 11:59:25.268 | 11:59:33.852 | Check asset quality    | A2 | P1 | repair_desk |
| 3  | 11:59:35.087 | 11:59:59.262 | Update asset status in the system    | A2 | P1 | it_working_desk |
| 4  | 12:00:00.231 | 12:00:11.877 | Move asset to storage    | A2 | P1 | mouse_cupboard |

## ID047

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 11:59:45.307 | 11:59:50.018 | Enter room    | C2 |  | door |
| 2  | 12:00:26.059 | 12:00:40.648 | Pick asset from warehouse    | A2 | T2 | keyboard_cupboard |
| 3  | 12:00:42.443 | 12:00:51.406 | Check asset quality    | A2 | T2 | it_working_desk |
| 4  | 12:00:51.406 | 12:00:53.416 | Handover asset to user    | A2, C2 | T2 | it_working_desk |
| 5  | 12:00:54.714 | 12:00:58.234 | Leave room    | C2 |  | door |

## ID048

| Step            |Begin              | End     |         Activity   | Humans | Assets | Locations | 
|-----------------|------------------ |---------|--------|-----------|-------|----|
| 1  | 12:01:00.631 | 12:01:04.814 | Enter room    | C7 | L6 | door |
| 2  | 12:01:08.838 | 12:01:16.297 | Handover asset to admin    | A2, C7 | L6 | it_working_desk |
| 3  | 12:01:22.660 | 12:01:33.012 | Check asset quality    | A2 | L6 | it_working_desk |
| 4  | 12:01:36.571 | 12:01:56.131 | Check-In asset to storage    | A2 | L6 | it_working_desk |
| 5  | 12:02:01.434 | 12:02:05.261 | Move asset to storage    | A2 | L6 | laptop_shelf |
| 6  | 12:02:06.468 | 12:02:10.772 | Leave room    | C7 |  | door |



## Scene Files

The files related to this scene are stored in `scene15/` as follows:

| Type                  | Filename                    |
|-----------------------|-----------------------------|
| Video                 | `scene15.mp4`      |
| Video Log             | `scene15_vid.json` |
| Joined Scene OCEL[^1] | `scene15_ocel.json` |
| Video OCEL            | `scene15_video_ocel.json` |
| Ambient Sensor OCEL   | `scene15_sensors_ocel.json` |
| Motion Tracking       | `scene15_mov.csv`|
| Web Task Mining       | `scene15_ui.csv` |
| Reed Switches         | `scene15_reed_switches.csv`  |
| Distance Sensor Laptop Shelf | `scene15_distance_sensor_laptop_shelf.csv`  |
| Room Temp and Humidity | `scene15_temp_hum_sensor_window.csv` |

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
      "duration_ts": 6014976,
      "duration": "391.600000",
      "bit_rate": "1558517",
      "bits_per_raw_sample": "8",
      "nb_frames": "11748",
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
    "filename": "scene15.mp4",
    "nb_streams": 1,
    "nb_programs": 0,
    "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
    "format_long_name": "QuickTime / MOV",
    "start_time": "0.000000",
    "duration": "391.600000",
    "size": "76432269",
    "bit_rate": "1561435",
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